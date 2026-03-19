import os
from src.document_parser import extract_pdf_content
from src.AI_engine import generate_document_report
from src.report_builder import save_document_report


def main():

    print("Starting AI Document Analysis System...\n")

    pdf_folder = "data/"

    all_text = ""
    all_images = []

    # Safety check
    if not os.path.exists(pdf_folder):
        print("Error: 'data/' folder not found.")
        return

    print("Step 1: Extracting text and images from all PDFs...\n")

    found_pdf = False

    for file in os.listdir(pdf_folder):

        if file.lower().endswith(".pdf"):
            found_pdf = True

            pdf_path = os.path.join(pdf_folder, file)

            print(f"Processing: {file}")

            try:
                text, images = extract_pdf_content(pdf_path, "output/images")

                all_text += text + "\n"
                all_images.extend(images)

            except Exception as e:
                print(f"Error processing {file}: {e}")

    if not found_pdf:
        print("No PDF files found in 'data/' folder.")
        return

    # Limit text size for LLM
    all_text = all_text[:12000]

    print("\nPDF extraction complete.")
    print(f"Total text length: {len(all_text)} characters")
    print(f"Total images extracted: {len(all_images)}\n")

    print("Step 2: Sending data to AI model...")

    report = generate_document_report(
        all_text,
        all_images
    )

    print("AI report generation complete.\n")

    print("Step 3: Saving report...")

    save_document_report(report)

    print("\nProcess completed successfully.")


if __name__ == "__main__":
    main()