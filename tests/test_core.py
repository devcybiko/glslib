"""Tests for glslib.core module."""

import unittest
from glslib.core import greeting


class TestCore(unittest.TestCase):
    """Test cases for core functionality."""

    def test_greeting_default(self):
        """Test greeting with default name."""
        result = greeting()
        self.assertEqual(result, "Hello, World!")

    def test_greeting_custom(self):
        """Test greeting with custom name."""
        result = greeting("Alice")
        self.assertEqual(result, "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
