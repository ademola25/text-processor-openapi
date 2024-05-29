import unittest
from unittest.mock import patch, MagicMock
from project import write_properly, write_the_same_grammar_fixed, summarize

class TestTextProcessing(unittest.TestCase):

    @patch('text_processing.OpenAI')
    def test_write_properly(self, MockOpenAI):
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Corrected text with enhanced grammar and style"))]
        )
        MockOpenAI.return_value = mock_client

        user_input = "This is a text with grammar and style issues."
        result = write_properly(user_input)
        self.assertEqual(result, "Corrected text with enhanced grammar and style")

    @patch('text_processing.OpenAI')
    def test_write_the_same_grammar_fixed(self, MockOpenAI):
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Text with fixed grammar"))]
        )
        MockOpenAI.return_value = mock_client

        user_input = "This is a text with grammar errors."
        result = write_the_same_grammar_fixed(user_input)
        self.assertEqual(result, "Text with fixed grammar")

    @patch('text_processing.OpenAI')
    def test_summarize(self, MockOpenAI):
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = MagicMock(
            choices=[MagicMock(message=MagicMock(content="Concise summary of the text"))]
        )
        MockOpenAI.return_value = mock_client

        user_input = "This is a long text that needs summarizing."
        result = summarize(user_input)
        self.assertEqual(result, "Concise summary of the text")

if __name__ == '__main__':
    unittest.main()
