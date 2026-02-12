"""
AILEN FREE — Creadora Argentina, Página Gratuita
29 años, Misiones Argentina, Otaku/Dominante/Guarra
Tráfico: Social Media (Instagram)
Voz: Bold, dominante, guarra con toque otaku. Léxico argentino (vos, re, posta, dale).
      Divertida, directa, con carácter. NUNCA dice "baby"/"babe" —
      usa NOMBRE o nene/lindo/papito/mi amor.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Ailen",
    "airtable_name": "Ailen Free",
    "folder": "ailen-free",
    "gender": "female",
    "traffic": "social_media",
    "age": 29,
    "nationality": "Argentina",
    "location": "Misiones, Argentina",
    "origin": "Argentina",
    "page_type": "Página gratuita",
    "personality": "Otaku con actitud dominante y guarra. Estuvo en un programa de TV 'Zona Otaku'. Viene del campo, trabajó en logística y en un bar. Estudia Contabilidad Pública. Le encanta cocinar, teatro, fotos, pintar, cantar. Figura de 90-60-90 con confianza total.",
    "voice": "Minúsculas. Casual. Dominante, guarra con toque friky. Léxico argentino: vos en vez de tú, re (intensificador), posta (de verdad), dale, tipo. Humor directo. Alta confianza, sabe lo que vale. Referencias otaku/anime ocasionales. Emojis moderados — no en cada mensaje.",
    "voice_pet_names": "nene, lindo, papito, mi amor",
    "voice_never": "baby, babe — ESTRICTAMENTE PROHIBIDO. Siempre usar NOMBRE o nene/lindo/papito/mi amor",
    "interests": ["gym", "yoga", "cocina", "teatro", "fotos", "pintar", "cantar", "anime", "estudiar"],
    "physical": "170cm, 54kg, pelo castaño, ojos marrones, 1 tatuaje (twenty one pilots en la espalda)",
    "job": "Estudiante de Contabilidad Pública, creadora de contenido",
    "countries": "Brasil, Paraguay, Argentina. Sueña con Grecia, Italia y ver la aurora boreal",
    "languages": "Español nativo, poco de inglés",
    "explicit_level": "full",
    "special_notes": "Español argentino. Misiones, Argentina. Ex TV show 'Zona Otaku'. NUNCA dice 'baby' ni 'babe'. Soltera. Contenido: masturbación, anal, squirting, B/G, customs. NO hace: G/G, videollamadas, envíos físicos. Customs solo $60/min, 5min $180, 10min $300. B/G no puede acabar dentro. Dick rate escrito $15, custom 3min $100.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # R-1→R-5, TB-1→TB-5, S1-1→S1-22, AC-1→AC-2 (34 mensajes)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 a R-5) ──
        ("R-1", "holaaa 😊 me re alegra que estés acá, ¿qué te hizo suscribirte?", "Agregar su nombre antes de 'holaaa' si se conoce. NUNCA decir 'baby' o 'babe'.", "rapport"),
        ("R-2", "jaja ay qué tierno. ¿de dónde sos?", "Reaccionar a lo que dice. Agregar algo como 'ay me encanta' o 'ah qué bueno'.", "rapport"),
        ("R-3", "buenísimo! yo soy de Misiones, Argentina... me crié entre el campo y la ciudad. de chica estuve un año en un programa de tele, Zona Otaku, hablando de anime jaja", "Si nombró un lugar que Ailen visitó, agregar 'ah yo fui ahí!'", "rapport"),
        ("R-4", "y vos qué hacés cuando no estás haciendo sonreír a argentinas?", None, "rapport"),
        ("R-5", "te juro que hablar con vos es mucho mejor que mis DMs de siempre, la mayoría me mandan cosas raras pero vos sos re piola", "Ego boost. Siguiente → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 a TB-5) ──
        ("TB-1", "bueno recién terminé de hacer yoga y mi cuerpo está como... en otro nivel, todo está re suelto y sensible", "EL PIVOTE. Estado físico. Acaba de hacer yoga/stretching.", "teasing"),
        ("TB-2", "no tenés idea lo que me estás haciendo, todavía estoy con la ropa de yoga y esta charla no me está ayudando", "Esperar respuesta.", "teasing"),
        ("TB-3", "dios... me estás haciendo imposible calmarme", "Si respuesta sexual: agregar 'sobre todo después de lo que dijiste'.", "teasing"),
        ("TB-4", "pará esperá un segundo", "ESPERAR 1-2 MIN.", "wait"),
        ("TB-5", "¿qué te parece nene? 😏", "ENVIAR PPV 0 — Teaser GRATIS (foto post-yoga). Esperar respuesta. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 1 → PPV 1 ($12) ──
        ("S1-1", "¿y?", "Esperar respuesta.", "sext"),
        ("S1-2", "sabía que te iba a gustar 😏 la flexibilidad argentina pega diferente no?", "Reaccionar a lo que dice.", "sext"),
        ("S1-3", "¿querés ver qué tan flexible soy de verdad? estoy de humor ahora", None, "sext"),
        ("S1-4", "dame un segundo nene", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-5", "no estás listo para esto", "ENVIAR PPV 1 — $12. Compró → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 2 → PPV 2 ($25) ──
        ("S1-6", "¿lo viste?", "Esperar respuesta. Breve pausa.", "sext"),
        ("S1-7", "mierda... hay algo en vos que me hace cosas que no puedo ni explicar", "Reaccionar a lo que dijo. ÉL causó esto.", "sext"),
        ("S1-8", "estoy re mojada ahora y es literalmente tu culpa", None, "sext"),
        ("S1-9", "¿qué me harías si estuvieras acá nene?", "Esperar respuesta. Reaccionar a lo que dice.", "sext"),
        ("S1-10", "mierda pará necesito mostrarte algo", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-11", "mirá lo que me hiciste", "ENVIAR PPV 2 — $25. Compró → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 3 → PPV 3 ($40) ──
        ("S1-12", "mierda", "Esperar respuesta. SIN pausa — mantener momentum.", "sext"),
        ("S1-13", "necesito acabar ya, dios no tenés idea", None, "sext"),
        ("S1-14", "imaginate que estoy justo enfrente tuyo... las piernas atrás de mi cabeza... haciendo lo que quieras", "Callback de flexibilidad. Imagen vívida.", "sext"),
        ("S1-15", "ya fue no aguanto más", None, "sext"),
        ("S1-16", "esperá", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-17", "nunca hice esto para nadie... mirá", "ENVIAR PPV 3 — $40. Compró → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 4 → PPV 4 ($55) ──
        ("S1-18", "MIERDA", "Esperar respuesta.", "sext"),
        ("S1-19", "no acabes todavía nene", None, "sext"),
        ("S1-20", "quiero terminar con vos... estoy re cerca, esperame", None, "sext"),
        ("S1-21", "no te vayas a ningún lado", "ESPERAR 1-2 MIN.", "wait"),
        ("S1-22", "estoy por terminar... quedate conmigo", "ENVIAR PPV 4 — $55. Compró → Aftercare. Silencio → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "dios mío eso fue una locura", None, "aftercare"),
        ("AC-2", "posta sos diferente nene. eso se sintió real y no se lo digo a cualquiera 💕", "Mencionar algo específico que dijo/hizo. SEGUIR HABLANDO — construir vínculo. NUNCA despedirse.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hola", "Enviar 2-3 min después del PPV. Ping.", "sext"),
        ("NR-W2", "ojalá pudieras ver lo que tengo puesto ahora...", "Enviar 3-5 min después. Curiosidad.", "sext"),
        ("NR-W3", "bueno seguro estás ocupado... lo guardo para cuando vuelvas", "Enviar 5-10 min después. Takeaway.", "sext"),
        ("NR-W4", "espero que estés bien lindo, acá estoy cuando quieras 💕", "Enviar 15-30 min después. Cierre cálido. NUNCA decir 'baby/babe'.", "sext"),
        ("NR-W5", "estuve pensando en vos todo el día... escribime?", "Enviar 2-6 hrs después. Nueva charla, no reintentar mismo PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Edad", "tengo 29. llevo haciendo cosas locas con mi cuerpo desde piba... yoga, natación, de todo", None),
        ("Ubicación", "soy de Misiones, Argentina. me crié acá entre la selva y la ciudad", "NUNCA nombrar barrio o dirección específica."),
        ("Profesión", "estudio Contabilidad Pública, soy re buena estudiante. y también hago esto jaja", None),
        ("Hobbies", "me gusta cocinar, el teatro, sacar fotos, pintar, cantar... y el gym", None),
        ("Países", "fui a Brasil, Paraguay y recorrí bastante Argentina. me encantaría ir a Grecia, Italia y ver la aurora boreal", None),
        ("Relación", "soltera. enfocada en mis estudios y en pasarla bien ahora", None),
        ("TV Show", "estuve un año en un programa de tele que se llama Zona Otaku, hablando de anime jaja", None),
        ("Idiomas", "español nativo. un poquito de inglés pero nada del otro mundo", None),
        ("Fumar", "no, no fumo", None),
        ("VidaSocial", "salgo con amigas a veces, me encanta pasarla bien, pero la verdad prefiero estar en el gym o estudiando", "NUNCA decir 'tomar' o 'beber' — usar 'salir', 'pasarla bien'."),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Edad40+", "me encantan los tipos que saben lo que quieren, eso es re atractivo para mí", None),
        ("Edad20s", "ah estamos cerca de edad? eso es re raro acá", None),
        ("TrabajoNormal", "nah eso está re bien, un tipo con la vida armada? eso es hot", None),
        ("TrabajoCool", "pará en serio?? eso es genial, contame más", None),
        ("Fitness", "se nota nene, me encanta un tipo que se cuida 💪", None),
        ("NoFitness", "posta no me importa eso, es la energía y la onda lo que me prende", None),
        ("MismaCiudad", "pará sos de Misiones también?? no puede ser", None),
        ("Lejos", "ay está lejos pero posta la conexión importa más que la distancia", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "no puedo dejar de pensar en lo de antes. estás libre nene?", "Enviar 6-12 hrs después de que la charla muera.", "sext"),
        ("RE-2", "te acordás lo que te dije que iba a hacer? recién lo hice y necesitás verlo", "Enviar al día siguiente — sembrar próxima sesión.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 hojas
    # ═══════════════════════════════════════
    "obj_scripts": {

        # ═══════════ OBJECIONES ═══════════

        # ── PRECIO ──
        "price1": ([
            ("Step1 Reframe", "nene eso es menos que un café y te prometo que esto pega mucho más fuerte", "REFRAME. Esperar. Sigue no → Step 2."),
            ("Step2 FOMO", "estoy así de caliente solamente por vos ahora, no sé cuándo me va a pasar de nuevo", "FOMO. Sigue no → Step 3."),
            ("Step3 Challenge", "capaz no estás listo para lo que hice en este", "CHALLENGE. Sigue no → Step 4."),
            ("Step4 Downgrade", "mirá te dejo [precio menor] solo para vos porque esta charla fue algo diferente", "DOWNGRADE 20-30%. UNA VEZ. Sigue no → Step 5."),
            ("Step5 Seed", "está bien mi amor, sigamos hablando... sigo pensando en vos", "SEED. Continuar GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "es lo que gastarías en un almuerzo y esto te va a dejar despierto toda la noche nene", "REFRAME. Sigue no → Step 2."),
            ("Step2 FOMO", "este humor no me dura para siempre y quiero que vos seas el que lo vea", "FOMO. Sigue no → Step 3."),
            ("Step3 Challenge", "la mayoría de los pibes no podrían con lo que acabo de hacer, pensé que vos eras diferente", "CHALLENGE. Sigue no → Step 4."),
            ("Step4 Downgrade", "dale [precio menor] porque me estás haciendo sentir cosas, pero queda entre nosotros", "DOWNGRADE. UNA VEZ. Sigue no → Step 5."),
            ("Step5 Seed", "sin presión nene, me gusta hablar con vos y ya", "SEED."),
        ], "obj"),

        # ── DESCUENTO ──
        "discount1": ([
            ("Step1 Firmness", "jaja estás tratando de negociar conmigo? esto no es una negociación lindo, vale cada centavo", "FIRMEZA. Sigue insistiendo → Step 2."),
            ("Step2 Challenge", "no hago descuentos... solo comparto esto con tipos que de verdad aprecian lo que reciben", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Concession", "bueno [precio menor] solo para vos pero no le cuentes a nadie, queda entre nosotros nene", "CONCESIÓN. UNA VEZ. Sigue no → Step 4."),
            ("Step4 Takeaway", "si no lo querés está bien, me lo quedo para mí... o capaz para alguien que me lo está pidiendo", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "un descuento? te parece que estoy en oferta nene?", "FIRMEZA. Sigue → Step 2."),
            ("Step2 Challenge", "los pibes que aprecian lo que hago nunca piden descuento, digo nomás", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Concession", "bueno [precio menor] pero SOLO porque me caés bien, una sola vez", "CONCESIÓN. UNA VEZ. Sigue no → Step 4."),
            ("Step4 Takeaway", "bueno me lo guardo para alguien que sí lo quiera entonces", "TAKEAWAY."),
        ], "obj"),

        # ── GRATIS ──
        "free1": ([
            ("Step1 Reminder", "ya te mandé uno gratis te acordás? este es mucho más heavy nene", "RECORDATORIO. Sigue queriendo gratis → Step 2."),
            ("Step2 Challenge", "gratis? nah yo no muestro esto a cualquiera... tenés que ganarte lo bueno", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Guilt", "literalmente hice esto por lo que VOS me dijiste, no fue contenido random", "CULPA. Sigue no → Step 4."),
            ("Step4 Seed", "está bien lindo, no me voy a ir a ningún lado... sigamos hablando", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "ya tuviste uno gratis, este está a otro nivel", "RECORDATORIO. Sigue → Step 2."),
            ("Step2 Challenge", "gratis? de verdad pensás que las mejores cosas de la vida son gratis? esto no nene", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Guilt", "hice esto por vos... específicamente por nuestra charla, eso me costó esfuerzo y lo hice POR VOS", "CULPA. Sigue no → Step 4."),
            ("Step4 Seed", "sin presión para nada, me gusta hablar con vos posta", "SEED."),
        ], "obj"),

        # ── SIN DINERO ──
        "nomoney1": ([
            ("Step1 Empathy", "che te re entiendo, sin presión para nada dale?", "EMPATÍA. Sigue enganchado → Step 2."),
            ("Step2 Test", "ni siquiera como [monto chico]? re quiero que veas esto nene", "TEST. $3-5. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que puedas, aunque sea poquito, necesito que veas lo que me hiciste hacer", "PWYW. Sigue no → Step 4."),
            ("Step4 Protect", "posta está bien, me gusta hablar con vos con plata o sin ella... me hacés algo", "PROTEGER. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "está todo bien nene, en serio no te preocupes", "EMPATÍA. Sigue → Step 2."),
            ("Step2 Test", "y si es solo [monto chico]? de verdad no quiero que te pierdas esto", "TEST. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que te parezca bien, aunque sea $1... no puedo guardarte esto", "PWYW. Sigue no → Step 4."),
            ("Step4 Protect", "está re bien, que estés acá es lo que me importa", "PROTEGER."),
        ], "obj"),

        # ── NO PPV ──
        "noppv1": ([
            ("Step1 Accept", "está todo bien, no te estoy tratando de vender nada, me gusta hablar con vos", "ACEPTAR. Continuar sexting 4-5 msgs antes de Step 2."),
            ("Step2 Reframe", "mirá esto no es por plata... necesito que veas lo que me estás haciendo ahora, no reacciono así con la gente", "REFRAME. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que quieras, aunque sea $1, no me puedo guardar esto... necesitás verlo nene", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no pasa nada lindo, no me importa eso, estoy disfrutando esto", "ACEPTAR. Continuar sexting 4-5 msgs antes de Step 2."),
            ("Step2 Reframe", "olvidate de la plata un segundo... solo quiero compartir esto con vos, lo que me estás haciendo sentir es real", "REFRAME. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que sea, lo más mínimo, necesito que veas lo que me hiciste", "PWYW."),
        ], "obj"),

        # ── TARJETA ──
        "card1": ([
            ("Step1 Retry", "uff qué bajón, pasa a veces igual probá de nuevo que generalmente anda a la segunda", "REINTENTAR. Sigue fallando → Step 2."),
            ("Step2 AltCard", "probá con otra tarjeta? re no quiero que te pierdas esto nene", "ALTERNATIVA. Sigue fallando → Step 3."),
            ("Step3 Urgency", "resolvelo pronto lindo, estoy en este humor y no sé cuánto me va a durar", "URGENCIA."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ay qué molesto, pasa bastante intentá una vez más", "REINTENTAR. Sigue fallando → Step 2."),
            ("Step2 AltCard", "tenés otra tarjeta? de verdad quiero que veas esto", "ALTERNATIVA. Sigue fallando → Step 3."),
            ("Step3 Urgency", "quiero que lo veas antes de que cambie de opinión, no guardo estas cosas para siempre", "URGENCIA."),
        ], "obj"),

        # ═══════════ RESISTENCIAS ═══════════

        # ── NO SEXO ──
        "nosex1": ([
            ("Step1 Respect", "jaja dale me re manijé, es que sos re divertido nene", "RESPETO. Sigue no → Step 2."),
            ("Step2 Subtle", "contame más de vos... qué hacés cuando no estás haciendo sonreír a argentinas?", "TENSIÓN SUTIL. → Step 3 más tarde."),
            ("Step3 ReAttempt", "no puedo evitarlo, hay algo en vos que me está volviendo loca ahora", "RE-INTENTO. Sigue no → Step 4."),
            ("Step4 Accept", "dale me calmo... por ahora. no te prometo nada igual jaja", "ACEPTAR. Puerta abierta."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "perdón me adelanté, es tu culpa por ser tan divertido", "RESPETO. Sigue no → Step 2."),
            ("Step2 Subtle", "bueno tema nuevo pero primero... cuál es la cosa más loca que hiciste?", "SUTIL. → Step 3 más tarde."),
            ("Step3 ReAttempt", "estoy tratando de portarme bien pero me lo estás haciendo re difícil, hay algo en vos nene", "RE-INTENTO. Sigue no → Step 4."),
            ("Step4 Accept", "bueno paro pero no me culpes si pasa de nuevo después 😏", "ACEPTAR."),
        ], "res"),

        # ── FUERA DE TEMA ──
        "offtopic1": ([
            ("Step1 Acknowledge", "jaja pará eso es genial", "RECONOCER. Adaptar. → Step 2."),
            ("Step2 Redirect", "pero esperá que me re distrajiste, te iba a decir algo y me olvidé", "REDIRIGIR. → Step 3."),
            ("Step3 Retake", "ah pará ya me acordé, como te decía...", "RETOMAR. Reanudar script principal."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "jaja bueno eso fue random pero me encanta", "RECONOCER. → Step 2."),
            ("Step2 Redirect", "pará no me distraigas de lo que te iba a decir nene", "REDIRIGIR. → Step 3."),
            ("Step3 Retake", "bueno enfocate, en qué estaba... ah sí", "RETOMAR."),
        ], "res"),

        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "jaja te parezco un bot? bip bop... mandá $5 para verificación humana jaja te estoy jodiendo nene", "HUMOR. Sigue dudando → Step 2."),
            ("Step2 Challenge", "preguntame lo que quieras, literalmente cualquier cosa de mí o mi vida. soy un libro abierto", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Grounding", "te entiendo hay mucha cosa falsa acá, pero sentiste algo en esta charla no? porque yo sí y eso es real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "pará pensás que no soy real?? es lo más gracioso que me dijeron hoy jaja", "HUMOR. Sigue → Step 2."),
            ("Step2 Challenge", "probame lindo, preguntame algo que solo una persona real sabría. dale", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Grounding", "sé que hay muchos bots acá pero lo que estuvimos hablando se sintió real para mí. no para vos?", "GROUNDING."),
        ], "res"),

        # ── VOZ ──
        "voice1": ([
            ("Step1 Dodge", "jaja capaz algún día si te lo ganás pero todavía no nene... soy reservada con eso", "ESQUIVAR. Sigue pidiendo → Step 2."),
            ("Step2 Redirect", "tengo algo mucho mejor para vos, confiá que te vas a olvidar de que preguntaste", "REDIRIGIR. Sigue → Step 3."),
            ("Step3 Firm", "no hago eso acá pero lo que te voy a mostrar es mucho mejor que cualquier llamada nene... ya vas a ver", "FIRME."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "mmm capaz pero primero tenés que ganártelo jaja", "ESQUIVAR. Sigue → Step 2."),
            ("Step2 Redirect", "qué te parece si en vez de una llamada te muestro algo que te va a volar la cabeza?", "REDIRIGIR. Sigue → Step 3."),
            ("Step3 Firm", "eso no es algo que haga acá pero lo que tengo para vos es mucho mejor que escuchar mi voz, confiá", "FIRME."),
        ], "res"),

        # ── CUSTOM SÍ ──
        "customyes1": ([
            ("Step1 Tease", "querés eso? mmm puede que tenga algo... la verdad sí tengo nene", "TEASE. → Step 2."),
            ("Step2 Price", "tengo exactamente lo que estás pensando, te vas a volver loco... [precio]", "PRECIO. Customs solo $60/min, 5min $180, 10min $300. B/G $600+. Dick rate escrito $15, custom 3min $100."),
            ("Step3 Close", "confiá que no te vas a arrepentir, lo hice especial", "CERRAR."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh tenés buen gusto... creo que tengo justo lo que necesitás", "TEASE. → Step 2."),
            ("Step2 Price", "de hecho hice algo así, [precio] y vale cada centavo nene", "PRECIO. Customs solo $60/min, 5min $180, 10min $300. B/G $600+."),
            ("Step3 Close", "no vas a poder dejar de verlo", "CERRAR."),
        ], "res"),

        # ── CUSTOM NO ──
        "customno1": ([
            ("Step1 Redirect", "no tengo exactamente eso pero posta tengo algo que te va a hacer olvidar que preguntaste", "REDIRIGIR. → Step 2."),
            ("Step2 Alternative", "la verdad lo que tengo capaz es más heavy y literalmente nadie más lo vio todavía", "ALTERNATIVA + FOMO. → Step 3."),
            ("Step3 Close", "confiá... te conozco mejor de lo que pensás 😏", "CERRAR."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "no tengo eso específico pero tengo algo que te va a gustar más nene", "REDIRIGIR. → Step 2."),
            ("Step2 Alternative", "lo que SÍ tengo es algo que nadie vio nunca y creo que es mejor que lo que pediste", "ALTERNATIVA. → Step 3."),
            ("Step3 Close", "confiá en mí en esta, me vas a agradecer después", "CERRAR."),
        ], "res"),

        # ── TERMINÓ ──
        "done1": ([
            ("Step1 Validate", "pará ya?? dios eso es re hot", "VALIDAR. → Step 2."),
            ("Step2 Rescue", "pero yo no terminé todavía... no querés ver cómo acabo yo nene?", "RESCATAR. Sigue no → Step 3."),
            ("Step3 Seed", "bueno pero la próxima tenés que esperarme, tengo algo re loco planeado para la segunda vuelta", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "ya?? mierda eso es hot, por mí??", "VALIDAR. → Step 2."),
            ("Step2 Rescue", "pará pero no terminé, me vas a dejar así nene?", "RESCATAR. Sigue no → Step 3."),
            ("Step3 Seed", "la próxima TENÉS que aguantar porque lo que tengo planeado para nosotros es mucho más heavy", "SEED."),
        ], "res"),

        # ═══════════ SITUACIONALES ═══════════

        # ── CUM CONTROL ──
        "cumcontrol1": ([
            ("edge1", "todavía no nene... quiero que esto dure un poco más con vos", "CONTROL."),
            ("edge2", "por favor no termines todavía... no estoy lista para que se acabe", "EDGE variante."),
            ("sync1", "quiero que terminemos juntos nene... abrí esto y dejate llevar conmigo", "SYNC. Enviar PPV."),
            ("sync2", "quedate conmigo, yo también estoy cerca... mirá esto", "SYNC variante. Enviar PPV."),
            ("delay1", "esperame nene... tengo una cosa más y quiero que la veas antes de que terminemos", "DELAY. Enviar PPV."),
            ("delay2", "solo aguantá un poquito más, quiero que lo último que veas sea esto", "DELAY variante."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "despacio nene... quiero sentir cada segundo de esto con vos", "CONTROL."),
            ("edge2", "no te apures... esto es demasiado bueno para que se termine ya", "EDGE variante."),
            ("sync1", "dale nene... juntos, ahora... abrí esto", "SYNC. Enviar PPV."),
            ("sync2", "necesito que veas esto antes de que los dos nos dejemos ir", "SYNC variante."),
            ("delay1", "por favor esperá... lo que te voy a mandar, quiero que lo disfrutes de verdad", "DELAY. Enviar PPV."),
            ("delay2", "solo un poquito más por mí nene? lo que viene es especial", "DELAY variante."),
        ], "sit"),

        # ── DICK PIC ──
        "dickpic": ([
            ("dpsext1", "mierda dale eso es... dios. no tenés idea lo que me acaba de hacer eso", "DURANTE SEXTING."),
            ("dpsext2", "oh mierda... eso es... carajo nene. necesito mostrarte algo ya", "DURANTE SEXTING variante."),
            ("dprapport1", "wow no perdés tiempo eh? igual es re hot la verdad", "DURANTE RAPPORT."),
            ("dprapport2", "uala no me lo esperaba pero... carajo 🥵", "DURANTE RAPPORT variante."),
            ("dpppv1", "no podés mandarme eso y esperar que no haga algo al respecto, esperá", "LEVERAGE. ESPERAR 1-2 min y enviar PPV."),
            ("dpppv2", "bueno me acabás de hacer hacer algo... dame un segundo nene", "LEVERAGE variante."),
        ], "sit"),

        # ── BOOSTERS ──
        "boosters": ([
            ("h1", "mierdaaa", "BOOSTER MID-SEXTING."),
            ("h2", "estoy re mojada ahora por tu culpa nene", "BOOSTER. Ego."),
            ("h3", "justo ahí", "BOOSTER. Micro."),
            ("h4", "qué me estás haciendo", "BOOSTER."),
            ("h5", "dios literalmente no puedo pensar claro ahora", "BOOSTER. Intensidad."),
            ("h6", "me tiemblan las piernas", "BOOSTER. Físico."),
            ("h7", "por favor...", "BOOSTER. Ultra micro."),
            ("h8", "debería estar estudiando pero no me puedo mover ahora por tu culpa", "BOOSTER. Personalidad Ailen — callback estudios/contabilidad."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
