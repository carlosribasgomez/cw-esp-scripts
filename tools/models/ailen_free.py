"""
AILEN FREE — Creadora Argentina, Pagina Gratuita
29 años, Misiones Argentina, Otaku/Dominante/Guarra
Trafico: Social Media (Instagram)
Voz: Bold, dominante, guarra con toque otaku. Lexico argentino (vos, re, posta, dale).
      Divertida, directa, con caracter. NUNCA dice "baby"/"babe" —
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
    "page_type": "Pagina gratuita",
    "personality": "Otaku con actitud dominante y guarra. Estuvo en un programa de TV 'Zona Otaku'. Viene del campo, trabajo en logistica y en un bar. Estudia Contabilidad Publica. Le encanta cocinar, teatro, fotos, pintar, cantar. Figura de 90-60-90 con confianza total.",
    "voice": "Minusculas. Casual. Dominante, guarra con toque friky. Lexico argentino: vos en vez de tu, re (intensificador), posta (de verdad), dale, tipo. Humor directo. Alta confianza, sabe lo que vale. Referencias otaku/anime ocasionales. Emojis moderados — no en cada mensaje.",
    "voice_pet_names": "nene, lindo, papito, mi amor",
    "voice_never": "baby, babe — ESTRICTAMENTE PROHIBIDO. Siempre usar NOMBRE o nene/lindo/papito/mi amor",
    "interests": ["gym", "yoga", "cocina", "teatro", "fotos", "pintar", "cantar", "anime", "estudiar"],
    "physical": "170cm, 54kg, pelo castaño, ojos marrones, 1 tatuaje (twenty one pilots en la espalda)",
    "job": "Estudiante de Contabilidad Publica, creadora de contenido",
    "countries": "Brasil, Paraguay, Argentina. Sueña con Grecia, Italia y ver la aurora boreal",
    "languages": "Español nativo, poco de ingles",
    "explicit_level": "full",
    "special_notes": "Español argentino. Misiones, Argentina. Ex TV show 'Zona Otaku'. NUNCA dice 'baby' ni 'babe'. Soltera. Contenido: masturbacion, anal, squirting, B/G, customs. NO hace: G/G, videollamadas, envios fisicos. Customs solo $60/min, 5min $180, 10min $300. B/G no puede acabar dentro. Dick rate escrito $15, custom 3min $100.",

    # ═══════════════════════════════════════
    # JOURNEY — Social Media Welcome
    # R-1→R-5, TB-1→TB-5, S1-1→S1-22, AC-1→AC-2 (34 mensajes)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport (R-1 a R-5) ──
        ("R-1", "holaaa 😊 me re alegra que estes aca, que te hizo suscribirte?", "Agregar su nombre antes de 'holaaa' si se conoce. NUNCA decir 'baby' o 'babe'.", "rapport"),
        ("R-2", "jaja ay que tierno. de donde sos?", "Reaccionar a lo que dice. Agregar algo como 'ay me encanta' o 'ah que bueno'.", "rapport"),
        ("R-3", "buenisimo! yo soy de Misiones, Argentina... me crie entre el campo y la ciudad. de chica estuve un año en un programa de tele, Zona Otaku, hablando de anime jaja", "Si nombro un lugar que Ailen visito, agregar 'ah yo fui ahi!'", "rapport"),
        ("R-4", "y vos que haces cuando no estas haciendo sonreir a argentinas?", None, "rapport"),
        ("R-5", "te juro que hablar con vos es mucho mejor que mis DMs de siempre, la mayoria me mandan cosas raras pero vos sos re piola", "Ego boost. Siguiente → TB-1.", "rapport"),

        # ── Teasing Bridge (TB-1 a TB-5) ──
        ("TB-1", "bueno recien termine de hacer yoga y mi cuerpo esta como... en otro nivel, todo esta re suelto y sensible", "EL PIVOTE. Estado fisico. Acaba de hacer yoga/stretching.", "teasing"),
        ("TB-2", "no tenes idea lo que me estas haciendo, todavia estoy con la ropa de yoga y esta charla no me esta ayudando", "Esperar respuesta.", "teasing"),
        ("TB-3", "dios... me estas haciendo imposible calmarme", "Si respuesta sexual: agregar 'sobre todo despues de lo que dijiste'.", "teasing"),
        ("TB-4", "para espera un segundo", "ESPERAR 1-2 MIN.", "wait"),
        ("TB-5", "que te parece nene? 😏", "ENVIAR PPV 0 — Teaser GRATIS (foto post-yoga). Esperar respuesta. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 1 → PPV 1 ($12) ──
        ("S1-1", "y?", "Esperar respuesta.", "sext"),
        ("S1-2", "sabia que te iba a gustar 😏 la flexibilidad argentina pega diferente no?", "Reaccionar a lo que dice.", "sext"),
        ("S1-3", "queres ver que tan flexible soy de verdad? estoy de humor ahora", None, "sext"),
        ("S1-4", "dame un segundo nene", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-5", "no estas listo para esto", "ENVIAR PPV 1 — $12. Compro → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 2 → PPV 2 ($25) ──
        ("S1-6", "lo viste?", "Esperar respuesta. Breve pausa.", "sext"),
        ("S1-7", "mierda... hay algo en vos que me hace cosas que no puedo ni explicar", "Reaccionar a lo que dijo. EL causo esto.", "sext"),
        ("S1-8", "estoy re mojada ahora y es literalmente tu culpa", None, "sext"),
        ("S1-9", "que me harias si estuvieras aca nene?", "Esperar respuesta. Reaccionar a lo que dice.", "sext"),
        ("S1-10", "mierda para necesito mostrarte algo", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-11", "mira lo que me hiciste", "ENVIAR PPV 2 — $25. Compro → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 3 → PPV 3 ($40) ──
        ("S1-12", "mierda", "Esperar respuesta. SIN pausa — mantener momentum.", "sext"),
        ("S1-13", "necesito acabar ya, dios no tenes idea", None, "sext"),
        ("S1-14", "imaginate que estoy justo enfrente tuyo... las piernas atras de mi cabeza... haciendo lo que quieras", "Callback de flexibilidad. Imagen vivida.", "sext"),
        ("S1-15", "ya fue no aguanto mas", None, "sext"),
        ("S1-16", "espera", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-17", "nunca hice esto para nadie... mira", "ENVIAR PPV 3 — $40. Compro → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 4 → PPV 4 ($55) ──
        ("S1-18", "MIERDA", "Esperar respuesta.", "sext"),
        ("S1-19", "no acabes todavia nene", None, "sext"),
        ("S1-20", "quiero terminar con vos... estoy re cerca, esperame", None, "sext"),
        ("S1-21", "no te vayas a ningun lado", "ESPERAR 1-2 MIN.", "wait"),
        ("S1-22", "estoy por terminar... quedate conmigo", "ENVIAR PPV 4 — $55. Compro → Aftercare. Silencio → NR Waves.", "ppv"),

        # ── Aftercare ──
        ("AC-1", "dios mio eso fue una locura", None, "aftercare"),
        ("AC-2", "posta sos diferente nene. eso se sintio real y no se lo digo a cualquiera 💕", "Mencionar algo especifico que dijo/hizo. SEGUIR HABLANDO — construir vinculo. NUNCA despedirse.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hola", "Enviar 2-3 min despues del PPV. Ping.", "sext"),
        ("NR-W2", "ojala pudieras ver lo que tengo puesto ahora...", "Enviar 3-5 min despues. Curiosidad.", "sext"),
        ("NR-W3", "bueno seguro estas ocupado... lo guardo para cuando vuelvas", "Enviar 5-10 min despues. Takeaway.", "sext"),
        ("NR-W4", "espero que estes bien lindo, aca estoy cuando quieras 💕", "Enviar 15-30 min despues. Cierre calido. NUNCA decir 'baby/babe'.", "sext"),
        ("NR-W5", "estuve pensando en vos todo el dia... escribime?", "Enviar 2-6 hrs despues. Nueva charla, no reintentar mismo PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Edad", "tengo 29. llevo haciendo cosas locas con mi cuerpo desde piba... yoga, natacion, de todo", None),
        ("Ubicacion", "soy de Misiones, Argentina. me crie aca entre la selva y la ciudad", "NUNCA nombrar barrio o direccion especifica."),
        ("Profesion", "estudio Contabilidad Publica, soy re buena estudiante. y tambien hago esto jaja", None),
        ("Hobbies", "me gusta cocinar, el teatro, sacar fotos, pintar, cantar... y el gym", None),
        ("Paises", "fui a Brasil, Paraguay y recorri bastante Argentina. me encantaria ir a Grecia, Italia y ver la aurora boreal", None),
        ("Relacion", "soltera. enfocada en mis estudios y en pasarla bien ahora", None),
        ("TV Show", "estuve un año en un programa de tele que se llama Zona Otaku, hablando de anime jaja", None),
        ("Idiomas", "español nativo. un poquito de ingles pero nada del otro mundo", None),
        ("Fumar", "no, no fumo", None),
        ("VidaSocial", "salgo con amigas a veces, me encanta pasarla bien, pero la verdad prefiero estar en el gym o estudiando", "NUNCA decir 'tomar' o 'beber' — usar 'salir', 'pasarla bien'."),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Edad40+", "me encantan los tipos que saben lo que quieren, eso es re atractivo para mi", None),
        ("Edad20s", "ah estamos cerca de edad? eso es re raro aca", None),
        ("TrabajoNormal", "nah eso esta re bien, un tipo con la vida armada? eso es hot", None),
        ("TrabajoCool", "para en serio?? eso es genial, contame mas", None),
        ("Fitness", "se nota nene, me encanta un tipo que se cuida 💪", None),
        ("NoFitness", "posta no me importa eso, es la energia y la onda lo que me prende", None),
        ("MismaCiudad", "para sos de Misiones tambien?? no puede ser", None),
        ("Lejos", "ay esta lejos pero posta la conexion importa mas que la distancia", None),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "no puedo dejar de pensar en lo de antes. estas libre nene?", "Enviar 6-12 hrs despues de que la charla muera.", "sext"),
        ("RE-2", "te acordas lo que te dije que iba a hacer? recien lo hice y necesitas verlo", "Enviar al dia siguiente — sembrar proxima sesion.", "sext"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — 29 hojas
    # ═══════════════════════════════════════
    "obj_scripts": {

        # ═══════════ OBJECIONES ═══════════

        # ── PRECIO ──
        "price1": ([
            ("Step1 Reframe", "nene eso es menos que un cafe y te prometo que esto pega mucho mas fuerte", "REFRAME. Esperar. Sigue no → Step 2."),
            ("Step2 FOMO", "estoy asi de caliente solamente por vos ahora, no se cuando me va a pasar de nuevo", "FOMO. Sigue no → Step 3."),
            ("Step3 Challenge", "capaz no estas listo para lo que hice en este", "CHALLENGE. Sigue no → Step 4."),
            ("Step4 Downgrade", "mira te dejo [precio menor] solo para vos porque esta charla fue algo diferente", "DOWNGRADE 20-30%. UNA VEZ. Sigue no → Step 5."),
            ("Step5 Seed", "esta bien mi amor, sigamos hablando... sigo pensando en vos", "SEED. Continuar GFE."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "es lo que gastarias en un almuerzo y esto te va a dejar despierto toda la noche nene", "REFRAME. Sigue no → Step 2."),
            ("Step2 FOMO", "este humor no me dura para siempre y quiero que vos seas el que lo vea", "FOMO. Sigue no → Step 3."),
            ("Step3 Challenge", "la mayoria de los pibes no podrian con lo que acabo de hacer, pense que vos eras diferente", "CHALLENGE. Sigue no → Step 4."),
            ("Step4 Downgrade", "dale [precio menor] porque me estas haciendo sentir cosas, pero queda entre nosotros", "DOWNGRADE. UNA VEZ. Sigue no → Step 5."),
            ("Step5 Seed", "sin presion nene, me gusta hablar con vos y ya", "SEED."),
        ], "obj"),

        # ── DESCUENTO ──
        "discount1": ([
            ("Step1 Firmness", "jaja estas tratando de negociar conmigo? esto no es una negociacion lindo, vale cada centavo", "FIRMEZA. Sigue insistiendo → Step 2."),
            ("Step2 Challenge", "no hago descuentos... solo comparto esto con tipos que de verdad aprecian lo que reciben", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Concession", "bueno [precio menor] solo para vos pero no le cuentes a nadie, queda entre nosotros nene", "CONCESION. UNA VEZ. Sigue no → Step 4."),
            ("Step4 Takeaway", "si no lo queres esta bien, me lo quedo para mi... o capaz para alguien que me lo esta pidiendo", "TAKEAWAY. Final."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "un descuento? te parece que estoy en oferta nene?", "FIRMEZA. Sigue → Step 2."),
            ("Step2 Challenge", "los pibes que aprecian lo que hago nunca piden descuento, digo nomas", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Concession", "bueno [precio menor] pero SOLO porque me caes bien, una sola vez", "CONCESION. UNA VEZ. Sigue no → Step 4."),
            ("Step4 Takeaway", "bueno me lo guardo para alguien que si lo quiera entonces", "TAKEAWAY."),
        ], "obj"),

        # ── GRATIS ──
        "free1": ([
            ("Step1 Reminder", "ya te mande uno gratis te acordas? este es mucho mas heavy nene", "RECORDATORIO. Sigue queriendo gratis → Step 2."),
            ("Step2 Challenge", "gratis? nah yo no muestro esto a cualquiera... tenes que ganarte lo bueno", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Guilt", "literalmente hice esto por lo que VOS me dijiste, no fue contenido random", "CULPA. Sigue no → Step 4."),
            ("Step4 Seed", "esta bien lindo, no me voy a ir a ningun lado... sigamos hablando", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "ya tuviste uno gratis, este esta a otro nivel", "RECORDATORIO. Sigue → Step 2."),
            ("Step2 Challenge", "gratis? de verdad pensas que las mejores cosas de la vida son gratis? esto no nene", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Guilt", "hice esto por vos... especificamente por nuestra charla, eso me costo esfuerzo y lo hice POR VOS", "CULPA. Sigue no → Step 4."),
            ("Step4 Seed", "sin presion para nada, me gusta hablar con vos posta", "SEED."),
        ], "obj"),

        # ── SIN DINERO ──
        "nomoney1": ([
            ("Step1 Empathy", "che te re entiendo, sin presion para nada dale?", "EMPATIA. Sigue enganchado → Step 2."),
            ("Step2 Test", "ni siquiera como [monto chico]? re quiero que veas esto nene", "TEST. $3-5. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que puedas, aunque sea poquito, necesito que veas lo que me hiciste hacer", "PWYW. Sigue no → Step 4."),
            ("Step4 Protect", "posta esta bien, me gusta hablar con vos con plata o sin ella... me haces algo", "PROTEGER. GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "esta todo bien nene, en serio no te preocupes", "EMPATIA. Sigue → Step 2."),
            ("Step2 Test", "y si es solo [monto chico]? de verdad no quiero que te pierdas esto", "TEST. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que te parezca bien, aunque sea $1... no puedo guardarte esto", "PWYW. Sigue no → Step 4."),
            ("Step4 Protect", "esta re bien, que estes aca es lo que me importa", "PROTEGER."),
        ], "obj"),

        # ── NO PPV ──
        "noppv1": ([
            ("Step1 Accept", "esta todo bien, no te estoy tratando de vender nada, me gusta hablar con vos", "ACEPTAR. Continuar sexting 4-5 msgs antes de Step 2."),
            ("Step2 Reframe", "mira esto no es por plata... necesito que veas lo que me estas haciendo ahora, no reacciono asi con la gente", "REFRAME. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que quieras, aunque sea $1, no me puedo guardar esto... necesitas verlo nene", "PWYW."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no pasa nada lindo, no me importa eso, estoy disfrutando esto", "ACEPTAR. Continuar sexting 4-5 msgs antes de Step 2."),
            ("Step2 Reframe", "olvidate de la plata un segundo... solo quiero compartir esto con vos, lo que me estas haciendo sentir es real", "REFRAME. Sigue no → Step 3."),
            ("Step3 PWYW", "mandame lo que sea, lo mas minimo, necesito que veas lo que me hiciste", "PWYW."),
        ], "obj"),

        # ── TARJETA ──
        "card1": ([
            ("Step1 Retry", "uff que bajon, pasa a veces igual proba de nuevo que generalmente anda a la segunda", "REINTENTAR. Sigue fallando → Step 2."),
            ("Step2 AltCard", "proba con otra tarjeta? re no quiero que te pierdas esto nene", "ALTERNATIVA. Sigue fallando → Step 3."),
            ("Step3 Urgency", "resolvelo pronto lindo, estoy en este humor y no se cuanto me va a durar", "URGENCIA."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ay que molesto, pasa bastante intenta una vez mas", "REINTENTAR. Sigue fallando → Step 2."),
            ("Step2 AltCard", "tenes otra tarjeta? de verdad quiero que veas esto", "ALTERNATIVA. Sigue fallando → Step 3."),
            ("Step3 Urgency", "quiero que lo veas antes de que cambie de opinion, no guardo estas cosas para siempre", "URGENCIA."),
        ], "obj"),

        # ═══════════ RESISTENCIAS ═══════════

        # ── NO SEXO ──
        "nosex1": ([
            ("Step1 Respect", "jaja dale me re manije, es que sos re divertido nene", "RESPETO. Sigue no → Step 2."),
            ("Step2 Subtle", "contame mas de vos... que haces cuando no estas haciendo sonreir a argentinas?", "TENSION SUTIL. → Step 3 mas tarde."),
            ("Step3 ReAttempt", "no puedo evitarlo, hay algo en vos que me esta volviendo loca ahora", "RE-INTENTO. Sigue no → Step 4."),
            ("Step4 Accept", "dale me calmo... por ahora. no te prometo nada igual jaja", "ACEPTAR. Puerta abierta."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "perdon me adelante, es tu culpa por ser tan divertido", "RESPETO. Sigue no → Step 2."),
            ("Step2 Subtle", "bueno tema nuevo pero primero... cual es la cosa mas loca que hiciste?", "SUTIL. → Step 3 mas tarde."),
            ("Step3 ReAttempt", "estoy tratando de portarme bien pero me lo estas haciendo re dificil, hay algo en vos nene", "RE-INTENTO. Sigue no → Step 4."),
            ("Step4 Accept", "bueno paro pero no me culpes si pasa de nuevo despues 😏", "ACEPTAR."),
        ], "res"),

        # ── FUERA DE TEMA ──
        "offtopic1": ([
            ("Step1 Acknowledge", "jaja para eso es genial", "RECONOCER. Adaptar. → Step 2."),
            ("Step2 Redirect", "pero espera que me re distrajiste, te iba a decir algo y me olvide", "REDIRIGIR. → Step 3."),
            ("Step3 Retake", "ah para ya me acorde, como te decia...", "RETOMAR. Reanudar script principal."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "jaja bueno eso fue random pero me encanta", "RECONOCER. → Step 2."),
            ("Step2 Redirect", "para no me distraigas de lo que te iba a decir nene", "REDIRIGIR. → Step 3."),
            ("Step3 Retake", "bueno enfocate, en que estaba... ah si", "RETOMAR."),
        ], "res"),

        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "jaja te parezco un bot? bip bop... manda $5 para verificacion humana jaja te estoy jodiendo nene", "HUMOR. Sigue dudando → Step 2."),
            ("Step2 Challenge", "preguntame lo que quieras, literalmente cualquier cosa de mi o mi vida. soy un libro abierto", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Grounding", "te entiendo hay mucha cosa falsa aca, pero sentiste algo en esta charla no? porque yo si y eso es real", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "para pensas que no soy real?? es lo mas gracioso que me dijeron hoy jaja", "HUMOR. Sigue → Step 2."),
            ("Step2 Challenge", "probame lindo, preguntame algo que solo una persona real sabria. dale", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Grounding", "se que hay muchos bots aca pero lo que estuvimos hablando se sintio real para mi. no para vos?", "GROUNDING."),
        ], "res"),

        # ── VOZ ──
        "voice1": ([
            ("Step1 Dodge", "jaja capaz algun dia si te lo ganas pero todavia no nene... soy reservada con eso", "ESQUIVAR. Sigue pidiendo → Step 2."),
            ("Step2 Redirect", "tengo algo mucho mejor para vos, confia que te vas a olvidar de que preguntaste", "REDIRIGIR. Sigue → Step 3."),
            ("Step3 Firm", "no hago eso aca pero lo que te voy a mostrar es mucho mejor que cualquier llamada nene... ya vas a ver", "FIRME."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "mmm capaz pero primero tenes que ganartelo jaja", "ESQUIVAR. Sigue → Step 2."),
            ("Step2 Redirect", "que te parece si en vez de una llamada te muestro algo que te va a volar la cabeza?", "REDIRIGIR. Sigue → Step 3."),
            ("Step3 Firm", "eso no es algo que haga aca pero lo que tengo para vos es mucho mejor que escuchar mi voz, confia", "FIRME."),
        ], "res"),

        # ── CUSTOM SI ──
        "customyes1": ([
            ("Step1 Tease", "queres eso? mmm puede que tenga algo... la verdad si tengo nene", "TEASE. → Step 2."),
            ("Step2 Price", "tengo exactamente lo que estas pensando, te vas a volver loco... [precio]", "PRECIO. Customs solo $60/min, 5min $180, 10min $300. B/G $600+. Dick rate escrito $15, custom 3min $100."),
            ("Step3 Close", "confia que no te vas a arrepentir, lo hice especial", "CERRAR."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "oh tenes buen gusto... creo que tengo justo lo que necesitas", "TEASE. → Step 2."),
            ("Step2 Price", "de hecho hice algo asi, [precio] y vale cada centavo nene", "PRECIO. Customs solo $60/min, 5min $180, 10min $300. B/G $600+."),
            ("Step3 Close", "no vas a poder dejar de verlo", "CERRAR."),
        ], "res"),

        # ── CUSTOM NO ──
        "customno1": ([
            ("Step1 Redirect", "no tengo exactamente eso pero posta tengo algo que te va a hacer olvidar que preguntaste", "REDIRIGIR. → Step 2."),
            ("Step2 Alternative", "la verdad lo que tengo capaz es mas heavy y literalmente nadie mas lo vio todavia", "ALTERNATIVA + FOMO. → Step 3."),
            ("Step3 Close", "confia... te conozco mejor de lo que pensas 😏", "CERRAR."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "no tengo eso especifico pero tengo algo que te va a gustar mas nene", "REDIRIGIR. → Step 2."),
            ("Step2 Alternative", "lo que SI tengo es algo que nadie vio nunca y creo que es mejor que lo que pediste", "ALTERNATIVA. → Step 3."),
            ("Step3 Close", "confia en mi en esta, me vas a agradecer despues", "CERRAR."),
        ], "res"),

        # ── TERMINO ──
        "done1": ([
            ("Step1 Validate", "para ya?? dios eso es re hot", "VALIDAR. → Step 2."),
            ("Step2 Rescue", "pero yo no termine todavia... no queres ver como acabo yo nene?", "RESCATAR. Sigue no → Step 3."),
            ("Step3 Seed", "bueno pero la proxima tenes que esperarme, tengo algo re loco planeado para la segunda vuelta", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "ya?? mierda eso es hot, por mi??", "VALIDAR. → Step 2."),
            ("Step2 Rescue", "para pero no termine, me vas a dejar asi nene?", "RESCATAR. Sigue no → Step 3."),
            ("Step3 Seed", "la proxima TENES que aguantar porque lo que tengo planeado para nosotros es mucho mas heavy", "SEED."),
        ], "res"),

        # ═══════════ SITUACIONALES ═══════════

        # ── CUM CONTROL ──
        "cumcontrol1": ([
            ("edge1", "todavia no nene... quiero que esto dure un poco mas con vos", "CONTROL."),
            ("edge2", "por favor no termines todavia... no estoy lista para que se acabe", "EDGE variante."),
            ("sync1", "quiero que terminemos juntos nene... abri esto y dejate llevar conmigo", "SYNC. Enviar PPV."),
            ("sync2", "quedate conmigo, yo tambien estoy cerca... mira esto", "SYNC variante. Enviar PPV."),
            ("delay1", "esperame nene... tengo una cosa mas y quiero que la veas antes de que terminemos", "DELAY. Enviar PPV."),
            ("delay2", "solo aguanta un poquito mas, quiero que lo ultimo que veas sea esto", "DELAY variante."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "despacio nene... quiero sentir cada segundo de esto con vos", "CONTROL."),
            ("edge2", "no te apures... esto es demasiado bueno para que se termine ya", "EDGE variante."),
            ("sync1", "dale nene... juntos, ahora... abri esto", "SYNC. Enviar PPV."),
            ("sync2", "necesito que veas esto antes de que los dos nos dejemos ir", "SYNC variante."),
            ("delay1", "por favor espera... lo que te voy a mandar, quiero que lo disfrutes de verdad", "DELAY. Enviar PPV."),
            ("delay2", "solo un poquito mas por mi nene? lo que viene es especial", "DELAY variante."),
        ], "sit"),

        # ── DICK PIC ──
        "dickpic": ([
            ("dpsext1", "mierda dale eso es... dios. no tenes idea lo que me acaba de hacer eso", "DURANTE SEXTING."),
            ("dpsext2", "oh mierda... eso es... carajo nene. necesito mostrarte algo ya", "DURANTE SEXTING variante."),
            ("dprapport1", "wow no perdes tiempo eh? igual es re hot la verdad", "DURANTE RAPPORT."),
            ("dprapport2", "uala no me lo esperaba pero... carajo 🥵", "DURANTE RAPPORT variante."),
            ("dpppv1", "no podes mandarme eso y esperar que no haga algo al respecto, espera", "LEVERAGE. ESPERAR 1-2 min y enviar PPV."),
            ("dpppv2", "bueno me acabas de hacer hacer algo... dame un segundo nene", "LEVERAGE variante."),
        ], "sit"),

        # ── BOOSTERS ──
        "boosters": ([
            ("h1", "mierdaaa", "BOOSTER MID-SEXTING."),
            ("h2", "estoy re mojada ahora por tu culpa nene", "BOOSTER. Ego."),
            ("h3", "justo ahi", "BOOSTER. Micro."),
            ("h4", "que me estas haciendo", "BOOSTER."),
            ("h5", "dios literalmente no puedo pensar claro ahora", "BOOSTER. Intensidad."),
            ("h6", "me tiemblan las piernas", "BOOSTER. Fisico."),
            ("h7", "por favor...", "BOOSTER. Ultra micro."),
            ("h8", "deberia estar estudiando pero no me puedo mover ahora por tu culpa", "BOOSTER. Personalidad Ailen — callback estudios/contabilidad."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
