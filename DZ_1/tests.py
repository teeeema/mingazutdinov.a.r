import unittest
from emulator import ShellEmulator

class TestShellEmulator(unittest.TestCase):

    def setUp(self):
        self.emulator = ShellEmulator('config.xml')

    def test_ls_empty(self):
        self.emulator.current_dir = '/'
        self.assertEqual(self.emulator.ls(), [])

    def test_ls_with_files(self):
        self.emulator.vfs = {'/file1.txt': 'content1', '/file2.txt': 'content2'}
        self.assertIn('/file1.txt', self.emulator.ls())
        self.assertIn('/file2.txt', self.emulator.ls())

    def test_cd_root(self):
        self.emulator.cd('/')
        self.assertEqual(self.emulator.current_dir, '/')

    def test_cd_nonexistent(self):
        with self.assertRaises(Exception) as context:
            self.emulator.cd('/nonexistent')
        self.assertTrue('No such file or directory' in str(context.exception))

    def test_mkdir_new_dir(self):
        dir_name = 'newdir'
        self.emulator.mkdir(dir_name)
        self.assertIn(f'/{dir_name}', self.emulator.vfs)

    def test_mkdir_existing_dir(self):
        dir_name = 'existingdir'
        self.emulator.vfs[f'/{dir_name}'] = None  # Инициализация в контексте теста, без self вне метода
        with self.assertRaises(Exception) as context:
            self.emulator.mkdir(dir_name)
        self.assertTrue("File exists" in str(context.exception))


    def test_echo(self):
        output = self.emulator.echo("Hello, World!")
        self.assertEqual(output, "Hello, World!")

    def test_exit(self):
        with self.assertRaises(SystemExit):
            self.emulator.execute_command('exit')

if __name__ == '__main__':
    unittest.main()
