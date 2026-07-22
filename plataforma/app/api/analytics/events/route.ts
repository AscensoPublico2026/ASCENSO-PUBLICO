import { NextRequest, NextResponse } from "next/server";
import { createAdminClient } from "@/lib/supabase/server";
import {
  isAnalyticsEventName,
  sanitizeAnalyticsProperties,
} from "@/lib/analytics";

export const dynamic = "force-dynamic";

const UUID_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const RATE_WINDOW_MS = 60_000;
const RATE_LIMIT = 90;
const rateBuckets = new Map<string, { count: number; resetAt: number }>();

function sameOrigin(req: NextRequest): boolean {
  const origin = req.headers.get("origin");
  if (!origin) return false;
  try {
    return new URL(origin).origin === req.nextUrl.origin;
  } catch {
    return false;
  }
}

function withinRateLimit(req: NextRequest): boolean {
  const forwarded = req.headers.get("x-forwarded-for")?.split(",")[0]?.trim();
  const key = forwarded || "unknown";
  const now = Date.now();
  if (rateBuckets.size > 2_000) {
    for (const [storedKey, stored] of rateBuckets) {
      if (stored.resetAt <= now) rateBuckets.delete(storedKey);
    }
  }
  const bucket = rateBuckets.get(key);
  if (!bucket || bucket.resetAt <= now) {
    rateBuckets.set(key, { count: 1, resetAt: now + RATE_WINDOW_MS });
    return true;
  }
  bucket.count += 1;
  return bucket.count <= RATE_LIMIT;
}

export async function POST(req: NextRequest) {
  if (!sameOrigin(req)) {
    return NextResponse.json({ ok: false }, { status: 403 });
  }
  if (!withinRateLimit(req)) {
    return NextResponse.json({ ok: false }, { status: 429 });
  }

  const contentLength = Number(req.headers.get("content-length") || "0");
  if (contentLength > 8_192) {
    return NextResponse.json({ ok: false }, { status: 413 });
  }

  let body: unknown;
  try {
    const rawBody = await req.text();
    if (rawBody.length > 8_192) {
      return NextResponse.json({ ok: false }, { status: 413 });
    }
    body = JSON.parse(rawBody);
  } catch {
    return NextResponse.json({ ok: false }, { status: 400 });
  }

  const payload = body && typeof body === "object" && !Array.isArray(body)
    ? body as Record<string, unknown>
    : {};
  if (!isAnalyticsEventName(payload.event_name)) {
    return NextResponse.json({ ok: false }, { status: 400 });
  }

  const sessionId = typeof payload.anonymous_session_id === "string" && UUID_RE.test(payload.anonymous_session_id)
    ? payload.anonymous_session_id
    : null;

  try {
    const admin = createAdminClient();
    const { error } = await admin.from("analytics_events").insert({
      event_name: payload.event_name,
      anonymous_session_id: sessionId,
      properties: sanitizeAnalyticsProperties(payload.properties),
    });
    if (error) {
      console.error("[analytics/events]", error.message);
      return NextResponse.json({ ok: false }, { status: 503 });
    }
  } catch (error) {
    console.error("[analytics/events]", error);
    return NextResponse.json({ ok: false }, { status: 503 });
  }

  return NextResponse.json({ ok: true }, { status: 202 });
}
