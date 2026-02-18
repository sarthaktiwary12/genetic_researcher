#!/usr/bin/env python3
"""Generate CONFIDENTIAL PDFs from all crop reports and cross-crop analysis.

Uses WeasyPrint with the same dark-blue/green CONFIDENTIAL styling
as the original ExRNA reports.
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import json

REPORTS_DIR = Path("reports")
CROPS_DIR = Path("crops")
OUTPUT_DIR = Path("reports/pdf")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Crop display info
CROP_INFO = {
    "spinach": ("Spinacia oleracea", "Spinach"),
    "broccoli": ("Brassica oleracea var. italica", "Broccoli"),
    "wheat": ("Triticum aestivum", "Wheat"),
    "quinoa": ("Chenopodium quinoa", "Quinoa"),
    "soybean": ("Glycine max", "Soybean"),
    "maize": ("Zea mays", "Maize"),
    "tomato": ("Solanum lycopersicum", "Tomato"),
}

CSS_CONTENT = """
@page {
    size: A4;
    margin: 25mm 20mm 30mm 20mm;

    @top-left {
        content: "CONFIDENTIAL";
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
        font-size: 7pt;
        font-weight: 700;
        color: #c0392b;
        letter-spacing: 3pt;
        padding-top: 5mm;
    }

    @top-right {
        content: "ExRNA-Ag  |  Sarthak Tiwary";
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
        font-size: 7pt;
        font-weight: 400;
        color: #7f8c8d;
        padding-top: 5mm;
    }

    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
        font-size: 7pt;
        color: #95a5a6;
    }

    @bottom-left {
        content: "CONFIDENTIAL  --  Do Not Distribute";
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
        font-size: 6.5pt;
        font-weight: 600;
        color: #c0392b;
        letter-spacing: 1pt;
    }

    @bottom-right {
        content: "February 2026";
        font-family: 'Helvetica Neue', 'Arial', sans-serif;
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

* { box-sizing: border-box; }

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 10pt;
    line-height: 1.65;
    color: #1a1a2e;
}

/* ============ COVER PAGE ============ */
.cover-page {
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
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 90pt;
    font-weight: 800;
    color: rgba(192, 57, 43, 0.06);
    letter-spacing: 20pt;
    white-space: nowrap;
    z-index: 0;
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
    font-family: 'Helvetica Neue', sans-serif;
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
    font-family: 'Georgia', serif;
    font-size: 20pt;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.35;
    margin: 6mm 0;
}

.cover-subtitle {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 11pt;
    font-weight: 300;
    color: rgba(255, 255, 255, 0.65);
    margin: 4mm 0 8mm 0;
    letter-spacing: 1pt;
}

.cover-meta { margin: 10mm 0 6mm 0; }

.cover-author {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 8pt;
    color: rgba(255, 255, 255, 0.4);
    text-transform: uppercase;
    letter-spacing: 3pt;
    margin-bottom: 2mm;
}

.cover-name {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 16pt;
    font-weight: 600;
    color: #ffffff;
    margin: 2mm 0;
}

.cover-org {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 11pt;
    color: #2ecc71;
    letter-spacing: 2pt;
}

.cover-date {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 9pt;
    color: rgba(255, 255, 255, 0.45);
    margin: 6mm 0;
}

.classification-badge {
    display: inline-block;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 9pt;
    font-weight: 700;
    color: #e74c3c;
    letter-spacing: 5pt;
    border: 1.5px solid #e74c3c;
    padding: 2mm 6mm;
    border-radius: 2px;
}

.classification-text {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 7pt;
    color: rgba(255, 255, 255, 0.35);
    margin-top: 3mm;
    line-height: 1.6;
}

.cover-classification {
    margin-top: 8mm;
    padding-top: 5mm;
    border-top: 1px solid rgba(192, 57, 43, 0.3);
}

/* ============ REPORT BODY ============ */
.report-body { padding: 0; }

.report-body::before {
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
}

/* ============ HEADINGS ============ */
h1 {
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
    page-break-before: always;
}

h1:first-of-type { page-break-before: avoid; }

h2 {
    font-family: 'Georgia', serif;
    font-size: 15pt;
    font-weight: 700;
    color: #1a2744;
    margin-top: 10mm;
    margin-bottom: 4mm;
    page-break-after: avoid;
    border-bottom: 1.5px solid #bdc3c7;
    padding-bottom: 2mm;
}

h2::after {
    content: " [CONFIDENTIAL]";
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 6pt;
    font-weight: 700;
    color: #c0392b;
    letter-spacing: 1.5pt;
    vertical-align: super;
    margin-left: 3mm;
}

h3 {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 12pt;
    font-weight: 600;
    color: #243b5e;
    margin-top: 7mm;
    margin-bottom: 3mm;
    page-break-after: avoid;
}

h4 {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 10.5pt;
    font-weight: 600;
    color: #34495e;
    margin-top: 5mm;
    margin-bottom: 2mm;
}

/* ============ TEXT ============ */
p {
    margin: 0 0 3mm 0;
    text-align: justify;
    hyphens: auto;
    orphans: 3;
    widows: 3;
}

strong { font-weight: 700; color: #0c1929; }

ul, ol { margin: 2mm 0 4mm 0; padding-left: 6mm; }
li { margin-bottom: 1.5mm; }

/* ============ TABLES ============ */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 8.5pt;
    line-height: 1.45;
}

thead { display: table-header-group; }
tr { page-break-inside: avoid; }

th {
    font-family: 'Helvetica Neue', sans-serif;
    font-weight: 600;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
    color: #ffffff;
    background: linear-gradient(135deg, #1a2744, #243b5e);
    padding: 2.5mm 3mm;
    text-align: left;
}

th:first-child { border-radius: 3px 0 0 0; }
th:last-child { border-radius: 0 3px 0 0; }

td {
    padding: 2mm 3mm;
    border-bottom: 0.5px solid #e0e0e0;
    vertical-align: top;
}

tr:nth-child(even) td { background-color: #f8f9fa; }

/* ============ CODE ============ */
code {
    font-family: 'Consolas', monospace;
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
    font-size: 8pt;
    line-height: 1.55;
    margin: 3mm 0 5mm 0;
    border-left: 3px solid #2ecc71;
}

pre code { background: none; color: inherit; padding: 0; }

/* ============ BLOCKQUOTES ============ */
blockquote {
    border-left: 3px solid #3498db;
    background: #eaf2f8;
    padding: 3mm 4mm;
    margin: 3mm 0 4mm 0;
    font-size: 9.5pt;
    border-radius: 0 3px 3px 0;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #bdc3c7, transparent);
    margin: 8mm 0;
}

a { color: #2980b9; text-decoration: none; }
"""


def build_cover_html(crop: str, species: str, common_name: str, target_count: int) -> str:
    """Build the cover page HTML."""
    return f"""
    <div class="cover-page">
        <div class="cover-confidential">CONFIDENTIAL</div>
        <div class="cover-border">
            <div class="cover-content">
                <div class="cover-logo">ExRNA-Ag</div>
                <div class="cover-divider"></div>
                <h1 class="cover-title">Bacterial Extracellular RNA-Mediated<br>
                Reprogramming of {common_name}<br>
                (<em>{species}</em>) Seed Germination</h1>
                <p class="cover-subtitle">Target Analysis &middot; Mechanistic Models &middot; Validation Strategy</p>
                <div class="cover-divider"></div>
                <p class="cover-subtitle">{target_count} Gene Targets Analyzed</p>
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
    """


def generate_pdf(md_path: Path, output_path: Path, crop: str):
    """Generate a PDF from a markdown report."""
    md_content = md_path.read_text(encoding="utf-8")

    species, common_name = CROP_INFO.get(crop, (crop, crop.title()))

    # Get target count
    target_count = 0
    config_path = CROPS_DIR / crop / "targets_config.json"
    if config_path.exists():
        data = json.loads(config_path.read_text())
        target_count = len(data.get("targets", []))

    # Convert markdown to HTML
    md_converter = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    body_html = md_converter.convert(md_content)

    cover_html = build_cover_html(crop, species, common_name, target_count)

    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8"><title>ExRNA-Ag {common_name} Report</title></head>
    <body>
    {cover_html}
    <div class="report-body">
    {body_html}
    </div>
    </body>
    </html>
    """

    html_doc = HTML(string=html_content)
    css_doc = CSS(string=CSS_CONTENT)
    html_doc.write_pdf(str(output_path), stylesheets=[css_doc])
    print(f"  PDF: {output_path}")


def generate_cross_crop_pdf(md_path: Path, output_path: Path):
    """Generate the cross-crop analysis PDF."""
    md_content = md_path.read_text(encoding="utf-8")

    md_converter = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
    body_html = md_converter.convert(md_content)

    cover_html = f"""
    <div class="cover-page">
        <div class="cover-confidential">CONFIDENTIAL</div>
        <div class="cover-border">
            <div class="cover-content">
                <div class="cover-logo">ExRNA-Ag</div>
                <div class="cover-divider"></div>
                <h1 class="cover-title">Cross-Crop Commonalities in<br>
                Bacterial Extracellular RNA-Mediated<br>
                Germination Enhancement</h1>
                <p class="cover-subtitle">Conserved Mechanisms Across 6 Crop Species</p>
                <div class="cover-divider"></div>
                <p class="cover-subtitle">Spinach &middot; Broccoli &middot; Wheat &middot; Quinoa &middot; Soybean &middot; Maize</p>
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
    """

    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head><meta charset="UTF-8"><title>ExRNA-Ag Cross-Crop Analysis</title></head>
    <body>
    {cover_html}
    <div class="report-body">
    {body_html}
    </div>
    </body>
    </html>
    """

    html_doc = HTML(string=html_content)
    css_doc = CSS(string=CSS_CONTENT)
    html_doc.write_pdf(str(output_path), stylesheets=[css_doc])
    print(f"  PDF: {output_path}")


def main():
    crops = ["spinach", "broccoli", "wheat", "quinoa", "soybean", "maize"]

    print("=" * 60)
    print("GENERATING CONFIDENTIAL PDFs")
    print("=" * 60)

    for crop in crops:
        md_path = REPORTS_DIR / f"{crop}_report.md"
        if not md_path.exists():
            print(f"  SKIP: {md_path} not found")
            continue
        output = OUTPUT_DIR / f"Bacterial_sRNA_Seed_Germination_{crop.title()}_Analysis.pdf"
        generate_pdf(md_path, output, crop)

    # Cross-crop
    cross_md = REPORTS_DIR / "cross_crop_commonalities.md"
    if cross_md.exists():
        output = OUTPUT_DIR / "Bacterial_sRNA_Cross_Crop_Conserved_Mechanisms.pdf"
        generate_cross_crop_pdf(cross_md, output)

    print(f"\nAll PDFs generated in {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
