import unittest
import reverse_walk
from mock import Mock, patch, call
from inheritance import Super
from create_subprocess import create_process


class TestWithMock(unittest.TestCase):
    """Examples of UTs using the 'mock' library."""

    @patch('reverse_walk.os.listdir', Mock(return_value=[]))
    @patch('reverse_walk.os.getcwd', Mock(return_value='/a/b/c/d'))
    def test_get_repo_root_dir(self):
        """Using mock.patch decorator & context manager."""
        with patch('reverse_walk.sys.stdout.write') as mock_stdout:
            self.assertEqual(None, reverse_walk.get_repo_root_dir())
            self.assertTrue(reverse_walk.os.listdir.called)
            expected = [
                call('The current working directory is not a git repository.'),
                call('\n')
            ]
            self.assertEqual(expected, mock_stdout.call_args_list)

        # Using a mock objects 'side_effect'
        nodes_dirs = [['.git'], ['y'], ['.gitignore', 'README.md', '.git'],
                      ['r', 'z']]

        reverse_walk.os.listdir.side_effect = nodes_dirs  # finds root at /a/b
        self.assertEqual('/a/b', reverse_walk.get_repo_root_dir())

    def test_create_subprocess(self):
        """Mocking Classes - mock Popen to prevent test spawning a process."""
        with patch('create_subprocess.Popen') as MockPopen:
            # Mock the object created by Popen()
            instance = MockPopen.return_value
            # Mock the communicate() function and returncode attribute
            instance.communicate.return_value = ('foo.py', '')
            instance.returncode = 0
            create_process('ls')

    @patch.object(Super, 'do')
    def test_mock_an_object(self, mock_do):
        """Using mock.patch.object() to mock local object and reset_mock()"""
        mock_do.return_value = 'bar'
        instance = Super('foo')
        self.assertEqual('bar', instance.do())
        self.assertTrue(mock_do.called)
        mock_do.reset_mock()
        self.assertFalse(mock_do.called)
