#!/usr/bin/python3
"""
Test for console.py
"""

import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up the console for testing."""
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        """Assert the output to the console."""
        self.console.onecmd(expected_output)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout_contains(self, expected_output, mock_stdout):
        """Assert that the output contains a certain string."""
        self.console.onecmd(expected_output)
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout_not_contains(self, expected_output, mock_stdout):
        """Assert that the output does not contain a certain string."""
        self.console.onecmd(expected_output)
        self.assertNotIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stderr', new_callable=StringIO)
    def assert_stderr(self, expected_output, mock_stderr):
        """Assert the error output to the console."""
        self.console.onecmd("{}".format(expected_output))
        self.assertEqual(mock_stderr.getvalue().strip(), expected_output)

    @patch('sys.stderr', new_callable=StringIO)
    def assert_stderr_contains(self, expected_output, mock_stderr):
        """Assert that the error output contains a certain string."""
        self.console.onecmd(expected_output)
        self.assertIn(expected_output, mock_stderr.getvalue())

    @patch('sys.stderr', new_callable=StringIO)
    def assert_stderr_not_contains(self, expected_output, mock_stderr):
        """Assert that the error output does not contain a certain string."""
        self.console.onecmd(expected_output)
        self.assertNotIn(expected_output, mock_stderr.getvalue())

    # Add more test functions based on your specific implementation of the console

    def test_create_command(self):
        """Test the create command in the console."""
        self.assert_stdout('create BaseModel')

    def test_show_command(self):
        """Test the show command in the console."""
        self.assert_stdout('show BaseModel')

    def test_destroy_command(self):
        """Test the destroy command in the console."""
        self.assert_stdout('destroy BaseModel')

    def test_all_command(self):
        """Test the all command in the console."""
        self.assert_stdout('all BaseModel')

    def test_update_command(self):
        """Test the update command in the console."""
        self.assert_stdout('update BaseModel 1234 attribute value')

    def test_quit_command(self):
        """Test the quit command in the console."""
        with patch('builtins.quit', side_effect=SystemExit):
            self.assert_stdout('quit')

    def test_EOF_command(self):
        """Test the EOF command in the console."""
        with patch('builtins.quit', side_effect=SystemExit):
            self.assert_stdout('EOF')

    def test_emptyline_command(self):
        """Test the emptyline command in the console."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('')
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_help_command(self):
        """Test the help command in the console."""
        expected_output = 'EOF  all  create  destroy  help  quit  show  update'
        self.assert_stdout_contains('help')

    def test_help_EOF_command(self):
        """Test the help command for EOF in the console."""
        expected_output = 'EOF command to exit the program'
        self.assert_stdout_contains('help EOF')

    def test_help_all_command(self):
        """Test the help command for all in the console."""
        expected_output = 'all command to prints all string representation of all instances'
        self.assert_stdout_contains('help all')

    # Add more test functions for other commands

if __name__ == '__main__':
    unittest.main()