import unittest

from text_processor import clean_text, split_text_into_chunks


class TestCleanText(unittest.TestCase):

    def test_remove_extra_spaces(self):
        text = "Artificial     Intelligence"
        result = clean_text(text)

        self.assertEqual(result, "Artificial Intelligence")

    def test_preserve_paragraphs(self):
        text = "Hello\n\n\nWorld"
        result = clean_text(text)

        self.assertEqual(result, "Hello\n\nWorld")

    def test_remove_leading_and_trailing_spaces(self):
        text = "   Hello World   "
        result = clean_text(text)

        self.assertEqual(result, "Hello World")

    def test_empty_text(self):
        self.assertEqual(clean_text(""), "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            clean_text(123)


class TestTextChunking(unittest.TestCase):

    def test_chunk_creation(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        chunks = split_text_into_chunks(
            text,
            chunk_size=10,
            overlap=2
        )

        self.assertEqual(len(chunks), 4)

    def test_chunk_size(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        chunks = split_text_into_chunks(
            text,
            chunk_size=10,
            overlap=2
        )

        for chunk in chunks:
            self.assertLessEqual(len(chunk), 10)

    def test_chunk_overlap(self):
        text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        chunks = split_text_into_chunks(
            text,
            chunk_size=10,
            overlap=2
        )

        self.assertEqual(chunks[0][-2:], chunks[1][:2])

    def test_empty_text(self):
        chunks = split_text_into_chunks("")

        self.assertEqual(chunks, [])

    def test_invalid_chunk_size(self):
        with self.assertRaises(ValueError):
            split_text_into_chunks("Hello World", chunk_size=0)

    def test_invalid_overlap(self):
        with self.assertRaises(ValueError):
            split_text_into_chunks(
                "Hello World",
                chunk_size=10,
                overlap=10
            )


if __name__ == "__main__":
    unittest.main()