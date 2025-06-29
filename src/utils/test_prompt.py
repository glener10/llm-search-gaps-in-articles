import unittest
from unittest.mock import patch

from .prompt import read_prompt

class TestReadPrompt(unittest.TestCase):

    @patch('src.utils.prompt.pathlib.Path')
    def test_read_prompt_success_file_exists(self, MockPath):
        """
        should read and return the content of prompt.txt after stripping whitespace.
        """
        fake_content = "  this is the prompt.txt content. \n"
        expected_content = "this is the prompt.txt content."
        mock_path_instance = MockPath.return_value
        mock_path_instance.exists.return_value = True
        mock_path_instance.read_text.return_value = fake_content

        result = read_prompt()

        self.assertEqual(result, expected_content)
        MockPath.assert_called_once_with("prompt.txt")
        mock_path_instance.exists.assert_called_once()
        mock_path_instance.read_text.assert_called_once_with(encoding="utf-8")

    @patch('src.utils.prompt.pathlib.Path')
    def test_read_prompt_file_not_found(self, MockPath):
        """
        should handle exception when prompt.txt does not exist.
        """
        mock_path_instance = MockPath.return_value
        mock_path_instance.exists.return_value = False
        with self.assertRaises(FileNotFoundError) as context:
            read_prompt()
            
        self.assertEqual(str(context.exception), "❌ prompt.txt not found")
        MockPath.assert_called_once_with("prompt.txt")
        mock_path_instance.exists.assert_called_once()
        mock_path_instance.read_text.assert_not_called()