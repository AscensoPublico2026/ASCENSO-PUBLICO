-- ============================================================
-- MIGRACIÓN: Cargar el curso DIAN Gestor I de Andrés
-- ============================================================
-- Ejecutar UNA VEZ en el SQL Editor de Supabase.
--
-- Andrés Guillermo Díaz Zamora  (andizam20@hotmail.com)
-- Cargo: Gestor I  ·  Código 301  ·  Grado 01  ·  OPEC 198368
-- Nivel: Profesional
-- Entidad: DIAN (Dirección de Impuestos y Aduanas Nacionales)
-- Proceso: Fiscalización y Liquidación
-- Concurso: CNSC
--
-- Carga las 21 sesiones del plan aprobado. Es IDEMPOTENTE: solo inserta
-- las guías que aún no existan en el curso (no duplica por archivo_path).
-- ============================================================

DO $$
DECLARE
  v_curso_id uuid;
  v_count int;
BEGIN
  -- 1) Buscar el curso de Andrés por correo + OPEC
  SELECT c.id INTO v_curso_id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'andizam20@hotmail.com'
    AND c.opec = '198368'
  ORDER BY c.created_at DESC
  LIMIT 1;

  -- Fallback: si no se halló con ese OPEC exacto, buscar solo por correo
  IF v_curso_id IS NULL THEN
    SELECT c.id INTO v_curso_id
    FROM public.cursos c
    JOIN public.profiles p ON p.id = c.usuario_id
    WHERE LOWER(p.correo) = 'andizam20@hotmail.com'
    ORDER BY c.created_at DESC
    LIMIT 1;
  END IF;

  IF v_curso_id IS NULL THEN
    RAISE EXCEPTION 'No se encontró el curso de Andrés (andizam20@hotmail.com). Verifica que el curso exista en la tabla cursos.';
  END IF;

  RAISE NOTICE 'Curso de Andrés encontrado: %', v_curso_id;

  SELECT COUNT(*) INTO v_count FROM public.guias_curso WHERE curso_id = v_curso_id;
  IF v_count > 0 THEN
    RAISE NOTICE 'El curso ya tiene % guías. Se agregarán solo las que falten (sin duplicar).', v_count;
  END IF;

  -- 2) Insertar las 21 sesiones del plan DIAN Gestor I (solo las que no existan)
  INSERT INTO public.guias_curso (curso_id, dia, titulo, tipo, orden, archivo_path)
  SELECT v_curso_id, dia, titulo, tipo::tipo_guia, orden, archivo_path
  FROM (VALUES
    -- Día 1: Conoce tu Entidad DIAN (general, reutilizable)
    (1,  'Conoce tu Entidad: DIAN',                                                         'general',    1,  'guias/ENT-DIAN-01-conoce-entidad-dian.html'),
    -- Días 2-4: Generales CNSC (reutilizables)
    (2,  'Estado, Función Pública y Servidores',                                            'general',    2,  'guias/GEN-01-estado-funcion-publica.html'),
    (3,  'Relación Estado-Ciudadano, Participación y Derechos',                             'general',    3,  'guias/GEN-02-relacion-estado-ciudadano.html'),
    (4,  'Marco Institucional y CNSC',                                                      'general',    4,  'guias/GEN-03-marco-institucional.html'),
    -- Días 5-8: Comportamentales DIAN (Nivel Profesional)
    (5,  'Comportamiento Ético y Adaptabilidad',                                            'nivel',      5,  'guias/DIAN-PRO-COM-01-comportamiento-etico-adaptabilidad.html'),
    (6,  'Comunicación Efectiva y Trabajo en Equipo',                                       'nivel',      6,  'guias/DIAN-PRO-COM-02-comunicacion-trabajo-equipo.html'),
    (7,  'Orientación al Logro y al Usuario/Ciudadano',                                     'nivel',      7,  'guias/DIAN-PRO-COM-03-orientacion-logro-usuario.html'),
    (8,  'Alcance del Cargo Gestor I y Evaluación',                                         'nivel',      8,  'guias/DIAN-PRO-COM-04-alcance-cargo-gestor-i.html'),
    -- Días 9-20: Funcionales DIAN (Fiscalización y Liquidación)
    (9,  'Generalidades del Sistema Tributario, Aduanero y Cambiario',                      'funcional',  9,  'guias/FUN-DIAN-01-generalidades-sistema-tributario-aduanero-cambiario.html'),
    (10, 'Determinación y Control Tributario',                                              'funcional',  10, 'guias/FUN-DIAN-02-determinacion-control-tributario.html'),
    (11, 'Proceso de Fiscalización y Liquidación',                                          'funcional',  11, 'guias/FUN-DIAN-03-proceso-fiscalizacion-liquidacion.html'),
    (12, 'Fiscalización Aduanera',                                                          'funcional',  12, 'guias/FUN-DIAN-04-fiscalizacion-aduanera.html'),
    (13, 'Régimen Cambiario',                                                               'funcional',  13, 'guias/FUN-DIAN-05-regimen-cambiario.html'),
    (14, 'Fiscalización Internacional y Precios de Transferencia',                          'funcional',  14, 'guias/FUN-DIAN-06-fiscalizacion-internacional.html'),
    (15, 'Evasión, Elusión y Contrabando',                                                  'funcional',  15, 'guias/FUN-DIAN-07-evasion-elusion-contrabando.html'),
    (16, 'Lavado de Activos y Financiación del Terrorismo (LA/FT)',                         'funcional',  16, 'guias/FUN-DIAN-08-lavado-activos-laft.html'),
    (17, 'CPACA y Procedimiento Administrativo (Ley 1437/2011)',                            'funcional',  17, 'guias/FUN-JUR-01-cpaca-procedimiento-administrativo.html'),
    (18, 'MIPG: Modelo Integrado de Planeación y Gestión',                                 'funcional',  18, 'guias/FUN-MIPG-01-mipg-gestion-publica.html'),
    (19, 'Gestión Documental, PQRSF y Servicio al Ciudadano',                              'funcional',  19, 'guias/FUN-DOC-01-gestion-documental-pqrsf-servicio.html'),
    (20, 'Herramientas Informáticas e Informes de Gestión',                                 'funcional',  20, 'guias/FUN-DIAN-09-herramientas-informaticas-informes.html'),
    -- Día 21: Simulacro Integral Final (70 preguntas)
    (21, 'Simulacro Integral Final — DIAN Gestor I (70 preguntas)',                         'simulacro',  21, 'simulacro/SIM-DIAN-001.html')
  ) AS t(dia, titulo, tipo, orden, archivo_path)
  WHERE NOT EXISTS (
    SELECT 1 FROM public.guias_curso gc
    WHERE gc.curso_id = v_curso_id
      AND gc.archivo_path = t.archivo_path
  );

  GET DIAGNOSTICS v_count = ROW_COUNT;
  RAISE NOTICE '✅ Se insertaron % guías nuevas en el curso de Andrés (DIAN Gestor I).', v_count;
END $$;

-- ============================================================
-- VERIFICACIÓN (opcional): ejecutar después para confirmar
-- ============================================================
-- SELECT gc.dia, gc.titulo, gc.tipo, gc.archivo_path
-- FROM public.guias_curso gc
-- JOIN public.cursos c ON c.id = gc.curso_id
-- JOIN public.profiles p ON p.id = c.usuario_id
-- WHERE LOWER(p.correo) = 'andizam20@hotmail.com'
-- ORDER BY gc.dia, gc.orden;
-- ============================================================
