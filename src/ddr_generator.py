from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def save_ddr_report(report_text):

    os.makedirs("output", exist_ok=True)

    file_path = "output/final_ddr.pdf"

    c = canvas.Canvas(file_path, pagesize=A4)

    y = 800

    for line in report_text.split("\n"):

        c.drawString(50, y, line[:100])

        y -= 15

        if y < 50:
            c.showPage()
            y = 800

    c.save()

    print("DDR report saved:", file_path)