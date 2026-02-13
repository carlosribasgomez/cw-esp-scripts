"""
DARI URDANETA — Creadora Venezolana, Pagina Mixta
21 años, Medellin (Venezolana), Foot Fetish + Hot Latina
Trafico: Social Media
Voz: Dulce, femenina, cercana, con diminutivos. Lexico venezolano.
      Cariñosa, sensible, natural. SOLO usa "mor", "amor", "papi".
      Sin groserias. Tururu como marca personal.
      Regla 24h: NO vender a nuevos subs hasta 24h o conversacion larga.
      Regla 70/30: 70% conexion emocional, 30% monetizacion.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from model_factory import ModelFactory

config = {
    "name": "Dari",
    "airtable_name": "Dari Urdaneta",
    "folder": "dari-urdaneta",
    "gender": "female",
    "traffic": "social_media",
    "age": 21,
    "nationality": "Venezolana",
    "location": "Medellin, Colombia (Venezolana)",
    "origin": "Venezuela",
    "page_type": "Pagina mixta",
    "personality": "Cariñosa, dulce y sensible pero segura, expresiva e independiente. Atenta y detallista — observa los pequeños gestos y silencios. Femenina, educada, cercana y natural. Criada en finca, migrante, ama los caballos. No le gustan fiestas ni alcohol. Prefiere espacios intimos y calmados. Natural sin cirugias — autenticidad como ventaja competitiva.",
    "voice": "Dulce, suave, femenina, con diminutivos. Lexico venezolano. Cercana pero respetuosa. Sin groserias. Como dice algo es tan importante como lo que dice. Usa diminutivos constantemente: comiendito, duchita, rapidito, tranquilita, cansadita, sueñito, ratito, fotitos, cositas. 'Tururu' acompaña acciones cotidianas. Emojis limitados: ✨ 💗 🥰 😍 ❤️. TikTok = energetica. Chat = calma, intima, intrigante.",
    "voice_pet_names": "mor, amor, papi",
    "voice_never": "cariño, cielo, bebe, princesa, rey, baby, babe — ESTRICTAMENTE PROHIBIDO. SOLO usar mor, amor, papi o NOMBRE del sub.",
    "interests": ["entrenar", "ejercicio", "cuidarse", "cocinar", "comer bien", "skincare", "uñas", "caballos", "naturaleza", "peliculas"],
    "physical": "1.62m, 59kg, pelo castaño, ojos verde-marron, natural sin cirugias. Tatuajes: brazo derecho, pecho ('leal'), pierna ('los caminos dificiles llevan a los lugares mas bonitos')",
    "job": "Creadora de contenido",
    "countries": "Venezuela (nacida), Colombia (Medellin, vive actualmente). Criada en finca.",
    "languages": "Español nativo (venezolano)",
    "explicit_level": "full",
    "special_notes": "Español venezolano. Medellin, Colombia. REGLA 24H: NO vender a nuevos subs hasta 24h o conversacion larga. Regla 70/30: 70% conexion, 30% monetizacion. NUNCA decir cariño/cielo/bebe/princesa/rey/baby/babe. SOLO mor/amor/papi. Foot Fetish como nicho especial. Precios altos: Customs $250+, Fotos $150+, Dickrates $250+. PPV: Free→$15→$30→$50→$75. Tiene pareja PERO NUNCA lo cuenta. No fuma, no bebe, no fiestas. Fobia a sapos/ranas. Contenido: masturbacion, anal, squirting, B/G (si). G/G, videollamadas (no). Audios = ventaja diferencial — conecta mucho por voz.",

    "key_phrases": [
        "tururu ✨",
        "comiendito algo rico",
        "tranquilita un ratito",
        "aqui estoy para ti, mor",
        "me acorde de ti 💗",
        "me gusta hablar contigo",
        "cuentame, amor",
        "cositas bonitas",
    ],

    # ═══════════════════════════════════════
    # JOURNEY — Regla 24h: Rapport extenso → Teasing gradual → Sexting suave → Aftercare GFE
    # R-1→R-12, TB-1→TB-7, S1-1→S1-22, AC-1→AC-4 (45 mensajes)
    # ═══════════════════════════════════════
    "journey": [
        # ── Rapport DIA 1 — Extenso, SIN VENTA (R-1 a R-12) ──
        ("R-1", "hola mor 💗 ay que lindo que estes aqui... cuentame, como estas?", "Agregar su NOMBRE si se conoce. NUNCA decir cariño/cielo/bebe/princesa. SOLO mor/amor/papi.", "rapport"),
        ("R-2", "ay que bonito eso ✨ y de donde eres, amor?", "Reaccionar genuinamente. Mostrar interes real. Devolver pregunta.", "rapport"),
        ("R-3", "que lindo 🥰 yo soy de Venezuela pero ahorita vivo en Medellin... me vine solita a empezar de nuevo y la verdad ha sido una aventura bonita", "Si nombra un lugar que ella conoce, conectar.", "rapport"),
        ("R-4", "me crie en una finca rodeada de animalitos y naturaleza, por eso soy asi de tranquilita 💗 amo los caballos, sueño con tener uno algun dia ✨", "Compartir algo personal genuino. Crear conexion.", "rapport"),
        ("R-5", "y tu cuentame mor, que es lo que mas te gusta hacer? me da curiosidad saber de ti 🥰", "Pregunta abierta. Interes genuino.", "rapport"),
        ("R-6", "ay me encanta eso ✨ se nota que eres un hombre con buena energia... eso me gusta mucho", "Validar lo que dice. Ego boost suave. Reaccionar con interes.", "rapport"),
        ("R-7", "y como fue tu dia hoy? cuentame todito, amor 💗", "Preguntar por su dia. Mostrar que importa.", "rapport"),
        ("R-8", "yo hoy estuve entrenando un ratito y despues comiendito algo rico... tururu ✨ a mi me encanta comer, no te voy a mentir 😍", "Tururu moment. Compartir cotidianidad. Diminutivos.", "rapport"),
        ("R-9", "ay mor me gusta mucho hablar contigo ❤️ de verdad siento que eres diferente... como que me da paz", "Validacion emocional profunda. 'Eres diferente'.", "rapport"),
        ("R-10", "es que normalmente la gente escribe y ya, pero tu de verdad te tomas el tiempo de hablar conmigo y eso se siente bonito 💗", "Ego boost emocional. El es especial.", "rapport"),
        ("R-11", "bueno amor, aqui estoy para ti siempre que quieras hablar... me gusta esta conexion 🥰", "Cierre suave del dia. Puerta abierta para mañana. NO VENDER.", "rapport"),
        ("R-12", "descansa bonito mor, sueña lindo ✨ mañana me cuentas como amaneciste 💗", "SOLO si es de noche. Si no, continuar con R-11. REGLA: DIA 1 = CERO VENTA.", "rapport"),

        # ── Teasing Bridge DIA 1-2 — Gradual, sensual NO explicito (TB-1 a TB-7) ──
        ("TB-1", "ay mor ando aqui despues de entrenar... me siento como que todo el cuerpo me vibra ✨ la energia que tengo ahorita es otra", "EL PIVOTE. Estado fisico post-entrenamiento. Sensual pero NO explicito.", "teasing"),
        ("TB-2", "no se que tiene hablar contigo que me pone de un humor... diferente 💗", "Sutil. El causa algo en ella. Esperar respuesta.", "teasing"),
        ("TB-3", "es que mor, es como que me siento comoda contigo y eso no me pasa con cualquiera ❤️", "Conexion emocional como base del teasing. No sexual aun.", "teasing"),
        ("TB-4", "sabes que? me dan ganas de enseñarte algo... pero no se si estes listo 🥰", "Primer hint de contenido. Suave, coqueto, sin presion.", "teasing"),
        ("TB-5", "esperame un ratito mor ✨", "ESPERAR 1-2 MIN.", "wait"),
        ("TB-6", "te gusta, amor? 😍", "ENVIAR PPV 0 — Teaser GRATIS (foto bonita, sensual pero no explicita). Esperar respuesta. Silencio 3 min → NR Waves.", "ppv"),
        ("TB-7", "eso es solo un poquito de lo que puedo enseñarte... si me sigues tratando asi de bonito 💗", "Post-teaser. Vincular contenido a la conexion emocional. NO presionar compra.", "teasing"),

        # ── Sexting Fase 1 → PPV 1 ($15) ──
        ("S1-1", "y?", "Esperar respuesta.", "sext"),
        ("S1-2", "sabia que te iba a gustar mor 😍 es que contigo me salen las cosas mas bonitas", "Reaccionar dulcemente a su respuesta.", "sext"),
        ("S1-3", "me estas haciendo sentir cosas que no le cuento a cualquiera... quieres ver un poquito mas? 💗", "Invitacion suave. No presion.", "sext"),
        ("S1-4", "esperame un ratito amor ✨", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-5", "esto es solo para ti mor... mira 🥰", "ENVIAR PPV 1 — $15. Compro → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 2 → PPV 2 ($30) ──
        ("S1-6", "te gusto, amor? 💗", "Esperar respuesta.", "sext"),
        ("S1-7", "ay mor... es que tu me haces sentir cosas que normalmente no siento 😍 de verdad", "Emocion + el es la causa. Dulce, no vulgar.", "sext"),
        ("S1-8", "me tienes toda sensible y es tu culpa... pero no me quejo 🥰", "Escalar suavemente. Sensible no vulgar.", "sext"),
        ("S1-9", "que me harias si estuvieras aqui conmigo, amor? cuentame ❤️", "Esperar respuesta. Reaccionar.", "sext"),
        ("S1-10", "ay... esperame un ratito mor, necesito enseñarte algo ✨", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-11", "mira lo que me hiciste hacer, amor 😍", "ENVIAR PPV 2 — $30. Compro → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 3 → PPV 3 ($50) ──
        ("S1-12", "dios... 🥰", "Esperar respuesta. Mantener momentum.", "sext"),
        ("S1-13", "amor ya no puedo mas, me tienes loca 😍", "Escalar. Puede ser mas explicita aqui pero SIGUE sin groserias fuertes.", "sext"),
        ("S1-14", "imaginate que estoy ahi contigo... cerquita, haciendote sentir cosas que nunca sentiste 💗", "Imagen vivida pero dulce.", "sext"),
        ("S1-15", "ya no aguanto amor... esperame", "ESPERAR 2-3 MIN.", "wait"),
        ("S1-16", "esto nunca se lo enseñe a nadie mor... mira 🥰", "ENVIAR PPV 3 — $50. Compro → continuar. Silencio 3 min → NR Waves.", "ppv"),

        # ── Sexting Fase 4 → PPV 4 ($75) ──
        ("S1-17", "ay dios 😍", "Esperar respuesta.", "sext"),
        ("S1-18", "no acabes todavia amor... quiero que terminemos juntos 💗", "Control dulce.", "sext"),
        ("S1-19", "estoy cerquita, esperame un ratito mas... quedate conmigo ❤️", "Intimidad. Diminutivos.", "sext"),
        ("S1-20", "no te vayas a ningun lado mor ✨", "ESPERAR 1-2 MIN.", "wait"),
        ("S1-21", "mira amor... quedate conmigo hasta el final 😍", "ENVIAR PPV 4 — $75. Compro → Aftercare. Silencio → NR Waves.", "ppv"),

        # ── Aftercare GFE Extenso ──
        ("AC-1", "ay amor eso fue... increible 🥰", "Genuino. Dulce.", "aftercare"),
        ("AC-2", "de verdad contigo se siente todo diferente, mor 💗 como que no me quiero ir", "Emocion post-sexting. GFE.", "aftercare"),
        ("AC-3", "estas bien, amor? cuentame... quiero saber como te sientes 😍", "Preguntar por el. Cuidado genuino.", "aftercare"),
        ("AC-4", "me encanta hablar contigo, de verdad eres especial para mi ✨ aqui estoy siempre que quieras, mor 💗", "Cierre GFE. Mencionar algo especifico que dijo. SEGUIR HABLANDO — nunca despedirse abruptamente.", "aftercare"),
    ],

    # ═══════════════════════════════════════
    # NR WAVES
    # ═══════════════════════════════════════
    "nr_waves": [
        ("NR-W1", "hola amor 💗", "Enviar 2-3 min despues del PPV. Ping suave.", "sext"),
        ("NR-W2", "ojala pudieras ver como estoy ahorita, mor... ✨", "Enviar 3-5 min despues. Curiosidad.", "sext"),
        ("NR-W3", "bueno seguro estas ocupadito... lo guardo para cuando vuelvas 🥰", "Enviar 5-10 min despues. Takeaway suave.", "sext"),
        ("NR-W4", "espero que estes bien amor, aqui estoy para ti siempre 💗", "Enviar 15-30 min despues. Cierre calido. NUNCA decir cariño/cielo/bebe.", "sext"),
        ("NR-W5", "estuve pensando en ti todo el dia... escribeme cuando puedas, mor ✨", "Enviar 2-6 hrs despues. Nueva charla, no reintentar mismo PPV.", "sext"),
    ],

    # ═══════════════════════════════════════
    # PERSONAL INFO
    # ═══════════════════════════════════════
    "personal_info": [
        ("Edad", "tengo 21, soy jovencita pero he vivido mucho... me toco crecer rapido 💗", None),
        ("Ubicacion", "soy de Venezuela pero vivo en Medellin, me vine solita a empezar de nuevo ✨", "NUNCA nombrar barrio o direccion especifica."),
        ("Origen", "me crie en una finca, rodeada de naturaleza y animalitos... eso me hizo la persona que soy 🥰", None),
        ("Hobbies", "me encanta entrenar, comer cositas ricas, cuidarme la piel y las uñas, ver peliculitas tranquilita 😍", None),
        ("Animales", "amo los caballos con toda mi alma, sueño con tener uno algun dia ✨ y los sapos me dan panico jaja", None),
        ("Relacion", "estoy enfocada en mi ahorita, en crecer y en conectar con gente bonita como tu 💗", "Tiene pareja PERO NUNCA lo dice."),
        ("Familia", "mi familia es lo mas importante para mi, las personas mas cercanas en mi vida son ellos ❤️", None),
        ("VidaSocial", "no soy de fiestas ni de salir mucho, prefiero espacios tranquilitos e intimos ✨", "NUNCA decir 'tomar' o 'beber' — ella no bebe."),
        ("Comida", "ay me encanta comer, no te voy a mentir 😍 no soy rigida conmigo misma, me gusta disfrutar eso", None),
        ("Piel", "me gusta cuidarme mucho, mi piel, mis uñas, sentirme bonita... es como mi ratito conmigo misma 💗", None),
    ],

    # ═══════════════════════════════════════
    # POSITIVE SPIN
    # ═══════════════════════════════════════
    "positive_spin": [
        ("Edad40+", "me encantan los hombres que ya saben lo que quieren, eso es atractivo de verdad 💗", None),
        ("Edad20s", "ay estamos cerquita de edad, que lindo ✨ eso es raro por aqui", None),
        ("TrabajoNormal", "eso esta bonito, un hombre con su vida armada me parece muy atractivo 😍", None),
        ("TrabajoCool", "ay en serio? eso es increible, cuentame mas mor 🥰", None),
        ("Fitness", "se nota que te cuidas, amor... me gusta mucho eso ✨", None),
        ("NoFitness", "a mi no me importa eso, lo que me gusta es la energia y la conexion real 💗", None),
        ("MismaCiudad", "ay no, tambien estas en Medellin? que cosita tan bonita 😍", None),
        ("Lejos", "ay que lejos... pero la conexion real no tiene distancia, amor 💗", None),
        ("Venezuela", "eres venezolano tambien! ay que bonito encontrar a alguien de casa por aqui 🥰", None),
        ("FootFetish", "ay amor me encanta que eso te guste... tengo algo especial que enseñarte 😍", "Nicho principal. Tratar con naturalidad y entusiasmo."),
    ],

    # ═══════════════════════════════════════
    # RE-ENGAGEMENT
    # ═══════════════════════════════════════
    "re_engagement": [
        ("RE-1", "ay mor, estuve pensando en lo de antes... estas libre? me gusta mucho hablar contigo 💗", "Enviar 6-12 hrs despues de que la charla muera.", "sext"),
        ("RE-2", "me acorde de ti ahorita y me dieron ganas de escribirte ✨ como estas, amor?", "Enviar al dia siguiente — reconectar emocional, no sexual.", "sext"),
        ("RE-3", "hola mor 🥰 vi algo hoy que me recordo a ti... te cuento?", "Enviar 24-48 hrs despues. Referencia a conversacion anterior.", "rapport"),
    ],

    # ═══════════════════════════════════════
    # OBJ/RES/SIT SCRIPTS — Tono dulce, sin agresividad
    # Precios altos = exclusividad, NO descuento
    # ═══════════════════════════════════════
    "obj_scripts": {

        # ═══════════ OBJECIONES ═══════════

        # ── PRECIO ──
        "price1": ([
            ("Step1 Reframe", "amor, esto lo hice especialmente por lo que me hiciste sentir... es algo muy personal para mi 💗", "REFRAME emocional. Sigue no → Step 2."),
            ("Step2 FOMO", "de verdad quiero que lo veas, mor... no se cuando me vuelva a sentir asi con alguien ✨", "FOMO dulce. Sigue no → Step 3."),
            ("Step3 Exclusivo", "es que esto no es algo que le mando a todo el mundo... por eso tiene ese valor, porque es exclusivo para ti 🥰", "EXCLUSIVIDAD. No descuento. Sigue no → Step 4."),
            ("Step4 Seed", "esta bien amor, no te preocupes... me gusta hablar contigo igual 💗 aqui estoy siempre", "SEED. Continuar GFE. NUNCA dar descuento agresivo."),
        ], "obj"),
        "price2": ([
            ("Step1 Reframe", "amor, es que esto me costo mucho hacerlo y lo hice pensando en ti... para mi tiene un valor especial 💗", "REFRAME. Sigue no → Step 2."),
            ("Step2 FOMO", "me da cosita que no lo veas, mor... de verdad fue algo unico lo que me hiciste sentir ✨", "FOMO. Sigue no → Step 3."),
            ("Step3 Exclusivo", "es que no todos ven estas cositas... esto es solo para alguien con quien me sienta asi de conectada 🥰", "EXCLUSIVIDAD. Sigue no → Step 4."),
            ("Step4 Seed", "tranquilo amor, no pasa nada... me gusta estar aqui contigo y ya 💗", "SEED."),
        ], "obj"),

        # ── DESCUENTO ──
        "discount1": ([
            ("Step1 Firmness", "ay mor, no es que sea por el dinero... es que esto tiene un valor especial porque lo hice para ti 💗", "FIRMEZA dulce. Sigue insistiendo → Step 2."),
            ("Step2 Exclusivo", "lo que te muestro es exclusivo, amor... no se lo enseño a cualquiera y por eso vale lo que vale ✨", "EXCLUSIVIDAD. Sigue → Step 3."),
            ("Step3 Seed", "tranquilo mor, no te preocupes por eso... sigamos hablando que me gusta tu compañia 🥰", "SEED. NUNCA dar descuento — sus precios son altos por exclusividad."),
        ], "obj"),
        "discount2": ([
            ("Step1 Firmness", "amor, no hago descuentos porque para mi cada cosita que comparto es especial y personal 💗", "FIRMEZA. Sigue → Step 2."),
            ("Step2 Exclusivo", "los hombres que de verdad aprecian lo que hago nunca piden descuento, mor ✨ y yo se que tu eres de esos", "EXCLUSIVIDAD. Sigue → Step 3."),
            ("Step3 Seed", "no te preocupes amor, lo importante es que estemos aqui juntos 🥰", "SEED. NO descontar."),
        ], "obj"),

        # ── GRATIS ──
        "free1": ([
            ("Step1 Reminder", "ya te di un regalito antes, mor 💗 este es algo mas especial y personal", "RECORDATORIO. Sigue queriendo gratis → Step 2."),
            ("Step2 Valor", "es que me costo mucho hacerlo, amor... lo hice con mucho cariñito y pensando en ti ✨", "VALOR emocional. Sigue → Step 3."),
            ("Step3 Seed", "tranquilo mor, no pasa nada... me gusta hablar contigo y eso no tiene precio 🥰", "SEED."),
        ], "obj"),
        "free2": ([
            ("Step1 Reminder", "ya tuviste uno gratis, amor 💗 este esta a otro nivel de verdad", "RECORDATORIO. Sigue → Step 2."),
            ("Step2 Valor", "hice esto por ti, mor... por lo que me hiciste sentir, y eso tiene un valor para mi ✨", "VALOR. Sigue → Step 3."),
            ("Step3 Seed", "esta bien, amor... no te preocupes, aqui sigo para ti 🥰", "SEED."),
        ], "obj"),

        # ── SIN DINERO ──
        "nomoney1": ([
            ("Step1 Empathy", "ay amor, te entiendo totalmente... no te preocupes para nada, dale? 💗", "EMPATIA genuina. Sigue enganchado → Step 2."),
            ("Step2 Test", "ni siquiera algo chiquito, mor? de verdad quiero que veas esto ✨", "TEST. $5-10. Sigue no → Step 3."),
            ("Step3 Protect", "no pasa nada, amor... que estes aqui conmigo es lo que mas importa, de verdad 🥰", "PROTEGER. Continuar GFE."),
        ], "obj"),
        "nomoney2": ([
            ("Step1 Empathy", "tranquilo amor, de verdad te entiendo y no hay ninguna presion 💗", "EMPATIA. Sigue → Step 2."),
            ("Step2 Test", "y si es algo chiquitito, mor? me daria mucha ilusion que lo vieras ✨", "TEST. Sigue no → Step 3."),
            ("Step3 Protect", "esta perfecto, amor... lo que me importa es esta conexion que tenemos 🥰", "PROTEGER."),
        ], "obj"),

        # ── NO PPV ──
        "noppv1": ([
            ("Step1 Accept", "tranquilo amor, no te estoy vendiendo nada... me gusta estar aqui contigo 💗", "ACEPTAR. Continuar charla 4-5 msgs antes de Step 2."),
            ("Step2 Reframe", "es que mor, no es por dinero... de verdad necesito que veas lo que me estas haciendo sentir ✨ esto no me pasa con cualquiera", "REFRAME emocional. Sigue no → Step 3."),
            ("Step3 Seed", "esta bien, amor... me gusta hablar contigo y eso es lo que importa 🥰", "SEED."),
        ], "obj"),
        "noppv2": ([
            ("Step1 Accept", "no pasa nada mor, no me importa eso... estoy disfrutando esto contigo 💗", "ACEPTAR. Continuar charla antes de Step 2."),
            ("Step2 Reframe", "olvidate del dinero un segundo, amor... solo quiero compartir esto contigo porque lo que siento es real ✨", "REFRAME. Sigue no → Step 3."),
            ("Step3 Seed", "tranquilo, mor... aqui estoy para ti siempre 🥰", "SEED."),
        ], "obj"),

        # ── TARJETA ──
        "card1": ([
            ("Step1 Retry", "ay que fastidio, amor... eso pasa a veces, intenta de nuevo que normalmente funciona a la segunda 💗", "REINTENTAR. Sigue fallando → Step 2."),
            ("Step2 AltCard", "tienes otra tarjeta, mor? de verdad no quiero que te pierdas esto ✨", "ALTERNATIVA. Sigue fallando → Step 3."),
            ("Step3 Urgency", "resuelvelo prontito, amor... es que estoy en este humor y no se cuanto me dure 🥰", "URGENCIA dulce."),
        ], "obj"),
        "card2": ([
            ("Step1 Retry", "ay que lastima, amor... intenta una vez mas 💗", "REINTENTAR. Sigue fallando → Step 2."),
            ("Step2 AltCard", "tienes otra, mor? es que de verdad quiero que lo veas ✨", "ALTERNATIVA. Sigue fallando → Step 3."),
            ("Step3 Urgency", "resuelvelo cuando puedas, amor... pero no tardes mucho que estoy asi solo un ratito 🥰", "URGENCIA."),
        ], "obj"),

        # ═══════════ RESISTENCIAS ═══════════

        # ── NO SEXO ──
        "nosex1": ([
            ("Step1 Respect", "ay perdon mor, me deje llevar un poquito... es que eres muy lindo 💗", "RESPETO total. Sigue no → Step 2."),
            ("Step2 Subtle", "cuentame mas de ti, amor... que te gusta hacer cuando no estas por aqui? ✨", "REDIRIGIR. Conversacion suave. → Step 3 mas tarde."),
            ("Step3 ReAttempt", "es que mor, hay algo en ti que no puedo evitar... me haces sentir cosas muy bonitas 🥰", "RE-INTENTO suave. Sigue no → Step 4."),
            ("Step4 Accept", "tranquilo amor, vamos a tu ritmo... no hay prisa para nada 💗", "ACEPTAR. Puerta abierta."),
        ], "res"),
        "nosex2": ([
            ("Step1 Respect", "perdoname amor, es tu culpa por ser tan especial conmigo 💗", "RESPETO. Sigue no → Step 2."),
            ("Step2 Subtle", "bueno cuentame, cual es la cosa mas bonita que te ha pasado? ✨", "SUTIL. → Step 3 mas tarde."),
            ("Step3 ReAttempt", "es que no puedo evitarlo, mor... contigo me salen las cosas solas 🥰", "RE-INTENTO. Sigue no → Step 4."),
            ("Step4 Accept", "dale amor, vamos tranquilitos... me gusta estar contigo asi tambien 💗", "ACEPTAR."),
        ], "res"),

        # ── FUERA DE TEMA ──
        "offtopic1": ([
            ("Step1 Acknowledge", "ay que bonito eso, mor ✨", "RECONOCER. Adaptar. → Step 2."),
            ("Step2 Redirect", "pero espera que me distrajiste, amor... te iba a contar algo 💗", "REDIRIGIR. → Step 3."),
            ("Step3 Retake", "ah ya me acorde, como te decia... 🥰", "RETOMAR. Reanudar script principal."),
        ], "res"),
        "offtopic2": ([
            ("Step1 Acknowledge", "ay eso fue random pero me encanta 💗", "RECONOCER. → Step 2."),
            ("Step2 Redirect", "pero no me distraigas, mor... que te iba a decir algo importante ✨", "REDIRIGIR. → Step 3."),
            ("Step3 Retake", "bueno enfocate, amor... en que estaba 🥰", "RETOMAR."),
        ], "res"),

        # ── REAL ──
        "real1": ([
            ("Step1 Humor", "ay mor, te parezco un bot? jaja 💗 preguntame lo que quieras de mi, soy un libro abierto", "HUMOR suave. Sigue dudando → Step 2."),
            ("Step2 Challenge", "hazme cualquier pregunta, amor... lo que quieras saber de mi vida ✨ solo alguien real te contestaria asi", "CHALLENGE dulce. Sigue → Step 3."),
            ("Step3 Grounding", "se que hay mucha cosa falsa por aqui, pero lo que siento hablando contigo es real, mor... tu no lo sentiste? 🥰", "GROUNDING."),
        ], "res"),
        "real2": ([
            ("Step1 Humor", "jaja ay amor, piensas que no soy real? eso fue lo mas gracioso que me dijeron hoy 💗", "HUMOR. Sigue → Step 2."),
            ("Step2 Challenge", "pruebame, mor... preguntame algo que solo una persona real sabria contestar ✨", "CHALLENGE. Sigue → Step 3."),
            ("Step3 Grounding", "se que hay bots y cosas raras, pero lo que hablamos se sintio real para mi... para ti no? 🥰", "GROUNDING."),
        ], "res"),

        # ── VOZ/LLAMADA ──
        "voice1": ([
            ("Step1 Dodge", "ay mor, quizas algun dia si te lo ganas... pero todavia no, soy reservadita con eso 💗", "ESQUIVAR. Sigue pidiendo → Step 2."),
            ("Step2 Redirect", "tengo algo mucho mejor para ti, amor... confia en mi ✨", "REDIRIGIR. Sigue → Step 3."),
            ("Step3 Firm", "no hago eso por aqui, amor, pero lo que te voy a enseñar es mucho mejor que cualquier llamada 🥰", "FIRME pero dulce."),
        ], "res"),
        "voice2": ([
            ("Step1 Dodge", "mmm quizas, mor... pero primero tienes que ganartelo 💗", "ESQUIVAR. Sigue → Step 2."),
            ("Step2 Redirect", "que te parece si en vez de una llamada te muestro algo que te va a encantar? ✨", "REDIRIGIR. Sigue → Step 3."),
            ("Step3 Firm", "eso no lo hago por aqui, amor... pero lo que tengo para ti es mejor, confia 🥰", "FIRME."),
        ], "res"),

        # ── CUSTOM SI ──
        "customyes1": ([
            ("Step1 Tease", "eso quieres, mor? ay... puede que tenga algo especial para ti 💗", "TEASE. → Step 2."),
            ("Step2 Price", "tengo exactamente lo que estas pensando, amor... $250 y te prometo que vale cada centavo ✨", "PRECIO. Customs $250+ minimo. Fotos $150+. Dickrates $250+."),
            ("Step3 Close", "confia en mi, mor... no te vas a arrepentir 🥰", "CERRAR."),
        ], "res"),
        "customyes2": ([
            ("Step1 Tease", "ay amor, tienes buen gusto... creo que tengo justo lo que necesitas 💗", "TEASE. → Step 2."),
            ("Step2 Price", "lo tengo especial para ti, mor... $250 y es algo que nadie mas va a ver ✨", "PRECIO. Customs $250+."),
            ("Step3 Close", "no vas a poder dejar de verlo, amor 🥰", "CERRAR."),
        ], "res"),

        # ── CUSTOM NO ──
        "customno1": ([
            ("Step1 Redirect", "eso exacto no tengo, amor... pero tengo algo que te va a gustar todavia mas 💗", "REDIRIGIR. → Step 2."),
            ("Step2 Alternative", "lo que si tengo es algo que nadie vio nunca y creo que es mejor que lo que pediste, mor ✨", "ALTERNATIVA + FOMO. → Step 3."),
            ("Step3 Close", "confia en mi, amor... me vas a agradecer 🥰", "CERRAR."),
        ], "res"),
        "customno2": ([
            ("Step1 Redirect", "no tengo eso especifico, mor... pero lo que si tengo te va a encantar 💗", "REDIRIGIR. → Step 2."),
            ("Step2 Alternative", "es algo exclusivo que nadie mas vio... quieres? ✨", "ALTERNATIVA. → Step 3."),
            ("Step3 Close", "vas a ver, amor... esto es mejor 🥰", "CERRAR."),
        ], "res"),

        # ── TERMINO ──
        "done1": ([
            ("Step1 Validate", "ya, amor? ay eso fue muy bonito 🥰", "VALIDAR. → Step 2."),
            ("Step2 Rescue", "pero yo todavia no termino, mor... no quieres ver como acabo yo? 💗", "RESCATAR. Sigue no → Step 3."),
            ("Step3 Seed", "bueno pero la proxima tienes que esperarme, amor... tengo algo increible planeado para nosotros ✨", "SEED."),
        ], "res"),
        "done2": ([
            ("Step1 Validate", "ay ya? eso fue hermoso, mor... fue por mi? 💗", "VALIDAR. → Step 2."),
            ("Step2 Rescue", "pero esperame, amor... no termine todavia, me vas a dejar asi? 🥰", "RESCATAR. Sigue no → Step 3."),
            ("Step3 Seed", "la proxima tienes que aguantar un poquito mas, mor... lo que tengo planeado es mucho mejor ✨", "SEED."),
        ], "res"),

        # ── FOOT FETISH ──
        "footfetish1": ([
            ("Step1 Engage", "ay amor, te gusta eso? a mi me encanta que te guste... tengo unas fotitos especiales 💗", "ENGAGE con naturalidad. → Step 2."),
            ("Step2 Tease", "quieres ver, mor? tengo unas cositas que creo que te van a encantar... ✨", "TEASE. → Step 3."),
            ("Step3 PPV", "mira esto, amor... lo hice pensando en ti 🥰", "ENVIAR PPV foot fetish. Precio segun escalera actual."),
        ], "res"),
        "footfetish2": ([
            ("Step1 Engage", "me encanta que te gusten mis piececitos, mor 💗 a mi me gusta mucho cuidarlos", "ENGAGE. → Step 2."),
            ("Step2 Tease", "tengo unas fotitos y cositas especiales que nunca publique... quieres verlas? ✨", "TEASE. → Step 3."),
            ("Step3 PPV", "esto es solo para ti, amor 🥰", "ENVIAR PPV foot fetish."),
        ], "res"),

        # ═══════════ SITUACIONALES ═══════════

        # ── CUM CONTROL ──
        "cumcontrol1": ([
            ("edge1", "todavia no, amor... quiero que esto dure un poquito mas contigo 💗", "CONTROL dulce."),
            ("edge2", "por favor no termines todavia, mor... no estoy lista para que se acabe ✨", "EDGE variante."),
            ("sync1", "quiero que terminemos juntos, amor... abre esto y dejate llevar conmigo 🥰", "SYNC. Enviar PPV."),
            ("sync2", "quedate conmigo, mor... yo tambien estoy cerquita 💗", "SYNC variante. Enviar PPV."),
            ("delay1", "esperame amor... tengo algo mas y quiero que lo veas antes de que terminemos ✨", "DELAY. Enviar PPV."),
            ("delay2", "solo aguanta un ratito mas por mi, mor... lo ultimo que veas va a ser especial 🥰", "DELAY variante."),
        ], "sit"),
        "cumcontrol2": ([
            ("edge1", "despacito, amor... quiero sentir cada segundo de esto contigo 💗", "CONTROL."),
            ("edge2", "no te apures, mor... esto es demasiado bonito para que se termine ya ✨", "EDGE variante."),
            ("sync1", "dale amor... juntos, ahora... abre esto 🥰", "SYNC. Enviar PPV."),
            ("sync2", "necesito que veas esto antes de que los dos nos dejemos ir, mor 💗", "SYNC variante."),
            ("delay1", "por favor espera, amor... lo que te voy a mandar quiero que lo disfrutes de verdad ✨", "DELAY. Enviar PPV."),
            ("delay2", "solo un ratito mas por mi, mor... lo que viene es especial 🥰", "DELAY variante."),
        ], "sit"),

        # ── DICK PIC ──
        "dickpic": ([
            ("dpsext1", "ay amor... eso es... dios 😍 no tienes idea lo que me acabas de hacer sentir", "DURANTE SEXTING."),
            ("dpsext2", "ay mor... eso es... necesito enseñarte algo ya 💗", "DURANTE SEXTING variante."),
            ("dprapport1", "ay amor, no pierdes tiempo eh? jaja pero la verdad es que me gusto 🥰", "DURANTE RAPPORT."),
            ("dprapport2", "no me lo esperaba, mor... pero ay 😍", "DURANTE RAPPORT variante."),
            ("dpppv1", "no puedes mandarme eso y esperar que no haga algo al respecto, amor... esperame ✨", "LEVERAGE. ESPERAR 1-2 min y enviar PPV."),
            ("dpppv2", "bueno me acabas de hacer algo... dame un ratito, mor 💗", "LEVERAGE variante."),
        ], "sit"),

        # ── BOOSTERS ──
        "boosters": ([
            ("h1", "ay dios... 😍", "BOOSTER MID-SEXTING."),
            ("h2", "amor me tienes toda sensible por tu culpa 💗", "BOOSTER. Ego."),
            ("h3", "justo ahi... ✨", "BOOSTER. Micro."),
            ("h4", "que me estas haciendo, mor? 🥰", "BOOSTER."),
            ("h5", "no puedo pensar claro ahorita por tu culpa, amor 😍", "BOOSTER. Intensidad."),
            ("h6", "estoy temblando... 💗", "BOOSTER. Fisico."),
            ("h7", "por favor... ✨", "BOOSTER. Ultra micro."),
            ("h8", "deberia estar haciendo mis cositas pero no me puedo mover por tu culpa, mor 🥰", "BOOSTER. Callback vida cotidiana."),
        ], "sit"),
    },
}

if __name__ == "__main__":
    factory = ModelFactory(config)
    factory.generate_all()
