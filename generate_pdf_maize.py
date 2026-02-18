"""Generate a fancy PDF from the Maize MoA Report with CONFIDENTIAL markings.
Uses reportlab (no system deps required) with markdown parsing."""

import re
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, Frame
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

REPORT_PATH = "ExRNA_Maize_MoA_Report.md"
OUTPUT_PATH = "ExRNA_Ag_Final_Report_CONFIDENTIAL_Long_Maize.pdf"

# ============ COLORS ============
DARK_NAVY = HexColor('#0c1929')
NAVY = HexColor('#1a2744')
MID_NAVY = HexColor('#243b5e')
GREEN_ACCENT = HexColor('#2ecc71')
RED_CONF = HexColor('#c0392b')
LIGHT_RED = HexColor('#e74c3c')
GRAY_TEXT = HexColor('#7f8c8d')
LIGHT_GRAY = HexColor('#95a5a6')
BODY_TEXT = HexColor('#1a1a2e')
TABLE_ALT = HexColor('#f8f9fa')
BLUE_LINK = HexColor('#2980b9')
BLUE_QUOTE_BG = HexColor('#eaf2f8')
BLUE_QUOTE_BORDER = HexColor('#3498db')
CODE_BG = HexColor('#f4f6f9')
WHITE = HexColor('#ffffff')
BLACK = HexColor('#000000')
BORDER_GRAY = HexColor('#bdc3c7')
SECTION_COLOR = HexColor('#34495e')

# ============ STYLES ============
styles = getSampleStyleSheet()

# Override and add custom styles
styles.add(ParagraphStyle(
    'BodyJustify',
    parent=styles['Normal'],
    fontSize=10,
    leading=16,
    textColor=BODY_TEXT,
    alignment=TA_JUSTIFY,
    spaceAfter=3*mm,
    fontName='Helvetica',
))

styles.add(ParagraphStyle(
    'H1Custom',
    parent=styles['Heading1'],
    fontSize=20,
    leading=26,
    textColor=DARK_NAVY,
    fontName='Helvetica-Bold',
    spaceBefore=12*mm,
    spaceAfter=5*mm,
    borderWidth=2,
    borderColor=GREEN_ACCENT,
    borderPadding=(0, 0, 3*mm, 0),
))

styles.add(ParagraphStyle(
    'H2Custom',
    parent=styles['Heading2'],
    fontSize=15,
    leading=20,
    textColor=NAVY,
    fontName='Helvetica-Bold',
    spaceBefore=10*mm,
    spaceAfter=4*mm,
    borderWidth=1,
    borderColor=BORDER_GRAY,
    borderPadding=(0, 0, 2*mm, 0),
))

styles.add(ParagraphStyle(
    'H3Custom',
    parent=styles['Heading3'],
    fontSize=12,
    leading=16,
    textColor=MID_NAVY,
    fontName='Helvetica-Bold',
    spaceBefore=7*mm,
    spaceAfter=3*mm,
))

styles.add(ParagraphStyle(
    'H4Custom',
    parent=styles['Heading4'],
    fontSize=10.5,
    leading=14,
    textColor=SECTION_COLOR,
    fontName='Helvetica-Bold',
    spaceBefore=5*mm,
    spaceAfter=2*mm,
))

styles.add(ParagraphStyle(
    'CodeBlock',
    parent=styles['Code'],
    fontSize=7.5,
    leading=11,
    textColor=HexColor('#ecf0f1'),
    backColor=HexColor('#1a1a2e'),
    fontName='Courier',
    leftIndent=5*mm,
    rightIndent=5*mm,
    spaceBefore=3*mm,
    spaceAfter=5*mm,
    borderWidth=0,
    borderPadding=4*mm,
))

styles.add(ParagraphStyle(
    'BlockQuote',
    parent=styles['Normal'],
    fontSize=9.5,
    leading=14,
    textColor=BODY_TEXT,
    backColor=BLUE_QUOTE_BG,
    fontName='Helvetica-Oblique',
    leftIndent=8*mm,
    rightIndent=3*mm,
    spaceBefore=3*mm,
    spaceAfter=4*mm,
    borderWidth=0,
    borderPadding=3*mm,
))

styles.add(ParagraphStyle(
    'ListItem',
    parent=styles['Normal'],
    fontSize=10,
    leading=15,
    textColor=BODY_TEXT,
    fontName='Helvetica',
    leftIndent=8*mm,
    spaceAfter=1.5*mm,
    bulletIndent=3*mm,
))

styles.add(ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontSize=8,
    leading=11,
    textColor=BODY_TEXT,
    fontName='Helvetica',
    alignment=TA_LEFT,
))

styles.add(ParagraphStyle(
    'TableHeader',
    parent=styles['Normal'],
    fontSize=7.5,
    leading=10,
    textColor=WHITE,
    fontName='Helvetica-Bold',
    alignment=TA_LEFT,
))

styles.add(ParagraphStyle(
    'ClassificationBox',
    parent=styles['Normal'],
    fontSize=8.5,
    leading=13,
    textColor=GRAY_TEXT,
    fontName='Helvetica',
    borderWidth=1,
    borderColor=BORDER_GRAY,
    borderPadding=3*mm,
    backColor=HexColor('#fafbfc'),
    spaceAfter=4*mm,
))

# ============ HEADER / FOOTER ============
def header_footer(canvas, doc):
    """Draw header and footer on each page (except cover)."""
    canvas.saveState()
    page_num = canvas.getPageNumber()

    if page_num > 1:
        # Top left - CONFIDENTIAL
        canvas.setFont('Helvetica-Bold', 7)
        canvas.setFillColor(RED_CONF)
        canvas.drawString(20*mm, A4[1] - 15*mm, "CONFIDENTIAL")

        # Top right - org info
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(GRAY_TEXT)
        canvas.drawRightString(A4[0] - 20*mm, A4[1] - 15*mm,
                              "ExRNA-Ag  |  Maize MoA Dossier  |  Sarthak Tiwary")

        # Bottom left - confidential
        canvas.setFont('Helvetica-Bold', 6.5)
        canvas.setFillColor(RED_CONF)
        canvas.drawString(20*mm, 15*mm, "CONFIDENTIAL  --  Do Not Distribute")

        # Bottom center - page number
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(LIGHT_GRAY)
        canvas.drawCentredString(A4[0]/2, 15*mm, f"Page {page_num}")

        # Bottom right - date
        canvas.setFont('Helvetica', 7)
        canvas.setFillColor(LIGHT_GRAY)
        canvas.drawRightString(A4[0] - 20*mm, 15*mm, "February 2026")

        # Watermark
        canvas.setFont('Helvetica-Bold', 50)
        canvas.setFillColor(Color(0.75, 0.22, 0.17, alpha=0.03))
        canvas.saveState()
        canvas.translate(A4[0]/2, A4[1]/2)
        canvas.rotate(40)
        canvas.drawCentredString(0, 0, "CONFIDENTIAL")
        canvas.restoreState()

    canvas.restoreState()


def build_cover_page(canvas, doc):
    """Draw the cover page."""
    canvas.saveState()
    width, height = A4

    # Background gradient (approximated with rectangles)
    steps = 100
    for i in range(steps):
        frac = i / steps
        r = 0.047 + frac * (0.141 - 0.047)
        g = 0.098 + frac * (0.231 - 0.098)
        b = 0.161 + frac * (0.369 - 0.161)
        y = height - (height * i / steps)
        canvas.setFillColor(Color(r, g, b))
        canvas.rect(0, y - height/steps, width, height/steps + 1, fill=1, stroke=0)

    # Watermark CONFIDENTIAL (faint)
    canvas.setFont('Helvetica-Bold', 72)
    canvas.setFillColor(Color(0.75, 0.22, 0.17, alpha=0.06))
    canvas.saveState()
    canvas.translate(width/2, height/2)
    canvas.rotate(35)
    canvas.drawCentredString(0, 0, "CONFIDENTIAL")
    canvas.restoreState()

    # Border box
    bx = 20*mm
    bw = width - 40*mm
    by = 35*mm
    bh = height - 70*mm
    canvas.setStrokeColor(Color(1, 1, 1, alpha=0.15))
    canvas.setLineWidth(1)
    canvas.roundRect(bx, by, bw, bh, 4, fill=0, stroke=1)

    # Inner box
    canvas.setFillColor(Color(1, 1, 1, alpha=0.03))
    canvas.setStrokeColor(Color(1, 1, 1, alpha=0.08))
    canvas.roundRect(bx + 3*mm, by + 3*mm, bw - 6*mm, bh - 6*mm, 2, fill=1, stroke=1)

    # Content positioning
    cx = width / 2
    top = height - 60*mm

    # Logo
    canvas.setFont('Helvetica', 14)
    canvas.setFillColor(Color(1, 1, 1, alpha=0.5))
    canvas.drawCentredString(cx, top, "E X R N A - A G")

    # Divider line
    canvas.setStrokeColor(Color(0.18, 0.80, 0.44, alpha=0.6))
    canvas.setLineWidth(1)
    canvas.line(cx - 25*mm, top - 10*mm, cx + 25*mm, top - 10*mm)

    # Title
    canvas.setFont('Helvetica-Bold', 18)
    canvas.setFillColor(WHITE)
    title_y = top - 25*mm
    canvas.drawCentredString(cx, title_y, "Bacterial Extracellular tRF-Mediated")
    canvas.drawCentredString(cx, title_y - 22, "Gene Regulation in Maize (Zea mays L.)")

    # Subtitle
    canvas.setFont('Helvetica', 11)
    canvas.setFillColor(Color(1, 1, 1, alpha=0.65))
    sub_y = title_y - 50
    canvas.drawCentredString(cx, sub_y, "Mechanistic Mode of Action, Grain-Filling Physiology,")
    canvas.drawCentredString(cx, sub_y - 15, "and Yield Prediction Dossier")

    # Divider line
    canvas.setStrokeColor(Color(0.18, 0.80, 0.44, alpha=0.6))
    canvas.line(cx - 25*mm, sub_y - 30, cx + 25*mm, sub_y - 30)

    # Author info
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(Color(1, 1, 1, alpha=0.4))
    auth_y = sub_y - 50
    canvas.drawCentredString(cx, auth_y, "R E P O R T   P R E P A R E D   B Y")

    canvas.setFont('Helvetica-Bold', 16)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(cx, auth_y - 20, "Sarthak Tiwary")

    canvas.setFont('Helvetica', 11)
    canvas.setFillColor(GREEN_ACCENT)
    canvas.drawCentredString(cx, auth_y - 38, "E X R N A - A G")

    # Date
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(Color(1, 1, 1, alpha=0.45))
    canvas.drawCentredString(cx, auth_y - 60, "February 2026")

    # Classification box
    class_y = auth_y - 85
    canvas.setStrokeColor(Color(0.75, 0.22, 0.17, alpha=0.3))
    canvas.line(cx - 40*mm, class_y + 10, cx + 40*mm, class_y + 10)

    canvas.setStrokeColor(LIGHT_RED)
    canvas.setLineWidth(1.5)
    canvas.setFillColor(Color(0, 0, 0, alpha=0))
    badge_w = 40*mm
    badge_h = 8*mm
    canvas.roundRect(cx - badge_w/2, class_y - badge_h/2, badge_w, badge_h, 2, fill=0, stroke=1)

    canvas.setFont('Helvetica-Bold', 9)
    canvas.setFillColor(LIGHT_RED)
    canvas.drawCentredString(cx, class_y - 2, "C O N F I D E N T I A L")

    canvas.setFont('Helvetica', 7)
    canvas.setFillColor(Color(1, 1, 1, alpha=0.35))
    canvas.drawCentredString(cx, class_y - 18, "This document contains proprietary research findings.")
    canvas.drawCentredString(cx, class_y - 28, "Unauthorized distribution is strictly prohibited.")

    canvas.restoreState()


# ============ MARKDOWN PARSER ============
def parse_markdown(md_text):
    """Parse markdown into reportlab flowables."""
    flowables = []
    lines = md_text.split('\n')
    i = 0
    in_code_block = False
    code_lines = []
    in_table = False
    table_rows = []

    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                code_text = '<br/>'.join(
                    l.replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;')
                    for l in code_lines
                )
                flowables.append(Paragraph(code_text, styles['CodeBlock']))
                code_lines = []
                in_code_block = False
            else:
                # Flush table if pending
                if in_table:
                    flowables.append(build_table(table_rows))
                    table_rows = []
                    in_table = False
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Table rows
        if '|' in line and line.strip().startswith('|'):
            stripped = line.strip()
            # Check if separator row
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                i += 1
                continue
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            if cells:
                if not in_table:
                    in_table = True
                table_rows.append(cells)
                i += 1
                continue

        # End of table
        if in_table and (not line.strip().startswith('|') or '|' not in line):
            flowables.append(build_table(table_rows))
            table_rows = []
            in_table = False

        # Empty line
        if not line.strip():
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ('---', '***', '___'):
            flowables.append(HRFlowable(
                width="100%", thickness=0.5, color=BORDER_GRAY,
                spaceBefore=8*mm, spaceAfter=8*mm
            ))
            i += 1
            continue

        # Headings
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            text = line.lstrip('#').strip()
            text = format_inline(text)

            if level == 1:
                flowables.append(PageBreak())
                flowables.append(Paragraph(text, styles['H1Custom']))
                flowables.append(HRFlowable(
                    width="100%", thickness=2, color=GREEN_ACCENT,
                    spaceBefore=0, spaceAfter=5*mm
                ))
            elif level == 2:
                conf_tag = ' <font size="6" color="#c0392b"><b>[CONFIDENTIAL]</b></font>'
                flowables.append(Paragraph(text + conf_tag, styles['H2Custom']))
                flowables.append(HRFlowable(
                    width="100%", thickness=1, color=BORDER_GRAY,
                    spaceBefore=0, spaceAfter=3*mm
                ))
            elif level == 3:
                flowables.append(Paragraph(text, styles['H3Custom']))
            elif level >= 4:
                flowables.append(Paragraph(text, styles['H4Custom']))
            i += 1
            continue

        # Blockquote
        if line.startswith('>'):
            quote_text = format_inline(line.lstrip('>').strip())
            flowables.append(Paragraph(quote_text, styles['BlockQuote']))
            i += 1
            continue

        # List items
        if re.match(r'^[\s]*[-*+]\s', line):
            text = re.sub(r'^[\s]*[-*+]\s', '', line)
            text = format_inline(text)
            flowables.append(Paragraph(f"&bull;&nbsp;&nbsp;{text}", styles['ListItem']))
            i += 1
            continue

        # Numbered list
        if re.match(r'^[\s]*\d+\.\s', line):
            m = re.match(r'^[\s]*(\d+)\.\s(.*)', line)
            if m:
                num, text = m.group(1), m.group(2)
                text = format_inline(text)
                flowables.append(Paragraph(f"<b>{num}.</b>&nbsp;&nbsp;{text}", styles['ListItem']))
            i += 1
            continue

        # Regular paragraph — collect consecutive lines
        para_lines = [line]
        while i + 1 < len(lines) and lines[i+1].strip() and \
              not lines[i+1].startswith('#') and \
              not lines[i+1].startswith('```') and \
              not lines[i+1].startswith('>') and \
              not lines[i+1].strip().startswith('|') and \
              not re.match(r'^[\s]*[-*+]\s', lines[i+1]) and \
              not re.match(r'^[\s]*\d+\.\s', lines[i+1]) and \
              not lines[i+1].strip() in ('---', '***', '___'):
            i += 1
            para_lines.append(lines[i])

        full_text = ' '.join(para_lines)
        full_text = format_inline(full_text)

        # First paragraph gets special classification box style
        if len(flowables) < 3 and ('Classification' in full_text or 'Evidence Level' in full_text):
            flowables.append(Paragraph(full_text, styles['ClassificationBox']))
        else:
            flowables.append(Paragraph(full_text, styles['BodyJustify']))

        i += 1

    # Flush remaining table
    if in_table and table_rows:
        flowables.append(build_table(table_rows))

    return flowables


def format_inline(text):
    """Convert markdown inline formatting to reportlab XML tags."""
    # Bold + italic
    text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<font face="Courier" size="8" color="#c0392b">\1</font>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<font color="#2980b9">\1</font>', text)
    # Arrows and special chars
    text = text.replace('→', '->')
    text = text.replace('↑', '^')
    text = text.replace('↓', 'v')
    text = text.replace('←', '<-')
    text = text.replace('≥', '>=')
    text = text.replace('≤', '<=')
    text = text.replace('±', '+/-')
    text = text.replace('×', 'x')
    text = text.replace('α', 'alpha')
    text = text.replace('β', 'beta')
    text = text.replace('μ', 'u')
    text = text.replace('°', 'deg')
    # Box-drawing chars (from ASCII diagrams)
    for ch in '╔╗╚╝╠╣║═┌┐└┘├┤│─┬┴┼':
        text = text.replace(ch, ' ')
    return text


def build_table(rows):
    """Build a reportlab Table from parsed rows."""
    if not rows:
        return Spacer(1, 0)

    # First row is header
    header = rows[0]
    data_rows = rows[1:] if len(rows) > 1 else []

    num_cols = len(header)

    # Build table data with Paragraph objects
    table_data = []
    header_cells = [Paragraph(format_inline(c), styles['TableHeader']) for c in header]
    table_data.append(header_cells)

    for row in data_rows:
        # Pad row if needed
        while len(row) < num_cols:
            row.append('')
        cells = [Paragraph(format_inline(c[:200]), styles['TableCell']) for c in row[:num_cols]]
        table_data.append(cells)

    # Calculate column widths
    available = 170*mm
    col_width = available / num_cols

    t = Table(table_data, colWidths=[col_width]*num_cols, repeatRows=1)

    style_cmds = [
        # Header
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 7.5),
        # Body
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        # Grid
        ('LINEBELOW', (0, 0), (-1, 0), 1, NAVY),
        ('LINEBELOW', (0, 1), (-1, -1), 0.5, HexColor('#e0e0e0')),
        # Padding
        ('TOPPADDING', (0, 0), (-1, -1), 2*mm),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2*mm),
        ('LEFTPADDING', (0, 0), (-1, -1), 2*mm),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2*mm),
        # Alignment
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]

    # Alternating row colors
    for row_idx in range(1, len(table_data)):
        if row_idx % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, row_idx), (-1, row_idx), TABLE_ALT))

    # Round top corners for header
    style_cmds.append(('ROUNDEDCORNERS', [3, 3, 0, 0]))

    t.setStyle(TableStyle(style_cmds))
    return t


# ============ BUILD DOCUMENT ============
def build_pdf():
    """Main PDF generation function."""
    print("Reading markdown report...")
    with open(REPORT_PATH, 'r') as f:
        md_content = f.read()

    print("Parsing markdown...")
    flowables = parse_markdown(md_content)

    print("Building PDF document...")

    # Create document
    doc = BaseDocTemplate(
        OUTPUT_PATH,
        pagesize=A4,
        leftMargin=20*mm,
        rightMargin=20*mm,
        topMargin=25*mm,
        bottomMargin=30*mm,
        title="ExRNA-Ag Maize MoA Confidential Report",
        author="Sarthak Tiwary",
        subject="Bacterial Extracellular tRF-Mediated Gene Regulation in Maize",
    )

    # Cover page template
    cover_frame = Frame(
        0, 0, A4[0], A4[1],
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        id='cover'
    )
    cover_template = PageTemplate(
        id='cover',
        frames=[cover_frame],
        onPage=build_cover_page,
    )

    # Content page template
    content_frame = Frame(
        20*mm, 30*mm,
        A4[0] - 40*mm, A4[1] - 55*mm,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        id='content'
    )
    content_template = PageTemplate(
        id='content',
        frames=[content_frame],
        onPage=header_footer,
    )

    doc.addPageTemplates([cover_template, content_template])

    # Build story: cover + content
    story = []

    # Cover page (empty spacer to trigger the page, then switch template)
    story.append(Spacer(1, 1))
    from reportlab.platypus.doctemplate import NextPageTemplate
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())

    # Add all parsed content
    story.extend(flowables)

    # Build
    doc.build(story)
    print(f"PDF generated successfully: {OUTPUT_PATH}")


if __name__ == '__main__':
    build_pdf()
