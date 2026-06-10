---
name: report-generator
description: Produces PDF and JSON reports from project artifacts, audits, and data.
version: 1.0.0
author: FutureReady Team
tags: [reporting, pdf, json, automation]
---

# Report Generator

## Trigger
Receives request for report generation with data source and template specification.

## Goal
Produce beautiful, branded PDF reports and structured JSON exports from any project data.

## Inputs
- Report template specification
- Data source (API response, database query, CSV, JSON)
- Brand assets (logo, colors, fonts)
- Optional: previous report for comparison

## Outputs
1. `reports/outputs/*.pdf` — Generated PDF reports
2. `reports/outputs/*.json` — Structured data exports
3. `reports/templates/*.html` — HTML/CSS templates for PDF generation
4. `reports/templates/*.md` — Markdown templates
5. `backend/app/services/reporting.py` — Report generation service

## Workflow

1. **Define Report Schema**
   - Report metadata (title, date, author, version)
   - Section structure with data bindings
   - Chart/visualization specifications
   - Page layout (A4, Letter, landscape)

2. **Fetch Data**
   - API calls with authentication
   - SQL queries with parameterization
   - File parsing (CSV, Excel, JSON)
   - Data transformation and aggregation

3. **Render Template**
   - HTML templates with Jinja2
   - CSS styling with @page rules
   - Dynamic charts (matplotlib, plotly, or Chart.js via puppeteer)
   - Conditional sections based on data

4. **Generate PDF**
   - WeasyPrint (pure Python, good for simple reports)
   - Playwright + Paged.js (best for complex layouts)
   - Gotenberg (Dockerized Chrome, production-ready)
   - Add headers, footers, page numbers, TOC

5. **Generate JSON**
   - Structured export matching report schema
   - Include metadata and data provenance
   - Pretty-printed or minified

6. **Deliver**
   - S3 presigned URL
   - Email attachment via AgentMail
   - API download endpoint
   - Webhook callback

## Validation Checklist
- [ ] PDF renders correctly on all target page sizes
- [ ] JSON schema validates against expected structure
- [ ] Charts are legible at print resolution
- [ ] Accessibility: alt text for images, tagged PDF structure
- [ ] File size under 10MB for email delivery

## Prompt Library

### generate-report-template
```
Given this report specification:
{{spec}}

Generate an HTML template with:
1. Cover page with logo, title, date
2. Table of contents
3. Executive summary section
4. Data tables with zebra striping
5. Chart placeholders (bar, line, pie)
6. Footer with page numbers and confidentiality notice

Use CSS @page rules for print layout.
```

### generate-pdf-from-data
```
Given this data:
{{data}}

And this template:
{{template}}

Generate a PDF using WeasyPrint with:
- Proper page breaks
- Table overflow handling
- Image embedding
- Custom fonts

Return the PDF as base64 or save to path.
```

### generate-json-export
```
Given this database query result:
{{query_result}}

Generate a structured JSON export with:
1. Metadata block (generated_at, source, version)
2. Data array with typed fields
3. Summary statistics
4. Pagination info if applicable

Schema should match: {{json_schema}}
```
