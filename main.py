from pathlib import Path

from pdf_reader import extract_text_from_pdf


def main():

    print("=" * 60)
    print("AI RESEARCH PAPER-TO-EXPERIMENT AGENT")
    print("=" * 60)

    # Project information
    project_name = "AI Research Paper-to-Experiment Agent"

    print("\nProject:", project_name)

    # Locate the research paper
    pdf_path = Path(__file__).parent / "samplePaperForProject.pdf"

    print("\nReading research paper...")

    try:

        # Extract text from PDF
        extracted_text = extract_text_from_pdf(str(pdf_path))

        if not extracted_text.strip():
            print("Warning: No extractable text found in the PDF.")
            return

        print("\nPDF extraction successful!")

        # Display extraction information
        print("Extracted characters:", len(extracted_text))

        print("\nFirst 1000 characters:")
        print("-" * 60)

        print(extracted_text[:1000])

        print("\n" + "=" * 60)
        print("PDF PROCESSING COMPLETED")
        print("=" * 60)

    except (FileNotFoundError, ValueError) as error:

        print("\nError:", error)


if __name__ == "__main__":
    main()