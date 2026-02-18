"""Generate a fancy PDF from the Maize MoA Report with CONFIDENTIAL markings.
Uses weasyprint with preloaded pango libraries."""

import ctypes
import os

# Preload pango/cairo libraries from extracted debs
_lp = '/tmp/pango_libs/usr/lib/x86_64-linux-gnu'
for _lib in ['libfribidi.so.0','libthai.so.0','libgraphite2.so.3','libharfbuzz.so.0',
             'libpango-1.0.so.0','libpangoft2-1.0.so.0','libcairo.so.2',
             'libpangocairo-1.0.so.0','libgdk_pixbuf-2.0.so.0']:
    try:
        ctypes.cdll.LoadLibrary(os.path.join(_lp, _lib))
    except OSError:
        pass

import markdown
from weasyprint import HTML, CSS

REPORT_PATH = "ExRNA_Maize_MoA_Report.md"
OUTPUT_PATH = "ExRNA_Ag_Final_Report_CONFIDENTIAL_Long_Maize.pdf"
COVER_TITLE = "Bacterial Extracellular tRF-Mediated Gene Regulation in Maize (<em>Zea mays</em> L.)"
COVER_SUBTITLE = "Mechanistic Mode of Action, Grain-Filling Physiology, and Yield Prediction Dossier"

# Read the markdown
with open(REPORT_PATH, "r") as f:
    md_content = f.read()

# Convert markdown to HTML
md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
body_html = md.convert(md_content)

# Build full HTML document
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>ExRNA-Ag Maize tRF MoA Dossier - Confidential</title>
</head>
<body>

<!-- Cover Page -->
<div class="cover-page">
    <div class="cover-confidential">CONFIDENTIAL</div>
    <div class="cover-border">
        <div class="cover-content">
            <div class="cover-logo">ExRNA-Ag</div>
            <div class="cover-divider"></div>
            <h1 class="cover-title">{COVER_TITLE}</h1>
            <p class="cover-subtitle">{COVER_SUBTITLE}</p>
            <div class="cover-divider"></div>
            <div class="cover-meta">
                <p class="cover-author">Report prepared by</p>
                <p class="cover-name">Sarthak Tiwary</p>
                <p class="cover-org">ExRNA-Ag</p>
            </div>
            <div class="cover-date">February 2026</div>
            <div class="cover-classification">
                <span class="classification-badge">CONFIDENTIAL</span>
                <p class="classification-text">This document contains proprietary research findings.<br>
                Unauthorized distribution is strictly prohibited.</p>
            </div>
        </div>
    </div>
</div>

<!-- Report Body -->
<div class="report-body">
{body_html}
</div>

</body>
</html>
"""

# CSS styling — matches existing reports for brand consistency
css_content = """
@page {{
    size: A4;
    margin: 25mm 20mm 30mm 20mm;

    @top-left {{
        content: "CONFIDENTIAL";
        font-family: 'Helvetica Neue', 'Inter', sans-serif;
        font-size: 7pt;
        font-weight: 700;
        color: #c0392b;
        letter-spacing: 3pt;
        padding-top: 5mm;
    }}

    @top-right {{
        content: "ExRNA-Ag  |  Maize tRF MoA Dossier  |  Sarthak Tiwary";
        font-family: 'Helvetica Neue', 'Inter', sans-serif;
        font-size: 7pt;
        font-weight: 400;
        color: #7f8c8d;
        padding-top: 5mm;
    }}

    @bottom-center {{
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', 'Inter', sans-serif;
        font-size: 7pt;
        color: #95a5a6;
    }}

    @bottom-left {{
        content: "CONFIDENTIAL  --  Do Not Distribute";
        font-family: 'Helvetica Neue', 'Inter', sans-serif;
        font-size: 6.5pt;
        font-weight: 600;
        color: #c0392b;
        letter-spacing: 1pt;
    }}

    @bottom-right {{
        content: "February 2026";
        font-family: 'Helvetica Neue', 'Inter', sans-serif;
        font-size: 7pt;
        color: #95a5a6;
    }}
}}

@page :first {{
    margin: 0;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-center {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

/* ============ GLOBAL ============ */
* {{
    box-sizing: border-box;
}}

body {{
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 10pt;
    line-height: 1.65;
    color: #1a1a2e;
}}

/* ============ COVER PAGE ============ */
.cover-page {{
    page: cover;
    width: 210mm;
    height: 297mm;
    position: relative;
    background: linear-gradient(160deg, #0c1929 0%, #1a2744 40%, #243b5e 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    page-break-after: always;
    overflow: hidden;
}}

.cover-confidential {{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-35deg);
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 90pt;
    font-weight: 800;
    color: rgba(192, 57, 43, 0.06);
    letter-spacing: 20pt;
    white-space: nowrap;
    z-index: 0;
    user-select: none;
}}

.cover-border {{
    width: 170mm;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 4px;
    padding: 3mm;
    z-index: 1;
}}

.cover-content {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 2px;
    padding: 15mm 12mm;
    text-align: center;
}}

.cover-logo {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14pt;
    font-weight: 300;
    letter-spacing: 12pt;
    color: rgba(255, 255, 255, 0.5);
    text-transform: uppercase;
    margin-bottom: 8mm;
}}

.cover-divider {{
    width: 50mm;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(46, 204, 113, 0.6), transparent);
    margin: 6mm auto;
}}

.cover-title {{
    font-family: 'Georgia', serif;
    font-size: 20pt;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.35;
    margin: 6mm 0;
    letter-spacing: 0.2pt;
}}

.cover-subtitle {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 11pt;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.65);
    margin: 4mm 0 8mm 0;
    letter-spacing: 1pt;
}}

.cover-meta {{
    margin: 10mm 0 6mm 0;
}}

.cover-author {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 8pt;
    font-weight: 400;
    color: rgba(255, 255, 255, 0.4);
    text-transform: uppercase;
    letter-spacing: 3pt;
    margin-bottom: 2mm;
}}

.cover-name {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 16pt;
    font-weight: 600;
    color: #ffffff;
    margin: 2mm 0;
}}

.cover-org {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 11pt;
    font-weight: 400;
    color: #2ecc71;
    letter-spacing: 2pt;
}}

.cover-date {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 9pt;
    color: rgba(255, 255, 255, 0.45);
    margin: 6mm 0;
}}

.cover-classification {{
    margin-top: 8mm;
    padding-top: 5mm;
    border-top: 1px solid rgba(192, 57, 43, 0.3);
}}

.classification-badge {{
    display: inline-block;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 9pt;
    font-weight: 700;
    color: #e74c3c;
    letter-spacing: 5pt;
    border: 1.5px solid #e74c3c;
    padding: 2mm 6mm;
    border-radius: 2px;
}}

.classification-text {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 7pt;
    color: rgba(255, 255, 255, 0.35);
    margin-top: 3mm;
    line-height: 1.6;
}}

/* ============ REPORT BODY ============ */
.report-body {{
    padding: 0;
}}

/* Watermark on every page */
.report-body::before {{
    content: "CONFIDENTIAL";
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-40deg);
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 72pt;
    font-weight: 800;
    color: rgba(192, 57, 43, 0.035);
    letter-spacing: 15pt;
    white-space: nowrap;
    z-index: -1;
    pointer-events: none;
}}

/* ============ HEADINGS ============ */
h1 {{
    font-family: 'Georgia', serif;
    font-size: 22pt;
    font-weight: 700;
    color: #0c1929;
    margin-top: 12mm;
    margin-bottom: 5mm;
    line-height: 1.25;
    page-break-after: avoid;
    border-bottom: 2.5px solid #2ecc71;
    padding-bottom: 3mm;
}}

h2 {{
    font-family: 'Georgia', serif;
    font-size: 15pt;
    font-weight: 700;
    color: #1a2744;
    margin-top: 10mm;
    margin-bottom: 4mm;
    page-break-after: avoid;
    border-bottom: 1.5px solid #bdc3c7;
    padding-bottom: 2mm;
}}

h3 {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 12pt;
    font-weight: 600;
    color: #243b5e;
    margin-top: 7mm;
    margin-bottom: 3mm;
    page-break-after: avoid;
}}

h4 {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 10.5pt;
    font-weight: 600;
    color: #34495e;
    margin-top: 5mm;
    margin-bottom: 2mm;
    page-break-after: avoid;
}}

/* ============ PARAGRAPHS ============ */
p {{
    margin: 0 0 3mm 0;
    text-align: justify;
    hyphens: auto;
    orphans: 3;
    widows: 3;
}}

/* ============ STRONG / EM ============ */
strong {{
    font-weight: 700;
    color: #0c1929;
}}

em {{
    font-style: italic;
}}

/* ============ LISTS ============ */
ul, ol {{
    margin: 2mm 0 4mm 0;
    padding-left: 6mm;
}}

li {{
    margin-bottom: 1.5mm;
}}

/* ============ TABLES ============ */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 8.5pt;
    line-height: 1.45;
    page-break-inside: auto;
}}

thead {{
    display: table-header-group;
}}

tr {{
    page-break-inside: avoid;
}}

th {{
    font-family: 'Helvetica Neue', sans-serif;
    font-weight: 600;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
    color: #ffffff;
    background: linear-gradient(135deg, #1a2744, #243b5e);
    padding: 2.5mm 3mm;
    text-align: left;
    border: none;
}}

th:first-child {{
    border-radius: 3px 0 0 0;
}}

th:last-child {{
    border-radius: 0 3px 0 0;
}}

td {{
    padding: 2mm 3mm;
    border-bottom: 0.5px solid #e0e0e0;
    vertical-align: top;
}}

tr:nth-child(even) td {{
    background-color: #f8f9fa;
}}

tr:hover td {{
    background-color: #eef5f0;
}}

/* ============ CODE BLOCKS ============ */
code {{
    font-family: 'Courier New', 'Consolas', monospace;
    font-size: 8.5pt;
    background: #f4f6f9;
    padding: 0.5mm 1.5mm;
    border-radius: 2px;
    color: #c0392b;
}}

pre {{
    background: #1a1a2e;
    color: #ecf0f1;
    padding: 4mm 5mm;
    border-radius: 4px;
    font-family: 'Courier New', 'Consolas', monospace;
    font-size: 8pt;
    line-height: 1.55;
    overflow-x: auto;
    margin: 3mm 0 5mm 0;
    border-left: 3px solid #2ecc71;
}}

pre code {{
    background: none;
    color: inherit;
    padding: 0;
    font-size: 8pt;
}}

/* ============ BLOCKQUOTES (Evidence labels) ============ */
blockquote {{
    border-left: 3px solid #3498db;
    background: #eaf2f8;
    padding: 3mm 4mm;
    margin: 3mm 0 4mm 0;
    font-size: 9.5pt;
    border-radius: 0 3px 3px 0;
}}

/* ============ HORIZONTAL RULES ============ */
hr {{
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #bdc3c7, transparent);
    margin: 8mm 0;
}}

/* ============ LINKS ============ */
a {{
    color: #2980b9;
    text-decoration: none;
}}

/* ============ SPECIAL CALLOUTS ============ */
.report-body > p:first-of-type {{
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 8.5pt;
    color: #7f8c8d;
    border: 1px solid #ddd;
    padding: 3mm 4mm;
    border-radius: 3px;
    background: #fafbfc;
}}

/* ============ PAGE BREAKS ============ */
h1 {{
    page-break-before: always;
}}

h1:first-of-type {{
    page-break-before: avoid;
}}

/* ============ CONFIDENTIAL STAMP PER SECTION ============ */
h2::after {{
    content: " [CONFIDENTIAL]";
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 6pt;
    font-weight: 700;
    color: #c0392b;
    letter-spacing: 1.5pt;
    vertical-align: super;
    margin-left: 3mm;
}}
"""

# Generate PDF
print("Generating Maize tRF MoA Dossier PDF...")
html_doc = HTML(string=html_content, base_url=os.getcwd())
css_doc = CSS(string=css_content)
html_doc.write_pdf(OUTPUT_PATH, stylesheets=[css_doc])
print(f"PDF generated: {OUTPUT_PATH}")
print(f"File size: {os.path.getsize(OUTPUT_PATH) / 1024:.0f} KB")
