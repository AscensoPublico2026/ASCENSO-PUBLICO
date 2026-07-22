import "server-only";

import { createHash } from "crypto";
import { createAdminClient } from "@/lib/supabase/server";
import {
  sanitizeAnalyticsProperties,
  type AnalyticsEventName,
  type AnalyticsProperties,
} from "@/lib/analytics";

export function analyticsEventKey(prefix: string, value: string): string {
  const digest = createHash("sha256").update(value).digest("hex").slice(0, 32);
  return `${prefix}:${digest}`;
}

export async function trackServerEvent(
  eventName: AnalyticsEventName,
  properties: AnalyticsProperties = {},
  options: { eventKey?: string } = {},
): Promise<void> {
  try {
    const supabase = createAdminClient();
    const { error } = await supabase.from("analytics_events").insert({
      event_name: eventName,
      event_key: options.eventKey || null,
      properties: sanitizeAnalyticsProperties(properties),
    });

    if (error && error.code !== "23505" && error.code !== "42P01") {
      console.error("[analytics] No se pudo guardar el evento:", error.message);
    }
  } catch (error) {
    console.error("[analytics] Error no bloqueante:", error);
  }
}
