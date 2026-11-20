import unittest

from src.preprocessing.text_cleaner import clean_text


class TestCleanText(unittest.TestCase):

    def test_remove_extra_spaces(self):
        text = "  Hello    Python   World  "
        result = clean_text(text)

        self.assertEqual(result, "Hello Python World")

    def test_remove_tabs_and_newlines(self):
        text = "Hello\tPython\nWorld"
        result = clean_text(text)

        self.assertEqual(result, "Hello Python World")

    def test_empty_string(self):
        text = ""
        result = clean_text(text)

        self.assertEqual(result, "")

    def test_only_whitespace(self):
        text = "       "
        result = clean_text(text)

        self.assertEqual(result, "")

    def test_integer_input(self):
        with self.assertRaises(TypeError):
            clean_text(123)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            clean_text(None)


if __name__ == "__main__":
    unittest.main()
