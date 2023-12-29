"""Module containing unit tests for transform module."""
import unittest
import transform

class TestStringMethods(unittest.TestCase):
    """Test the functions in the transform module."""

    def test_is_upper(self):
        """Test the to_upper_case function."""
        string = transform.to_upper_case("hello")
        self.assertEqual(string, "HELLO")

    def test_is_lower(self):
        """Test the to_lower_case function."""
        string = transform.to_lower_case("HELLO")
        self.assertEqual(string, "hello")

    def test_is_capitalize(self):
        """Test the to_capitalize function."""
        string = transform.to_capitalize("HELLO")
        self.assertEqual(string, "Hello")

if __name__ == '__main__':
    unittest.main()
