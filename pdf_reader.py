import pymupdf
from pathlib import Path


def extract_text_from_pdf(pdf_path):
    pdf_file = Path(pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    if pdf_file.suffix.lower() != ".pdf":
        raise ValueError("The provided file must have a .pdf extension.")

    try:
        with pymupdf.open(pdf_file) as document:
            extracted_text = ""

            for page in document:
                extracted_text += page.get_text()

        if not extracted_text.strip():
            raise ValueError(
                "No extractable text found. The PDF may be scanned or empty."
            )

        return extracted_text

    except pymupdf.FileDataError as error:
        raise ValueError("The file is not a valid or readable PDF.") from error


if __name__ == "__main__":
    try:
        text = extract_text_from_pdf("samplePaperForProject.pdf")

        print("PDF text extraction successful!")
        print("\nExtracted text length:", len(text), "characters")
        print("\nFirst 1000 characters:\n")
        print(text[:1000])

    except (FileNotFoundError, ValueError) as error:
        print("Error:", error)