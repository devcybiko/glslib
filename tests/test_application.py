"""Tests for glslib.application module."""

import unittest
from unittest.mock import patch, MagicMock
from glslib.application import Application


class TestApplication(unittest.TestCase):
    """Test cases for Application class."""

    @patch('sys.argv', ['test_app'])
    def test_application_init(self):
        """Test Application initialization."""
        app = Application("Test Application")
        self.assertIsNotNone(app._arg_parser)
        self.assertIsNotNone(app.logger)
        self.assertIsNotNone(app.args)

    @patch('sys.argv', ['test_app', '--debug'])
    def test_debug_flag(self):
        """Test debug flag parsing."""
        app = Application("Test Application")
        self.assertTrue(app.args.debug)

    @patch('sys.argv', ['test_app', '--config', 'key1=value1', '--config', 'key2=value2'])
    @patch('glslib.application.Application._config_load')
    def test_config_arguments(self, mock_config_load):
        """Test config arguments parsing."""
        mock_config_load.return_value = {}
        app = Application("Test Application")
        self.assertEqual(app.args.config, ['key1=value1', 'key2=value2'])

    @patch('sys.argv', ['test_app'])
    def test_arg_parse(self):
        """Test argument parser setup."""
        app = Application("Test Application")
        self.assertIsNotNone(app._arg_parser)
        # Verify default config_json value
        self.assertEqual(app.args.config_json, ['config.json5'])

    @patch('sys.argv', ['test_app'])
    @patch('glslib.application.GJSON.load')
    def test_config_load_with_file(self, mock_gjson_load):
        """Test loading configuration from JSON file."""
        mock_gjson_load.return_value = {"key": "value"}
        app = Application("Test Application")
        self.assertIn("key", app.config)
        self.assertEqual(app.config["key"], "value")

    @patch('sys.argv', ['test_app', '--config', 'override_key=override_value'])
    @patch('glslib.application.GJSON.load')
    def test_config_override(self, mock_gjson_load):
        """Test config parameter override."""
        mock_gjson_load.return_value = {"key": "value"}
        app = Application("Test Application")
        self.assertIn("override_key", app.config)
        self.assertEqual(app.config["override_key"], "override_value")

    @patch('sys.argv', ['test_app'])
    @patch('builtins.print')
    def test_run_method(self, mock_print):
        """Test run method."""
        app = Application("Test Application")
        app.run()
        mock_print.assert_called_once_with("Running the application...")

    @patch('sys.argv', ['test_app'])
    def test_logger_initialized(self):
        """Test that logger is properly initialized."""
        app = Application("Test Application")
        self.assertIsNotNone(app.logger)
        self.assertEqual(app.logger.debug_level, 'Application')


if __name__ == "__main__":
    unittest.main()
