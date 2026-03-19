import os
import markdown

def save_document_report(report_text):

    os.makedirs("output", exist_ok=True)

    # Save Markdown
    md_path = "output/final_report.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    # Convert to HTML with basic styling
    html_content = markdown.markdown(report_text)

    styled_html = f"""
    <html>
    <head>
        <title>Document Analysis Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
            }}
            h1 {{
                color: #2c3e50;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 1px solid #ccc;
                padding-bottom: 5px;
            }}
            p {{
                margin: 10px 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    html_path = "output/final_report.html"

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(styled_html)

    print("Report saved successfully.")
    print(f"Markdown: {md_path}")
    print(f"HTML: {html_path}")