"""
Genera PDF profesional para presentar al cliente.
Uso: python tools/generate_client_pdf.py
Salida: dari-urdaneta/CW_ESP_Sistema_Chat_Dari_Urdaneta.pdf
"""
import sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime

# ══════════════════════════════════════════
# COLORS
# ══════════════════════════════════════════
BG_DARK = HexColor('#0d1117')
CARD_BG = HexColor('#161b22')
PINK = HexColor('#f778ba')
ACCENT = HexColor('#58a6ff')
GREEN = HexColor('#3fb950')
RED = HexColor('#f85149')
ORANGE = HexColor('#d29922')
PURPLE = HexColor('#bc8cff')
YELLOW = HexColor('#e3b341')
MUTED = HexColor('#8b949e')
TEXT_COLOR = HexColor('#1a1a2e')
LIGHT_BG = HexColor('#f8f9fa')
LIGHT_GREEN = HexColor('#d4edda')
LIGHT_RED = HexColor('#f8d7da')
LIGHT_BLUE = HexColor('#d1ecf1')
LIGHT_YELLOW = HexColor('#fff3cd')
LIGHT_PINK = HexColor('#fce4ec')
LIGHT_PURPLE = HexColor('#e8daef')
BORDER_LIGHT = HexColor('#dee2e6')
HEADER_BG = HexColor('#1a1a2e')
SECTION_BG = HexColor('#2d1b4e')

W, H = A4

# ══════════════════════════════════════════
# STYLES
# ══════════════════════════════════════════
styles = getSampleStyleSheet()

s_title_cover = ParagraphStyle('TitleCover', parent=styles['Title'],
    fontSize=28, leading=34, textColor=white, alignment=TA_CENTER,
    spaceAfter=10, fontName='Helvetica-Bold')

s_subtitle_cover = ParagraphStyle('SubCover', parent=styles['Normal'],
    fontSize=14, leading=18, textColor=HexColor('#cccccc'), alignment=TA_CENTER,
    spaceAfter=6, fontName='Helvetica')

s_h1 = ParagraphStyle('H1', parent=styles['Heading1'],
    fontSize=18, leading=22, textColor=HEADER_BG, fontName='Helvetica-Bold',
    spaceBefore=18, spaceAfter=10, borderPadding=(0, 0, 4, 0))

s_h2 = ParagraphStyle('H2', parent=styles['Heading2'],
    fontSize=13, leading=16, textColor=SECTION_BG, fontName='Helvetica-Bold',
    spaceBefore=14, spaceAfter=6)

s_body = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=10, leading=14, textColor=TEXT_COLOR, fontName='Helvetica',
    spaceAfter=6, alignment=TA_JUSTIFY)

s_body_bold = ParagraphStyle('BodyBold', parent=s_body,
    fontName='Helvetica-Bold')

s_small = ParagraphStyle('Small', parent=s_body,
    fontSize=9, leading=12, textColor=MUTED)

s_bullet = ParagraphStyle('Bullet', parent=s_body,
    leftIndent=16, bulletIndent=6, spaceBefore=2, spaceAfter=2)

s_example_good = ParagraphStyle('ExGood', parent=s_body,
    fontSize=10, leading=13, textColor=HexColor('#155724'),
    backColor=LIGHT_GREEN, borderPadding=8, leftIndent=8, rightIndent=8,
    spaceBefore=4, spaceAfter=4)

s_example_bad = ParagraphStyle('ExBad', parent=s_body,
    fontSize=10, leading=13, textColor=HexColor('#721c24'),
    backColor=LIGHT_RED, borderPadding=8, leftIndent=8, rightIndent=8,
    spaceBefore=4, spaceAfter=4)

s_note = ParagraphStyle('Note', parent=s_body,
    fontSize=9, leading=12, textColor=HexColor('#856404'),
    backColor=LIGHT_YELLOW, borderPadding=8, leftIndent=8, rightIndent=8,
    spaceBefore=4, spaceAfter=4)

s_info = ParagraphStyle('Info', parent=s_body,
    fontSize=10, leading=13, textColor=HexColor('#0c5460'),
    backColor=LIGHT_BLUE, borderPadding=8, leftIndent=8, rightIndent=8,
    spaceBefore=4, spaceAfter=4)

s_pink_box = ParagraphStyle('PinkBox', parent=s_body,
    fontSize=10, leading=14, textColor=HexColor('#880e4f'),
    backColor=LIGHT_PINK, borderPadding=10, leftIndent=8, rightIndent=8,
    spaceBefore=6, spaceAfter=6, fontName='Helvetica-Bold')

s_toc = ParagraphStyle('TOC', parent=s_body,
    fontSize=11, leading=16, spaceBefore=3, spaceAfter=3)

s_footer = ParagraphStyle('Footer', parent=styles['Normal'],
    fontSize=7, leading=9, textColor=MUTED, alignment=TA_CENTER)


# ══════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER_LIGHT,
                       spaceBefore=6, spaceAfter=6)

def spacer(h=6):
    return Spacer(1, h)

def bullet(text, style=None):
    return Paragraph(f"&bull; {text}", style or s_bullet)

def make_table(headers, rows, col_widths=None):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.4, BORDER_LIGHT),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, LIGHT_BG]),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]
    t.setStyle(TableStyle(style_cmds))
    return t

def section_num(n, title):
    return Paragraph(f"{n}. {title}", s_h1)


# ══════════════════════════════════════════
# PAGE TEMPLATES
# ══════════════════════════════════════════

def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(HEADER_BG)
    canvas.rect(0, 0, W, H, fill=1)
    # Accent bar
    canvas.setFillColor(PINK)
    canvas.rect(0, H - 8*mm, W, 8*mm, fill=1)
    canvas.rect(0, 0, W, 4*mm, fill=1)
    # Side accent
    canvas.setFillColor(ACCENT)
    canvas.rect(0, H*0.3, 6*mm, H*0.4, fill=1)
    canvas.restoreState()

def later_pages(canvas, doc):
    canvas.saveState()
    # Header line
    canvas.setStrokeColor(PINK)
    canvas.setLineWidth(1.5)
    canvas.line(20*mm, H - 12*mm, W - 20*mm, H - 12*mm)
    # Header text
    canvas.setFillColor(MUTED)
    canvas.setFont('Helvetica', 7)
    canvas.drawString(20*mm, H - 10*mm, "CW ESP  |  Sistema de Chat  |  Dari Urdaneta")
    canvas.drawRightString(W - 20*mm, H - 10*mm, f"Pag. {doc.page}")
    # Footer
    canvas.setFillColor(BORDER_LIGHT)
    canvas.setLineWidth(0.5)
    canvas.line(20*mm, 12*mm, W - 20*mm, 12*mm)
    canvas.setFillColor(MUTED)
    canvas.setFont('Helvetica', 6.5)
    canvas.drawCentredString(W/2, 7*mm, "Documento confidencial  |  CW ESP  |  2026")
    canvas.restoreState()


# ══════════════════════════════════════════
# BUILD DOCUMENT
# ══════════════════════════════════════════

def build_pdf():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_path = os.path.join(base_dir, "dari-urdaneta", "CW_ESP_Sistema_Chat_Dari_Urdaneta.pdf")

    doc = SimpleDocTemplate(
        out_path, pagesize=A4,
        leftMargin=20*mm, rightMargin=20*mm,
        topMargin=18*mm, bottomMargin=18*mm,
    )

    story = []

    # ══════════════════════════════════════
    # COVER PAGE
    # ══════════════════════════════════════
    story.append(Spacer(1, 55*mm))
    story.append(Paragraph("CW ESP", ParagraphStyle('Brand', parent=s_title_cover,
        fontSize=42, leading=48, textColor=PINK)))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Sistema Personalizado de Chat", s_title_cover))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Dari Urdaneta", ParagraphStyle('Name', parent=s_title_cover,
        fontSize=22, textColor=ACCENT)))
    story.append(Spacer(1, 15*mm))
    story.append(Paragraph(
        f"Fecha: {datetime.now().strftime('%d de %B de %Y').replace('February', 'febrero')}",
        s_subtitle_cover))
    story.append(Paragraph("Documento confidencial \u2014 Uso interno", s_subtitle_cover))
    story.append(Spacer(1, 20*mm))
    story.append(Paragraph(
        "Este documento contiene el sistema completo de comunicaci\u00f3n, "
        "scripts, formaci\u00f3n y estrategia de chat personalizado para Dari Urdaneta, "
        "dise\u00f1ado seg\u00fan sus exigencias y personalidad.",
        ParagraphStyle('CoverDesc', parent=s_subtitle_cover, fontSize=10, leading=14)))

    story.append(PageBreak())

    # ══════════════════════════════════════
    # TABLE OF CONTENTS
    # ══════════════════════════════════════
    story.append(Paragraph("\u00cdNDICE DE CONTENIDOS", s_h1))
    story.append(hr())
    toc_items = [
        "1. Perfil de Personalidad",
        "2. Reglas de Comunicaci\u00f3n",
        "3. Gu\u00eda de Diminutivos",
        "4. Reglas del Turur\u00fa",
        "5. Emojis Permitidos",
        "6. Regla de las 24 Horas",
        "7. Regla 70/30",
        "8. Segmentaci\u00f3n de Usuarios",
        "9. T\u00e9cnica \u201cEs Mi Novio\u201d",
        "10. Protocolo de Audios",
        "11. Diferenciaci\u00f3n de Energ\u00eda",
        "12. Sinergia Redes \u2194 Chat",
        "13. Journey Completo (45 mensajes)",
        "14. Manejo de Objeciones (37 protocolos)",
        "15. Templates de Difusi\u00f3n (20 templates)",
        "16. Banco de Frases (51 frases)",
        "17. Precios y Escalera PPV",
        "18. Nicho Foot Fetish",
        "19. Lista de Prohibiciones",
    ]
    for item in toc_items:
        story.append(Paragraph(item, s_toc))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 1. PERFIL DE PERSONALIDAD
    # ══════════════════════════════════════
    story.append(section_num(1, "Perfil de Personalidad"))
    story.append(hr())
    story.append(Paragraph(
        "<b>Dari Urdaneta</b> es una creadora venezolana de 21 a\u00f1os que vive en Medell\u00edn. "
        "Se cri\u00f3 en una finca rodeada de naturaleza y animales. Es una migrante que se hizo "
        "fuerte e independiente. Su autenticidad y naturalidad (sin cirug\u00edas) son su "
        "<b>ventaja competitiva principal</b>.", s_body))
    story.append(spacer())

    story.append(Paragraph(
        '<b>PRINCIPIO NO NEGOCIABLE:</b> "El chat no representa a Dari. El chat ES Dari." '
        'Cada mensaje debe sonar humano, personalizado y coherente con su personalidad real. '
        'Si un mensaje puede parecer gen\u00e9rico o intercambiable con el de otra modelo, '
        'hay que corregirlo antes de enviarlo.', s_pink_box))
    story.append(spacer())

    story.append(Paragraph("Rasgos Clave \u2014 As\u00ed ES Dari:", s_h2))
    for trait in [
        "Cari\u00f1osa, dulce y sensible",
        "Segura, expresiva e independiente",
        "Atenta y detallista \u2014 observa peque\u00f1os gestos y silencios",
        "Femenina y educada",
        "Cercana pero respetuosa",
        "Consciente y tranquila",
        "Natural (sin cirug\u00edas)",
        "Familiar, reservada, privada",
        "Amante de la naturaleza y los caballos",
    ]:
        story.append(bullet(trait))
    story.append(spacer())

    story.append(Paragraph("As\u00ed NO es Dari:", s_h2))
    for trait in [
        "NO es agresiva ni dominante",
        "NO es vulgar ni grosera",
        "NO es fiestera ni le gusta el alcohol",
        "NO es superficial ni materialista",
        "NO es impulsiva \u2014 es consciente",
        "NO usa jerga callejera ni expresiones fuertes",
    ]:
        story.append(bullet(trait))
    story.append(spacer())

    story.append(Paragraph("Datos Personales para Conversaci\u00f3n:", s_h2))
    datos = [
        ["Dato", "Informaci\u00f3n"],
        ["Edad", "21 a\u00f1os"],
        ["Origen", "Venezuela, vive en Medell\u00edn"],
        ["Infancia", "Criada en finca, rodeada de naturaleza y animales"],
        ["Animales", "Ama los caballos, sue\u00f1a con tener uno. Fobia a sapos/ranas"],
        ["F\u00edsico", "1.62m, 59kg, casta\u00f1a, ojos verde-marr\u00f3n, natural sin cirug\u00edas"],
        ["Tatuajes", 'Brazo derecho, pecho ("leal"), pierna ("los caminos dif\u00edciles...")'],
        ["Estilo de vida", "No fuma, no bebe, no fiestas. Entrena, cuida su piel/u\u00f1as, ama comer"],
        ["Familia", "Muy importante, sus personas m\u00e1s cercanas"],
        ["Relaci\u00f3n", "NUNCA decir que tiene pareja \u2014 enfocada en crecer y conectar"],
    ]
    story.append(make_table(datos[0], datos[1:], col_widths=[80, None]))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 2. REGLAS DE COMUNICACION
    # ══════════════════════════════════════
    story.append(section_num(2, "Reglas de Comunicaci\u00f3n"))
    story.append(hr())
    story.append(Paragraph(
        "Dari habla de forma <b>cercana, suave, femenina, con diminutivos, natural y sin groser\u00edas</b>. "
        "Para ella, <i>c\u00f3mo se dice algo es tan importante como lo que se dice</i>.", s_body))
    story.append(spacer())

    story.append(Paragraph("Apodos \u2014 SOLO estos tres:", s_h2))
    story.append(Paragraph(
        '<b>PERMITIDOS:</b> <font color="#3fb950"><b>mor</b></font>, '
        '<font color="#3fb950"><b>amor</b></font>, '
        '<font color="#3fb950"><b>papi</b></font> '
        '(tambi\u00e9n se puede usar el NOMBRE del sub)', s_info))
    story.append(spacer(4))
    story.append(Paragraph(
        '<b>PROHIBIDOS:</b> <font color="#f85149">cari\u00f1o, cielo, beb\u00e9, princesa, rey, '
        'baby, babe, nene, lindo, papito, mi vida, coraz\u00f3n</font> '
        '\u2014 Si usas cualquiera de estos, el cliente lo detectar\u00e1 inmediatamente.', s_example_bad))
    story.append(spacer())

    story.append(Paragraph("Ejemplos de Tono Correcto:", s_h2))
    story.append(Paragraph(
        '\u2705 CORRECTO: "Buenos d\u00edas, mor \u2764 \u00bfC\u00f3mo est\u00e1s? \u00bfQu\u00e9 planes tienes hoy?"',
        s_example_good))
    story.append(Paragraph(
        '\u2705 CORRECTO: "Ay amor, ando aqu\u00ed tranquilita un ratito... comiendito algo rico \u2728"',
        s_example_good))
    story.append(Paragraph(
        '\u274c INCORRECTO: "Hola cari\u00f1o! c\u00f3mo est\u00e1s? qu\u00e9 haces hoy beb\u00e9?"',
        s_example_bad))
    story.append(Paragraph(
        '\u274c INCORRECTO: "Hey nene, qu\u00e9 onda? estoy ac\u00e1 aburrida"',
        s_example_bad))
    story.append(spacer())

    story.append(Paragraph("Reglas de Groser\u00edas:", s_h2))
    story.append(Paragraph(
        "<b>Rapport / Conversaci\u00f3n general:</b> CERO groser\u00edas. Nunca.<br/>"
        "<b>Teasing:</b> CERO groser\u00edas. Sensual pero limpio.<br/>"
        "<b>Sexting avanzado:</b> Se puede escalar SUAVEMENTE, pero el tono sigue siendo dulce.",
        s_note))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 3. GUIA DE DIMINUTIVOS
    # ══════════════════════════════════════
    story.append(section_num(3, "Gu\u00eda de Diminutivos"))
    story.append(hr())
    story.append(Paragraph(
        "Los diminutivos son <b>marca fundamental de Dari</b>. Los usa constantemente y de forma "
        "natural. Son parte de su forma de hablar, no un adorno.", s_body))
    story.append(spacer())

    dims = [
        "comiendito", "duchita", "rapidito", "por favorcito", "delicadito",
        "tranquilita", "cansadita", "sue\u00f1ito", "ratito", "fotitos",
        "cositas", "poquito", "cerquita", "solita", "fresquita",
        "ligerito", "tardecito", "ocupadita", "peliculitas", "planesito",
    ]
    dim_rows = []
    for i in range(0, len(dims), 4):
        row = dims[i:i+4]
        while len(row) < 4:
            row.append("")
        dim_rows.append(row)
    story.append(make_table(["Diminutivo", "Diminutivo", "Diminutivo", "Diminutivo"],
                            dim_rows, col_widths=[None]*4))
    story.append(spacer())

    story.append(Paragraph("Ejemplos en Contexto:", s_h2))
    dim_examples = [
        ("\u00bfY t\u00fa qu\u00e9 haces?", 'Estoy comiendito algo amor \u00bfA ti qu\u00e9 es lo que m\u00e1s te gusta comer?'),
        ("\u00bfQu\u00e9 haces ahora?", 'Estoy aqu\u00ed tranquilita un ratito, organizando unas cositas \u00bfY t\u00fa?'),
        ("\u00bfYa cenaste?", 'S\u00ed mor, comiendito algo ligerito \u00bfT\u00fa ya cenaste o eres de los que comen tardecito?'),
        ("\u00bfTe vas a dormir?", 'Me est\u00e1 dando un sue\u00f1ito la verdad, pero todav\u00eda aguanto un ratito m\u00e1s contigo'),
        ("\u00bfEst\u00e1s ocupada?", 'Un poquito ocupadita, pero siempre saco un ratito para ti \u00bfQu\u00e9 necesitas mor?'),
    ]
    story.append(make_table(
        ["Pregunta del Sub", "Respuesta Estilo Dari"],
        [[q, r] for q, r in dim_examples],
        col_widths=[120, None]))
    story.append(spacer())
    story.append(Paragraph(
        "REGLA: Los diminutivos deben sonar naturales, no forzados. M\u00e1ximo 2-3 por mensaje.",
        s_note))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 4. REGLAS DEL TURURU
    # ══════════════════════════════════════
    story.append(section_num(4, "Reglas del Turur\u00fa"))
    story.append(hr())
    story.append(Paragraph(
        '"Turur\u00fa" es una <b>marca personal de Dari</b>. Lo usa para acompa\u00f1ar '
        'acciones cotidianas de forma ligera y adorable.', s_body))
    story.append(spacer())

    story.append(Paragraph("Uso Correcto:", s_h2))
    for ex in [
        '"Aqu\u00ed caminando tranquilita... turur\u00fa \u2728"',
        '"Pein\u00e1ndome tranquilita... turur\u00fa"',
        '"Comiendito algo rico... turur\u00fa \u2728"',
        '"Aqu\u00ed organizando mis cositas... turur\u00fa"',
        '"Haci\u00e9ndome las u\u00f1as... turur\u00fa \u2728"',
    ]:
        story.append(Paragraph(f"\u2705 {ex}", s_example_good))
    story.append(spacer())

    story.append(Paragraph("Uso Incorrecto:", s_h2))
    for ex in [
        "NUNCA dirigido directamente al sub",
        "NUNCA en contexto sexual",
        "NUNCA como respuesta a algo del sub",
        "NUNCA en exceso \u2014 m\u00e1ximo 1-2 veces al d\u00eda",
    ]:
        story.append(Paragraph(f"\u274c {ex}", s_example_bad))

    # ══════════════════════════════════════
    # 5. EMOJIS PERMITIDOS
    # ══════════════════════════════════════
    story.append(spacer(12))
    story.append(section_num(5, "Emojis Permitidos"))
    story.append(hr())
    emoji_data = [
        ["\u2728", "General, turur\u00fa"],
        ["\u2764", "Conexi\u00f3n, mor"],
        ["\U0001f497", "Amor, dulzura"],
        ["\U0001f60d", "Le gusta algo"],
        ["\u2764\ufe0f", "Cierre c\u00e1lido"],
    ]
    story.append(make_table(["Emoji", "Uso"], emoji_data, col_widths=[60, None]))
    story.append(spacer())
    story.append(Paragraph(
        "M\u00e1ximo 1-2 emojis por mensaje. Nunca 3+ seguidos. "
        "El emoji complementa, no reemplaza las palabras. "
        "NUNCA usar emojis agresivos, sexuales expl\u00edcitos o demasiado informales.",
        s_note))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 6. REGLA DE LAS 24 HORAS
    # ══════════════════════════════════════
    story.append(section_num(6, "Regla de las 24 Horas"))
    story.append(hr())
    story.append(Paragraph(
        '<b>NO vender NADA a un sub nuevo hasta que hayan pasado al menos 24 horas de '
        'conversaci\u00f3n O se haya establecido una conversaci\u00f3n larga y significativa.</b>',
        s_pink_box))
    story.append(spacer())

    story.append(Paragraph("D\u00eda 1 con un Sub Nuevo:", s_h2))
    for item in [
        "\u2705 Saludar, conocer, preguntar, escuchar",
        "\u2705 Compartir sobre ella (finca, Medell\u00edn, entrenar, comer)",
        "\u2705 Validar emocionalmente al sub",
        "\u2705 Crear conexi\u00f3n real y seguimiento",
        "\u274c NO enviar PPV",
        "\u274c NO hablar de contenido",
        "\u274c NO insinuar venta",
        "\u274c NO ser sexual",
    ]:
        story.append(bullet(item))
    story.append(spacer())

    story.append(Paragraph("Flujo Correcto:", s_h2))
    story.append(Paragraph(
        "<b>D\u00eda 1:</b> Rapport extenso (10-12 msgs) \u2192 Seguimiento emocional \u2192 Cierre c\u00e1lido \u2192 NO VENTA<br/>"
        "<b>D\u00eda 2:</b> Reconectar \u2192 Teasing gradual \u2192 Solo si hay se\u00f1ales \u2192 PPV Free teaser<br/>"
        "<b>D\u00eda 2-3:</b> Si responde bien \u2192 Escalar suavemente \u2192 PPV $15 \u2192 $30 \u2192 etc.",
        s_info))

    # ══════════════════════════════════════
    # 7. REGLA 70/30
    # ══════════════════════════════════════
    story.append(spacer(12))
    story.append(section_num(7, "Regla 70/30"))
    story.append(hr())
    story.append(Paragraph(
        '<b>70% conexi\u00f3n emocional + 30% monetizaci\u00f3n estrat\u00e9gica</b>',
        s_pink_box))
    story.append(spacer())

    story.append(Paragraph("El 70% \u2014 Conexi\u00f3n:", s_h2))
    for item in [
        "Conversaci\u00f3n real, preguntar por su d\u00eda, interesarse genuinamente",
        "Compartir cosas de la vida de Dari (entrenamiento, comida, u\u00f1as, caballos)",
        "Validaci\u00f3n emocional, ego boost, hacer sentir especial",
        "Seguimiento de conversaciones anteriores",
        "Turur\u00fa moments, cotidianidad",
    ]:
        story.append(bullet(item))

    story.append(Paragraph("El 30% \u2014 Monetizaci\u00f3n:", s_h2))
    for item in [
        "PPV cuando hay se\u00f1ales claras y ya hay confianza",
        "Teasing natural que surge de la conversaci\u00f3n",
        "Ofertas exclusivas y personalizadas",
    ]:
        story.append(bullet(item))
    story.append(spacer())
    story.append(Paragraph(
        '\u274c MAL: "Hola amor, tengo contenido nuevo para ti \u00bfquieres verlo? Solo $15"',
        s_example_bad))
    story.append(Paragraph(
        '\u2705 BIEN: "Buenos d\u00edas, mor \u00bfC\u00f3mo est\u00e1s? Yo aqu\u00ed comiendito algo rico... turur\u00fa" '
        '...despu\u00e9s de 5-7 mensajes de conversaci\u00f3n real... '
        '"Ay mor, me hiciste acordar... tengo algo bonito que quiero ense\u00f1arte"',
        s_example_good))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 8. SEGMENTACION DE USUARIOS
    # ══════════════════════════════════════
    story.append(section_num(8, "Segmentaci\u00f3n de Usuarios"))
    story.append(hr())
    story.append(Paragraph(
        "Cada sub es diferente. <b>Clasificar obligatoriamente</b> al sub y adaptar el tono:", s_body))
    story.append(spacer())

    seg_data = [
        ["Tipo", "Descripci\u00f3n", "Estrategia"],
        ["Emocional\n(Novio)", "Busca conexi\u00f3n real.\nEl m\u00e1s valioso.", "M\u00e1xima cercan\u00eda. Seguimiento. Audios. GFE completo."],
        ["Dominante", "Quiere controlar.\nDirecto y exigente.", "Dulzura con firmeza. Ceder control perceptual sin perder el real."],
        ["Sensible", "T\u00edmido, inseguro.\nNecesita validaci\u00f3n.", "Mucha dulzura extra. Diminutivos al m\u00e1ximo. Nunca presionar."],
        ["Comprador\nDirecto", "Viene a comprar.\nSabe lo que quiere.", "Misma dulzura pero m\u00e1s directa con oferta. Convertir a emocional."],
        ["Celoso", "Pregunta si habla\ncon otros.", "Calmar con dulzura. Hacer sentir exclusivo. NUNCA mencionar otros subs."],
        ["Casual", "Entra y sale.\nNo muy comprometido.", "Puerta abierta. Mensajes ligeros. Cuando vuelva, retomar con calidez."],
    ]
    story.append(make_table(seg_data[0], seg_data[1:], col_widths=[65, 110, None]))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 9. TECNICA "ES MI NOVIO"
    # ══════════════════════════════════════
    story.append(section_num(9, 'T\u00e9cnica "Es Mi Novio"'))
    story.append(hr())
    story.append(Paragraph(
        '<b>Mentalidad obligatoria al entrar en cada chat: "Este es mi novio y quiero conquistarlo."</b>',
        s_pink_box))
    story.append(spacer())

    story.append(Paragraph("S\u00cd Hacer:", s_h2))
    for item in [
        "Seguimiento real (\u00bfC\u00f3mo te fue en el trabajo?)",
        "Preguntas de continuidad",
        "Notas actualizadas sobre cada sub",
        "Referencias a conversaciones anteriores",
        "Recordar detalles personales",
    ]:
        story.append(bullet(item))

    story.append(Paragraph("NO Hacer:", s_h2))
    for item in [
        "Exceso de disponibilidad (ser pegajosa)",
        "Exceso de venta",
        "Exceso de intensidad emocional",
        "Responder al instante SIEMPRE",
    ]:
        story.append(bullet(item))

    # ══════════════════════════════════════
    # 10. PROTOCOLO DE AUDIOS
    # ══════════════════════════════════════
    story.append(spacer(12))
    story.append(section_num(10, "Protocolo de Audios"))
    story.append(hr())
    story.append(Paragraph(
        '<b>Los audios son la herramienta m\u00e1s poderosa de Dari.</b> Ella conecta mucho por voz. '
        'USO DIARIO OBLIGATORIO con segmentaci\u00f3n estrat\u00e9gica.', s_pink_box))
    story.append(spacer())

    story.append(Paragraph("Cu\u00e1ndo enviar audio:", s_h2))
    for item in [
        "Buenos d\u00edas personalizado para top spenders",
        "Tras conversaci\u00f3n emocional profunda",
        "Despu\u00e9s de momento vulnerable del usuario",
        "Despu\u00e9s de una compra (agradecimiento genuino)",
        "En momentos de cercan\u00eda y conexi\u00f3n real",
    ]:
        story.append(bullet(item))

    audio_seg = [
        ["Tipo de Sub", "Audios"],
        ["Top Spenders", "Audio diario de buenos d\u00edas + post-compra"],
        ["Emocionales", "Audios de seguimiento y conexi\u00f3n"],
        ["Sensibles", "Audios de validaci\u00f3n y cercan\u00eda"],
        ["Casuales", "Audio de re-engagement cuando vuelven"],
    ]
    story.append(make_table(audio_seg[0], audio_seg[1:], col_widths=[110, None]))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 11. DIFERENCIACION DE ENERGIA
    # ══════════════════════════════════════
    story.append(section_num(11, "Diferenciaci\u00f3n de Energ\u00eda"))
    story.append(hr())
    energy_data = [
        ["Canal", "Energ\u00eda"],
        ["TikTok / Reels / Redes", "Energ\u00e9tica, divertida, extrovertida, directa, expresiva"],
        ["Chat / Mensajes / Lives OF", "Calmada, pausada, intrigante, \u00edntima, dulce, cercana"],
    ]
    story.append(make_table(energy_data[0], energy_data[1:], col_widths=[130, None]))
    story.append(spacer())
    story.append(Paragraph(
        'ERROR COM\u00daN: El usuario ve a Dari energ\u00e9tica en TikTok y espera lo mismo en el chat. '
        'NO caer en eso. Si pregunta: "Ay mor, es que en redes soy m\u00e1s loquita jaja pero '
        'contigo me sale mi lado m\u00e1s tranquilito e \u00edntimo... me gusta m\u00e1s as\u00ed"', s_note))

    # ══════════════════════════════════════
    # 12. SINERGIA REDES ↔ CHAT
    # ══════════════════════════════════════
    story.append(spacer(12))
    story.append(section_num(12, "Sinergia Redes \u2194 Chat"))
    story.append(hr())
    story.append(Paragraph(
        "Tiene que existir una <b>sinergia directa</b> entre lo que Dari transmite en redes y lo que "
        "se conversa dentro de la p\u00e1gina. Cuando el usuario percibe coherencia, aumenta "
        "confianza, cercan\u00eda, percepci\u00f3n de autenticidad, y retenci\u00f3n + gasto.", s_body))
    story.append(spacer())

    for item in [
        "<b>Update diario de la modelo:</b> Dari enviar\u00e1 un mini update (2-5 l\u00edneas) sobre qu\u00e9 har\u00e1/hizo",
        "<b>Usar el update como realidad:</b> Abrir conversaciones con eso, dar seguimiento",
        "<b>Stories/Posts \u2192 Puntos conversacionales:</b> Todo contenido reciente se usa en el chat",
        "<b>Lives \u2192 Continuidad:</b> 'Ayer en el live dije X...' / 'Te cont\u00e9 algo de...'",
    ]:
        story.append(bullet(item))
    story.append(spacer())
    story.append(Paragraph(
        "Si no hay sinergia, el usuario detecta disonancia y cae engagement, credibilidad y ventas.",
        s_note))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 13. JOURNEY COMPLETO
    # ══════════════════════════════════════
    story.append(section_num(13, "Journey Completo (45 mensajes)"))
    story.append(hr())

    # Import config
    from models.dari_urdaneta import config as dari_config

    journey = dari_config.get("journey", [])

    # Group by phase
    phases = {}
    phase_order = []
    current_phase = None
    sext_count = 0
    for msg_id, text, note, msg_type in journey:
        if msg_type in ("rapport", "teasing", "aftercare"):
            phase_name = msg_type.title()
        elif msg_type in ("sext", "ppv", "wait"):
            if msg_type == "ppv" or (current_phase and current_phase.startswith("Sexting")):
                phase_name = current_phase if current_phase and current_phase.startswith("Sexting") else f"Sexting {sext_count}"
            elif msg_type == "sext" and (not current_phase or not current_phase.startswith("Sexting")):
                sext_count += 1
                phase_name = f"Sexting {sext_count}"
            elif msg_type == "wait":
                phase_name = current_phase or "Teasing"
            else:
                phase_name = current_phase or "Sexting"
        else:
            phase_name = msg_type.title()

        if phase_name != current_phase:
            current_phase = phase_name
            if phase_name not in phases:
                phases[phase_name] = []
                phase_order.append(phase_name)
        phases[phase_name].append((msg_id, text, note, msg_type))

    for phase_name in phase_order:
        msgs = phases[phase_name]
        story.append(Paragraph(f"<b>{phase_name}</b> ({len(msgs)} msgs)", s_h2))
        rows = []
        for msg_id, text, note, msg_type in msgs:
            type_label = {"ppv": "[PPV]", "wait": "[ESPERAR]"}.get(msg_type, "")
            clean_text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            note_text = ""
            if note:
                note_text = note.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            rows.append([msg_id, f"{type_label} {clean_text}".strip(), note_text])
        story.append(make_table(["ID", "Mensaje", "Nota"], rows, col_widths=[40, 240, None]))
        story.append(spacer(4))

    story.append(PageBreak())

    # ══════════════════════════════════════
    # 14. MANEJO DE OBJECIONES
    # ══════════════════════════════════════
    story.append(section_num(14, "Manejo de Objeciones (37 protocolos)"))
    story.append(hr())
    story.append(Paragraph(
        "Resumen de los protocolos de objeciones, resistencias y scripts situacionales. "
        "Tono dulce, sin agresividad. Precios altos = exclusividad, NO descuento.", s_body))
    story.append(spacer())

    obj_scripts = dari_config.get("obj_scripts", {})
    cat_names = {"obj": "OBJECIONES", "res": "RESISTENCIAS", "sit": "SITUACIONALES"}
    cat_groups = {"obj": [], "res": [], "sit": []}
    for sheet_name, (rows, category) in obj_scripts.items():
        cat_groups.get(category, []).append((sheet_name, rows))

    for cat_key in ("obj", "res", "sit"):
        items = cat_groups[cat_key]
        if not items:
            continue
        story.append(Paragraph(f"<b>{cat_names[cat_key]}</b>", s_h2))
        for sheet_name, rows in items:
            display_name = sheet_name.rstrip("0123456789").replace("_", " ").title()
            variant = sheet_name[-1] if sheet_name[-1].isdigit() else ""
            label = f"{display_name}" + (f" (v{variant})" if variant else "")
            step_texts = []
            for step_name, text, note in rows:
                clean = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                step_texts.append(f"<b>{step_name}:</b> {clean}")
            story.append(Paragraph(f"<b>{label}:</b> {' \u2192 '.join(step_texts)}", s_small))
            story.append(spacer(2))
    story.append(PageBreak())

    # ══════════════════════════════════════
    # 15. TEMPLATES DE DIFUSION
    # ══════════════════════════════════════
    story.append(section_num(15, "Templates de Difusi\u00f3n (20 templates)"))
    story.append(hr())

    broadcast_sections = {
        "Buenos D\u00edas (Ma\u00f1ana)": [
            ("Buenos d\u00edas, mor \u2764 acabo de despertar y me qued\u00e9 un ratito en la cama pensando en cositas bonitas... \u00bfc\u00f3mo amaneciste hoy?", "Sin venta"),
            ("Hola amor \u2728 hoy me levant\u00e9 con ganas de entrenar tempranito... ya sabes que eso me pone de buen humor \u2764 cu\u00e9ntame, \u00bfqu\u00e9 planes tienes hoy?", "Sin venta"),
            ("Buenos d\u00edas, papi \u2764 aqu\u00ed comiendito mi desayuno tranquilita... turur\u00fa \u2728 \u00bfya desayunaste o eres de los que se saltan eso? jaja", "Sin venta"),
            ("Hola mor \u2764 hoy me despert\u00e9 pensando en ti... no s\u00e9 por qu\u00e9 pero me dieron ganas de escribirte \u2728 \u00bfc\u00f3mo est\u00e1s?", "Sin venta + audio top spenders"),
            ("Buenos d\u00edas amor \u2728 sabes que me encanta cuidarme... hoy me hice mi rutinita de skincare y me siento preciosa \u2764 \u00bfqu\u00e9 tal tu ma\u00f1ana?", "Sin venta"),
        ],
        "Tarde": [
            ("Hola amor \u2764 \u00bfc\u00f3mo va tu d\u00eda? Yo aqu\u00ed despu\u00e9s de entrenar, me siento incre\u00edble \u2728 cu\u00e9ntame de ti", "Sin venta"),
            ("Mor \u2764 estoy aqu\u00ed comiendo algo rico y me acord\u00e9 de ti... \u00bferes de los que comen bien o de los que comen cualquier cosita?", "Sin venta"),
            ("Hola papi \u2728 oye, ando con un humor diferente hoy... no s\u00e9 qu\u00e9 es pero tengo ganas de ense\u00f1arte algo que hice \u2764 \u00bfquieres ver?", "Monetizaci\u00f3n suave"),
            ("Amor \u2764 aqu\u00ed arregl\u00e1ndome las u\u00f1as tranquilita \u2728 sabes que eso me relaja mucho... \u00bft\u00fa qu\u00e9 haces para relajarte?", "Sin venta"),
            ("Hola mor \u2764 ay hoy vi un video de caballos y casi lloro de lo bonito \u2764 \u00bfsab\u00edas que amo los caballos?", "Sin venta"),
        ],
        "Noche": [
            ("Hola amor \u2764 ya aqu\u00ed en mi camita tranquilita... me dio un sue\u00f1ito pero no me quiero dormir sin saber c\u00f3mo te fue hoy \u2728", "Sin venta"),
            ("Mor \u2728 \u00bfsigues despierto? Yo aqu\u00ed viendo una peliculita acurrucadita... me hac\u00eda falta hablar contigo \u2764", "Sin venta"),
            ("Hola papi \u2764 oye, esta noche me siento... diferente \u2728 como que ando con ganas de ense\u00f1arte algo... \u00bfquieres?", "Monetizaci\u00f3n"),
            ("Amor \u2764 me di mi duchita y qued\u00e9 toda fresquita \u2728 estoy relajadita aqu\u00ed solita... \u00bft\u00fa c\u00f3mo est\u00e1s?", "Puente a escalada"),
            ("Mor \u2764 ya me voy a dormir pero quer\u00eda desearte buenas noches... sue\u00f1a bonito \u2728 ma\u00f1ana me cuentas", "Sin venta"),
        ],
        "Post-Live / Post-Contenido / Re-engagement": [
            ("Mor \u2764 \u00bfestuviste en mi live? Es que fue tan bonito... compart\u00ed algo muy personal y me acord\u00e9 de ti \u2728", "Post-live"),
            ("Amor \u2728 acabo de grabar algo y ay... qued\u00e9 toda emocionada \u2764 me encant\u00f3 c\u00f3mo sali\u00f3 y pens\u00e9 en ti primero", "Post-contenido"),
            ("Mor \u2764 hoy me tom\u00e9 unas fotitos que me encantaron \u2728 estaba pensando en ti mientras las hac\u00eda...", "Seed para PPV"),
            ("Hola amor \u2764 hace ratito que no hablamos y me dieron ganas de escribirte... \u00bfc\u00f3mo has estado? \u2728 te extra\u00f1\u00e9", "Re-engagement"),
            ("Mor \u2728 hoy vi algo que me record\u00f3 a ti y me dio nostalgia de nuestras charlas \u2764 \u00bfest\u00e1s por ah\u00ed?", "Re-engagement"),
        ],
    }

    for section_name, templates in broadcast_sections.items():
        story.append(Paragraph(f"<b>{section_name}</b>", s_h2))
        rows = [[str(i+1), t, cat] for i, (t, cat) in enumerate(templates)]
        story.append(make_table(["#", "Mensaje", "Tipo"], rows, col_widths=[20, 310, None]))
        story.append(spacer(4))

    story.append(PageBreak())

    # ══════════════════════════════════════
    # 16. BANCO DE FRASES
    # ══════════════════════════════════════
    story.append(section_num(16, "Banco de Frases (51 frases)"))
    story.append(hr())

    phrase_cats = {
        "Cotidianas (15)": [
            'Estoy comiendito algo amor \u00bfA ti qu\u00e9 es lo que m\u00e1s te gusta comer?',
            'Estoy aqu\u00ed tranquilita un ratito, organizando unas cositas \u00bfY t\u00fa qu\u00e9 haces?',
            'S\u00ed mor, comiendito algo ligerito \u00bfT\u00fa ya cenaste o eres de los que comen tardecito?',
            'Me est\u00e1 dando un sue\u00f1ito la verdad, pero todav\u00eda aguanto un ratito m\u00e1s contigo',
            'S\u00ed amor, me di una duchita rapidita. Qued\u00e9 fresquita \u00bfT\u00fa ya te diste la tuya?',
            'Hoy estoy tranquilita haciendo unas cositas pendientes \u2728 luego salgo un ratito',
            'Un poquito ocupadita, pero siempre saco un ratito para ti \u00bfQu\u00e9 necesitas mor?',
            'Me gusta hacer cositas tranquilitas, ver peliculitas, comer algo rico \u00bfY t\u00fa?',
            'Estoy aqu\u00ed solita tranquilita un ratito \u00bfY t\u00fa est\u00e1s solito tambi\u00e9n?',
            'Unas cositas ligeritas, nada pesadito \u00bfT\u00fa eres de comer dulcecito o salado?',
            'Depende mor... a veces tranquilita con mi sue\u00f1ito y otras veces hablando un ratito contigo',
            'Me gusta que sea segurito pero delicadito conmigo \u00bfT\u00fa c\u00f3mo eres?',
            'Un poquito cansadita, pero feliz \u00bfT\u00fa tambi\u00e9n tuviste un d\u00eda larguito?',
            'Ma\u00f1ana tengo unas cositas que hacer, pero siempre saco un ratito para hablar contigo',
            'Vivo en Medell\u00edn, amor. Me vine de Venezuela a empezar de nuevo \u00bfT\u00fa de d\u00f3nde eres?',
        ],
        "Emocionales (8)": [
            'Ay amor, me da cosita que est\u00e9s as\u00ed... cu\u00e9ntame qu\u00e9 pas\u00f3, aqu\u00ed estoy para ti',
            'Ven, mor... tranquilo. Todo est\u00e1 bien, aqu\u00ed estoy',
            'Ay me encanta verte as\u00ed de feliz, amor. Eso me pone feliz a m\u00ed tambi\u00e9n \u2728',
            'Papi, respira... s\u00e9 que ha sido un d\u00eda dif\u00edcil pero aqu\u00ed puedes relajarte conmigo',
            'Gracias por contarme eso, mor... me gusta que conf\u00edes en m\u00ed',
            'Ay mor, no seas as\u00ed contigo... eres m\u00e1s especial de lo que piensas',
            'Ay amor, eso que me dijiste me lleg\u00f3 al coraz\u00f3n de verdad...',
            'Me gusta mucho hablar contigo, mor. Siento que me entiendes y eso es dif\u00edcil de encontrar',
        ],
        "Coqueteo (8)": [
            'Es que hay algo en ti que me hace sentir... diferente. No s\u00e9 c\u00f3mo explicarlo, mor',
            'Ay amor, despu\u00e9s de entrenar me siento como... no s\u00e9, toda sensible. Y hablar contigo no me ayuda jaja',
            'Sabes que me pones de un humor... contigo me sale mi lado m\u00e1s travieso, mor',
            'Me acabo de dar mi duchita y qued\u00e9 toda fresquita... estoy aqu\u00ed solita pensando en cositas',
            '\u00bfSabes? Tengo ganas de ense\u00f1arte algo... pero no s\u00e9 si est\u00e9s listo, amor',
            'Es tu culpa mor... me tienes toda sensible y no puedo dejar de pensar en ti',
            'Contigo me siento c\u00f3moda de una forma que no me pasa con cualquiera, amor',
            'Ay amor... me est\u00e1s haciendo sentir cosas que no le cuento a nadie',
        ],
        "Post-Compra / Seguimiento / Turur\u00fa / Calmar (20)": [
            'Ay mor, gracias por apreciar lo que hago. De verdad significa mucho para m\u00ed',
            'Amor, me encanta que te haya gustado... lo hice pensando en ti',
            'Oye mor, \u00bfal final c\u00f3mo te fue con eso que me contaste? Estuve pensando en eso',
            'Me acord\u00e9 de ti hoy, amor. Vi algo que me record\u00f3 a lo que me contaste',
            'Aqu\u00ed caminando tranquilita... turur\u00fa \u2728 \u00bfY t\u00fa qu\u00e9 haces, mor?',
            'Comiendito algo rico... turur\u00fa \u2728 \u00bfYa comiste t\u00fa, amor?',
            'Pein\u00e1ndome tranquilita... turur\u00fa \u2728 ahorita te mando una fotito',
            'Ven, mor... tranquilo. Todo est\u00e1 bien, aqu\u00ed estoy',
            'Papi, si quieres hablar aqu\u00ed estoy para ti. No tienes que cargar todo solito',
        ],
    }

    for cat_name, phrases in phrase_cats.items():
        story.append(Paragraph(f"<b>{cat_name}</b>", s_h2))
        rows = [[str(i+1), p] for i, p in enumerate(phrases)]
        story.append(make_table(["#", "Frase"], rows, col_widths=[25, None]))
        story.append(spacer(4))

    story.append(PageBreak())

    # ══════════════════════════════════════
    # 17. PRECIOS Y ESCALERA PPV
    # ══════════════════════════════════════
    story.append(section_num(17, "Precios y Escalera PPV"))
    story.append(hr())

    story.append(Paragraph("Escalera de PPV:", s_h2))
    ppv_data = [
        ["PPV 0 (Teaser)", "GRATIS", "Foto bonita, sensual pero no expl\u00edcita"],
        ["PPV 1", "$15", "Contenido suave, personal"],
        ["PPV 2", "$30", 'M\u00e1s expl\u00edcito, "solo para ti"'],
        ["PPV 3", "$50", "Contenido avanzado, exclusivo"],
        ["PPV 4", "$75", 'M\u00e1ximo nivel, "nunca hice esto para nadie"'],
    ]
    story.append(make_table(["Nivel", "Precio", "Contenido"], ppv_data, col_widths=[90, 60, None]))
    story.append(spacer())

    story.append(Paragraph("Precios de Servicios:", s_h2))
    svc_data = [
        ["Customs", "$250+ m\u00ednimo", "NUNCA bajar \u2014 exclusividad"],
        ["Fotos personalizadas", "$150+", '"Solo para ti, amor"'],
        ["Dick Rates", "$250+", "Premium y personalizado"],
    ]
    story.append(make_table(["Servicio", "Precio", "Notas"], svc_data, col_widths=[110, 70, None]))
    story.append(spacer())
    story.append(Paragraph(
        "NUNCA dar descuento. NUNCA comparar precios. NUNCA justificar el precio pidiendo perd\u00f3n. "
        "Manejar objeci\u00f3n de precio con EXCLUSIVIDAD, no con rebaja.", s_example_bad))

    # ══════════════════════════════════════
    # 18. NICHO FOOT FETISH
    # ══════════════════════════════════════
    story.append(spacer(12))
    story.append(section_num(18, "Nicho Foot Fetish"))
    story.append(hr())
    story.append(Paragraph(
        "El foot fetish es un <b>nicho especial de Dari</b>. Tratarlo con naturalidad y entusiasmo, "
        "nunca con verg\u00fcenza.", s_body))
    story.append(spacer())
    for item in [
        'Tratar con dulzura: "ay amor, me encanta que eso te guste"',
        "Integrar en la conversaci\u00f3n cuando sea apropiado",
        "Conectar con su rutina de cuidado: u\u00f1as, pedicura, skincare",
        '"Mis piececitos" \u2014 diminutivo aplicado naturalmente',
        "NUNCA burlarse ni hacer sentir raro al sub",
        "NUNCA asumir que TODOS los subs quieren foot fetish",
    ]:
        story.append(bullet(item))

    # ══════════════════════════════════════
    # 19. LISTA DE PROHIBICIONES
    # ══════════════════════════════════════
    story.append(spacer(12))
    story.append(section_num(19, "Lista de Prohibiciones"))
    story.append(hr())
    story.append(Paragraph("<b>PROHIBIDO TOTALMENTE:</b>", s_h2))
    prohibitions = [
        "Usar apodos que no sean mor/amor/papi",
        "Groser\u00edas en conversaci\u00f3n general",
        "Vender a un sub nuevo antes de 24h",
        "Repetir estructuras de mensaje id\u00e9nticas",
        "Mensajes gen\u00e9ricos que suenen a bot",
        "Exceso de emojis",
        "Decir que tiene novio/pareja",
        "Mencionar que bebe o fuma",
        "Tono agresivo, dominante o vulgar",
        "Dar descuentos en precios",
        "Enviar el mismo mensaje a todos los subs",
        "Ignorar el contexto del d\u00eda de la modelo",
        "No usar diminutivos en la conversaci\u00f3n",
        'Usar "turur\u00fa" dirigido al sub o en contexto sexual',
        "Videollamadas o G/G",
    ]
    for p in prohibitions:
        story.append(Paragraph(f"\u274c {p}", s_example_bad))

    story.append(spacer(8))
    story.append(Paragraph("<b>SIEMPRE HACER:</b>", s_h2))
    always_do = [
        "Usar diminutivos naturalmente",
        "Tono dulce, femenino y cercano",
        "Seguimiento real de conversaciones",
        "Adaptar tono seg\u00fan tipo de usuario",
        "Usar contexto del d\u00eda de la modelo",
        "Audios diarios a top spenders",
        "Notas actualizadas de cada sub",
        "Regla 70/30 siempre",
        "Coherencia redes \u2194 chat",
        "Preguntar, escuchar, validar",
    ]
    for a in always_do:
        story.append(Paragraph(f"\u2705 {a}", s_example_good))

    # ══════════════════════════════════════
    # BUILD
    # ══════════════════════════════════════
    doc.build(story, onFirstPage=cover_page, onLaterPages=later_pages)
    print(f"\n[PDF] Generado: {out_path}")
    print(f"[PDF] Tama\u00f1o: {os.path.getsize(out_path) / 1024:.0f} KB")
    return out_path


if __name__ == "__main__":
    build_pdf()
