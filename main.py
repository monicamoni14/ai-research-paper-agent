from pdf_reader import extract_text_from_pdf
from text_processor import clean_text, split_text_into_chunks

pdf_path = "samplePaperForProject.pdf"

# Step 1: Extract text from PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Step 2: Clean extracted text
cleaned_text = clean_text(extracted_text)

# Step 3: Split cleaned text into chunks
chunks = split_text_into_chunks(
    cleaned_text,
    chunk_size=1500,
    overlap=200
)

# Display results
print("Original text length:", len(extracted_text))
print("Cleaned text length:", len(cleaned_text))
print("Total chunks:", len(chunks))

for index, chunk in enumerate(chunks):
    print(f"\nChunk {index + 1}")
    print("Characters:", len(chunk))
    print("Content:", chunk[:200])