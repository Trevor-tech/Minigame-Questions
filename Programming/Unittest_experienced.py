import unittest
from experienced import reverse_words

class TestReverseWords(unittest.TestCase):
    def test_basic_sentences(self):
        self.assertEqual(reverse_words("hello world"), "world hello")
        self.assertEqual(reverse_words("Python is fun"), "fun is Python")
    
    def test_single_word(self):
        self.assertEqual(reverse_words("Hello"), "Hello")
    
    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("  spaced  out  words  "), "words out spaced")
    
    def test_empty_string(self):
        self.assertEqual(reverse_words(""), "")
    
    def test_punctuation(self):
        self.assertEqual(reverse_words("Hello, world!"), "world! Hello,")
    
if __name__ == "__main__":
    unittest.main()
