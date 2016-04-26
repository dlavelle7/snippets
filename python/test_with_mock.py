import unittest
import reverse_walk
from mock import Mock, patch, call
from inheritance import Super


class TestWithMock(unittest.TestCase):
    """Examples of UTs using the 'mock' library."""

    @patch('reverse_walk.os.listdir', Mock(return_value=[]))
    @patch('reverse_walk.os.getcwd', Mock(return_value='/a/b/c/d'))
    def test_get_repo_root_dir(self):
        # Using mock.patch decorator & context manager
        with patch('reverse_walk.sys.stdout.write') as mock_stdout:
            self.assertEqual(None, reverse_walk.get_repo_root_dir())
            self.assertTrue(reverse_walk.os.listdir.called)
            expected = [
                call('The current working directory is not a git repository.'),
                call('\n')
            ]
            self.assertEqual(expected, mock_stdout.call_args_list)

        # Using a mock objects 'side_effect'
        nodes_dirs = [['r', 'z'], ['.gitignore', 'README.md', '.git'], ['y'], ['.git']]
        def find_at_b(current):
            return nodes_dirs.pop()

        reverse_walk.os.listdir.side_effect = find_at_b  # finds root at /a/b
        self.assertEqual('/a/b', reverse_walk.get_repo_root_dir())

    @patch.object(Super, 'do')
    def test_mock_a_class_function(self, mock_do):
        # Using mock.patch.object() and reset_mock()
        mock_do.return_value = 'bar'
        instance = Super('foo')
        self.assertEqual('bar', instance.do())
        self.assertTrue(mock_do.called)
        mock_do.reset_mock()
        self.assertFalse(mock_do.called)
