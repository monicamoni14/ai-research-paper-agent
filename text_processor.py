import re
def clean_text(text):
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove repeated spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove unnecessary spaces around line breaks
    text = re.sub(r" *\n *", "\n", text)

    # Reduce excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
def split_text_into_chunks(text, chunk_size=1500, overlap=200):

    # Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    # Store generated chunks
    chunks = []

    # Starting position
    start = 0

    # Process text until the entire document is covered
    while start < len(text):

        end = start + chunk_size

        # Extract a portion of text
        chunk = text[start:end]

        # Store the chunk
        chunks.append(chunk)

        # Move forward while retaining overlap
        start += chunk_size - overlap

    return chunks
if __name__ == "__main__":

    sample_text = "Artificial Intelligence and Machine Learning. " * 200

    chunks = split_text_into_chunks(sample_text)

    print("TEXT CHUNKING SUCCESSFUL")

    print("Total chunks:", len(chunks))

    for index, chunk in enumerate(chunks):

        print(f"\nChunk {index + 1}")

        print("Characters:", len(chunk))

        print("Content:", chunk[:100])


if __name__ == "__main__":
    sample_text = """
       Artificial       Intelligence


       Machine       Learning


       Deep       Learning
    """

    cleaned = clean_text(sample_text)

    print("Before cleaning:")
    print(repr(sample_text))

    print("\nAfter cleaning:")
    print(repr(cleaned))        