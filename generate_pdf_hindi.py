"""Generate a fancy PDF from the Hindi FINAL_REPORT with CONFIDENTIAL markings and Devanagari support."""

import markdown
from weasyprint import HTML, CSS
import os

REPORT_PATH = "ExRNA_Ag_Final_Report_CONFIDENTIAL_Long_Tomato_HINDI.md"
OUTPUT_PATH = "ExRNA_Ag_Final_Report_CONFIDENTIAL_Long_Tomato_HINDI.pdf"

# Read the markdown
with open(REPORT_PATH, "r", encoding="utf-8") as f:
    md_content = f.read()

# Strip the manual cover/header from the markdown (first ~17 lines before the first ---)
# We'll recreate it as a styled HTML cover page
lines = md_content.split("\n")
# Find the first "---" after the initial metadata block
first_hr = -1
for i, line in enumerate(lines):
    if line.strip() == "---" and i > 5:
        first_hr = i
        break

if first_hr > 0:
    # Keep everything after the first --- (the actual report body)
    body_md = "\n".join(lines[first_hr + 1:])
else:
    body_md = md_content

# Convert markdown to HTML
md_converter = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
body_html = md_converter.convert(body_md)

# Build full HTML document with Hindi cover page
html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<title>ExRNA-Ag गोपनीय प्रतिवेदन</title>
</head>
<body>

<!-- Cover Page -->
<div class="cover-page">
    <div class="cover-confidential">गोपनीय</div>
    <div class="cover-border">
        <div class="cover-content">
            <div class="cover-logo">ExRNA-Ag</div>
            <div class="cover-divider"></div>
            <h1 class="cover-title">बैक्टीरियल बाह्यकोशिकीय RNA-मध्यस्थित<br>पालक (<em>Spinacia oleracea</em>) बीज<br>अंकुरण का पुनर्क्रमादेशन</h1>
            <p class="cover-subtitle">लक्ष्य विश्लेषण, यांत्रिकी मॉडल, और सत्यापन रणनीति</p>
            <div class="cover-divider"></div>
            <div class="cover-meta">
                <p class="cover-author">प्रतिवेदन तैयारकर्ता</p>
                <p class="cover-name">Sarthak Tiwary</p>
                <p class="cover-org">ExRNA-Ag</p>
            </div>
            <div class="cover-date">फरवरी 2026</div>
            <div class="cover-classification">
                <span class="classification-badge">गोपनीय</span>
                <p class="classification-text">इस दस्तावेज़ में स्वामित्व अनुसंधान निष्कर्ष सम्मिलित हैं।<br>
                अनधिकृत वितरण सख्ती से निषिद्ध है।</p>
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

# CSS styling with Devanagari font support
css_content = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Serif+Devanagari:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

@page {
    size: A4;
    margin: 25mm 20mm 30mm 20mm;

    @top-left {
        content: "गोपनीय";
        font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
        font-size: 7pt;
        font-weight: 700;
        color: #c0392b;
        letter-spacing: 3pt;
        padding-top: 5mm;
    }

    @top-right {
        content: "ExRNA-Ag  |  Sarthak Tiwary";
        font-family: 'Inter', 'Noto Sans Devanagari', sans-serif;
        font-size: 7pt;
        font-weight: 400;
        color: #7f8c8d;
        padding-top: 5mm;
    }

    @bottom-center {
        content: "पृष्ठ " counter(page) " / " counter(pages);
        font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
        font-size: 7pt;
        color: #95a5a6;
    }

    @bottom-left {
        content: "गोपनीय  --  वितरण निषिद्ध";
        font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
        font-size: 6.5pt;
        font-weight: 600;
        color: #c0392b;
        letter-spacing: 1pt;
    }

    @bottom-right {
        content: "फरवरी 2026";
        font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
        font-size: 7pt;
        color: #95a5a6;
    }
}

@page :first {
    margin: 0;
    @top-left { content: none; }
    @top-right { content: none; }
    @bottom-center { content: none; }
    @bottom-left { content: none; }
    @bottom-right { content: none; }
}

/* ============ GLOBAL ============ */
* {
    box-sizing: border-box;
}

body {
    font-family: 'Noto Serif Devanagari', 'Noto Sans Devanagari', 'Source Serif 4', Georgia, serif;
    font-size: 10pt;
    line-height: 1.75;
    color: #1a1a2e;
    -webkit-font-smoothing: antialiased;
}

/* ============ COVER PAGE ============ */
.cover-page {
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
}

.cover-confidential {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-35deg);
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 80pt;
    font-weight: 800;
    color: rgba(192, 57, 43, 0.06);
    letter-spacing: 15pt;
    white-space: nowrap;
    z-index: 0;
    user-select: none;
}

.cover-border {
    width: 170mm;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 4px;
    padding: 3mm;
    z-index: 1;
}

.cover-content {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 2px;
    padding: 15mm 12mm;
    text-align: center;
}

.cover-logo {
    font-family: 'Inter', sans-serif;
    font-size: 14pt;
    font-weight: 300;
    letter-spacing: 12pt;
    color: rgba(255, 255, 255, 0.5);
    text-transform: uppercase;
    margin-bottom: 8mm;
}

.cover-divider {
    width: 50mm;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(46, 204, 113, 0.6), transparent);
    margin: 6mm auto;
}

.cover-title {
    font-family: 'Noto Serif Devanagari', Georgia, serif;
    font-size: 18pt;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.5;
    margin: 6mm 0;
    letter-spacing: 0.2pt;
}

.cover-subtitle {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 10.5pt;
    font-weight: 400;
    color: rgba(255, 255, 255, 0.65);
    margin: 4mm 0 8mm 0;
    letter-spacing: 0.5pt;
}

.cover-meta {
    margin: 10mm 0 6mm 0;
}

.cover-author {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 8pt;
    font-weight: 400;
    color: rgba(255, 255, 255, 0.4);
    text-transform: uppercase;
    letter-spacing: 3pt;
    margin-bottom: 2mm;
}

.cover-name {
    font-family: 'Inter', sans-serif;
    font-size: 16pt;
    font-weight: 600;
    color: #ffffff;
    margin: 2mm 0;
}

.cover-org {
    font-family: 'Inter', sans-serif;
    font-size: 11pt;
    font-weight: 400;
    color: #2ecc71;
    letter-spacing: 2pt;
}

.cover-date {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 9pt;
    color: rgba(255, 255, 255, 0.45);
    margin: 6mm 0;
}

.cover-classification {
    margin-top: 8mm;
    padding-top: 5mm;
    border-top: 1px solid rgba(192, 57, 43, 0.3);
}

.classification-badge {
    display: inline-block;
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 9pt;
    font-weight: 700;
    color: #e74c3c;
    letter-spacing: 5pt;
    border: 1.5px solid #e74c3c;
    padding: 2mm 6mm;
    border-radius: 2px;
}

.classification-text {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 7.5pt;
    color: rgba(255, 255, 255, 0.35);
    margin-top: 3mm;
    line-height: 1.7;
}

/* ============ REPORT BODY ============ */
.report-body {
    padding: 0;
}

/* Watermark on every page */
.report-body::before {
    content: "गोपनीय";
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(-40deg);
    font-family: 'Noto Sans Devanagari', sans-serif;
    font-size: 72pt;
    font-weight: 800;
    color: rgba(192, 57, 43, 0.035);
    letter-spacing: 10pt;
    white-space: nowrap;
    z-index: -1;
    pointer-events: none;
}

/* ============ HEADINGS ============ */
h1 {
    font-family: 'Noto Serif Devanagari', Georgia, serif;
    font-size: 20pt;
    font-weight: 700;
    color: #0c1929;
    margin-top: 12mm;
    margin-bottom: 5mm;
    line-height: 1.4;
    page-break-after: avoid;
    border-bottom: 2.5px solid #2ecc71;
    padding-bottom: 3mm;
}

h2 {
    font-family: 'Noto Serif Devanagari', Georgia, serif;
    font-size: 14pt;
    font-weight: 700;
    color: #1a2744;
    margin-top: 10mm;
    margin-bottom: 4mm;
    page-break-after: avoid;
    border-bottom: 1.5px solid #bdc3c7;
    padding-bottom: 2mm;
    line-height: 1.5;
}

h3 {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 11.5pt;
    font-weight: 600;
    color: #243b5e;
    margin-top: 7mm;
    margin-bottom: 3mm;
    page-break-after: avoid;
    line-height: 1.5;
}

h4 {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 10.5pt;
    font-weight: 600;
    color: #34495e;
    margin-top: 5mm;
    margin-bottom: 2mm;
    page-break-after: avoid;
    line-height: 1.5;
}

/* ============ PARAGRAPHS ============ */
p {
    margin: 0 0 3mm 0;
    text-align: justify;
    hyphens: auto;
    orphans: 3;
    widows: 3;
}

/* ============ STRONG / EM ============ */
strong {
    font-weight: 700;
    color: #0c1929;
}

em {
    font-style: italic;
}

/* ============ LISTS ============ */
ul, ol {
    margin: 2mm 0 4mm 0;
    padding-left: 6mm;
}

li {
    margin-bottom: 1.5mm;
    line-height: 1.7;
}

/* ============ TABLES ============ */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 8pt;
    line-height: 1.5;
    page-break-inside: auto;
}

thead {
    display: table-header-group;
}

tr {
    page-break-inside: avoid;
}

th {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-weight: 600;
    font-size: 7pt;
    color: #ffffff;
    background: linear-gradient(135deg, #1a2744, #243b5e);
    padding: 2.5mm 2.5mm;
    text-align: left;
    border: none;
}

th:first-child {
    border-radius: 3px 0 0 0;
}

th:last-child {
    border-radius: 0 3px 0 0;
}

td {
    padding: 2mm 2.5mm;
    border-bottom: 0.5px solid #e0e0e0;
    vertical-align: top;
    font-size: 7.5pt;
}

tr:nth-child(even) td {
    background-color: #f8f9fa;
}

tr:hover td {
    background-color: #eef5f0;
}

/* ============ CODE / INLINE CODE ============ */
code {
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    font-size: 8.5pt;
    background: #f4f6f9;
    padding: 0.5mm 1.5mm;
    border-radius: 2px;
    color: #c0392b;
}

pre {
    background: #1a1a2e;
    color: #ecf0f1;
    padding: 4mm 5mm;
    border-radius: 4px;
    font-family: 'JetBrains Mono', 'Consolas', monospace;
    font-size: 8pt;
    line-height: 1.55;
    overflow-x: auto;
    margin: 3mm 0 5mm 0;
    border-left: 3px solid #2ecc71;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
    font-size: 8pt;
}

/* ============ BLOCKQUOTES ============ */
blockquote {
    border-left: 3px solid #3498db;
    background: #eaf2f8;
    padding: 3mm 4mm;
    margin: 3mm 0 4mm 0;
    font-size: 9.5pt;
    border-radius: 0 3px 3px 0;
}

/* ============ HORIZONTAL RULES ============ */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #bdc3c7, transparent);
    margin: 8mm 0;
}

/* ============ LINKS ============ */
a {
    color: #2980b9;
    text-decoration: none;
}

/* ============ SPECIAL CALLOUTS ============ */
.report-body > p:first-of-type {
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 8.5pt;
    color: #7f8c8d;
    border: 1px solid #ddd;
    padding: 3mm 4mm;
    border-radius: 3px;
    background: #fafbfc;
}

/* ============ BIBLIOGRAPHY ============ */
.report-body > p:last-child,
.report-body p[id*="ref"],
.report-body p:nth-last-child(-n+70) {
    font-size: 7.5pt;
    line-height: 1.5;
    text-indent: -5mm;
    padding-left: 5mm;
    margin-bottom: 1.5mm;
}

/* ============ PAGE BREAKS ============ */
h1 {
    page-break-before: always;
}

h1:first-of-type {
    page-break-before: avoid;
}

/* ============ CONFIDENTIAL STAMP PER SECTION ============ */
h2::after {
    content: " [गोपनीय]";
    font-family: 'Noto Sans Devanagari', 'Inter', sans-serif;
    font-size: 6pt;
    font-weight: 700;
    color: #c0392b;
    letter-spacing: 1pt;
    vertical-align: super;
    margin-left: 3mm;
}
"""

# Generate PDF
print("Generating Hindi PDF...")
html_doc = HTML(string=html_content, base_url=os.getcwd())
css_doc = CSS(string=css_content)
html_doc.write_pdf(OUTPUT_PATH, stylesheets=[css_doc])
print(f"PDF generated: {OUTPUT_PATH}")
