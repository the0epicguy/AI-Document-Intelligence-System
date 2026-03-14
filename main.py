from src.pdf_parser import extract_pdf_content
from src.llm_analyzer import generate_ddr_report
from src.ddr_generator import save_ddr_report


def main():

    print("Starting DDR generation system...\n")

    inspection_path = "data/Sample Report.pdf"
    thermal_path = "data/Thermal Images.pdf"

    print("Step 1: Extracting text and images from PDFs...")

    inspection_text, inspection_images = extract_pdf_content(
        inspection_path, "output/inspection_images"
    )

    thermal_text, thermal_images = extract_pdf_content(
        thermal_path, "output/thermal_images"
    )

    # Optional: limit text length for LLM
    inspection_text = inspection_text[:12000]
    thermal_text = thermal_text[:12000]

    print("PDF text and image extraction complete.\n")

    print("Step 2: Sending data to AI model...")

    report = generate_ddr_report(
        inspection_text,
        thermal_text,
        inspection_images,
        thermal_images
    )

    print("AI report generation complete.\n")

    print("Step 3: Saving DDR report...")

    save_ddr_report(report)

    print("\nProcess completed successfully.")


if __name__ == "__main__":
    main()