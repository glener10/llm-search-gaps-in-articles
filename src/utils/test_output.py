import unittest
from unittest.mock import patch, mock_open

from .output import persist_output

class TestPersistOutput(unittest.TestCase):
    @patch('src.utils.output.print')
    @patch('src.utils.output.pathlib.Path')
    def test_persist_output_writes_correctly_to_file(self, MockPath, mock_print):
        """
        should write the response to the specified file with the correct format
        """
        path = "output/test_gaps.txt"
        input_str = "arquivo_de_entrada.txt"
        model = "gemini-pro"
        response = "this is a test response"
        mock_path_instance = MockPath.return_value
        mock_file_handle = mock_open()
        mock_path_instance.open = mock_file_handle
        separator = "-" * 100
        expected_content = (
            f"file {input_str} | {model}\n\n{response}\n{separator}\n\n\n"
        )
        expected_print_message = f"✅ gaps saved into {mock_path_instance}"

        persist_output(path, input_str, model, response)

        MockPath.assert_called_once_with(path)
        mock_path_instance.touch.assert_called_once_with(exist_ok=True)
        mock_path_instance.open.assert_called_once_with("a", encoding="utf-8")
        mock_file_handle().write.assert_called_once_with(expected_content)
        mock_print.assert_called_once_with(expected_print_message)