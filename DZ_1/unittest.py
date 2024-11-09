import unittest
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.shell = ShellEmulator('test_config.xml')
        self.shell.load_filesystem()

    def test_ls(self):
        self.shell.current_path = '/'
        self.shell.virtual_fs = {'/test_dir/': ''}
        output = self.shell.list_directory()
        self.assertIn('test_dir', output)

    def test_cd(self):
        self.shell.virtual_fs = {'/test_dir/': ''}
        self.shell.change_directory('test_dir')
        self.assertEqual(self.shell.current_path, '/test_dir/')

    def test_mkdir(self):
        self.shell.make_directory('new_dir')
        self.assertIn('/new_dir/', self.shell.virtual_fs)

    def test_echo(self):
        output = self.shell.echo('Hello World')
        self.assertEqual(output, 'Hello World')

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.shell.exit_shell()

if __name__ == '__main__':
    unittest.main()
