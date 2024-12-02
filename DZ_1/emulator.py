import os

class ShellEmulator:
    def __init__(self):
        self.file_system = {
            "/": {
                "type": "dir",
                "contents": {
                    "file1.txt": {"type": "file", "contents": "This is file1"},
                    "dir1": {
                        "type": "dir",
                        "contents": {
                            "file2.txt": {"type": "file", "contents": "This is file2"}
                        }
                    }
                }
            }
        }
        self.current_path = "/"
        self.home_directory = "/"

    def run(self):
        while True:
            command = input(f"Tema:{self.current_path}$ ").strip()
            if not command:
                continue
            try:
                self.execute_command(command)
            except Exception as e:
                print(e)

    def execute_command(self, command):
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "ls":
            self.ls()
        elif cmd == "cd":
            if len(args) == 0:
                self.cd(self.home_directory)
            else:
                self.cd(args[0])
        elif cmd == "mkdir":
            if len(args) == 0:
                raise Exception("Usage: mkdir <directory_name>")
            else:
                self.mkdir(args[0])
        elif cmd == "echo":
            self.echo(args)
        elif cmd == "exit":
            print("Exiting shell emulator.")
            exit()
        else:
            print(f"{cmd}: command not found")

    def ls(self):
        current_dir = self._get_current_dir()
        if not current_dir["contents"]:
            print("Directory is empty.")
        else:
            for name, item in current_dir["contents"].items():
                print(name)

    def cd(self, path):
        target_path = self._resolve_path(path)
        target_dir = self._get_directory(target_path)

        if target_dir and target_dir["type"] == "dir":
            self.current_path = target_path
        else:
            raise Exception("No such file or directory")

    def mkdir(self, dir_name):
        current_dir = self._get_current_dir()
        if dir_name in current_dir["contents"]:
            raise Exception("Directory already exists")
        current_dir["contents"][dir_name] = {"type": "dir", "contents": {}}

    def echo(self, args):
        print(" ".join(args))

    def _resolve_path(self, path):
        """Resolve relative or absolute path to an absolute path."""
        if path.startswith("/"):
            return os.path.normpath(path)
        else:
            return os.path.normpath(os.path.join(self.current_path, path))

    def _get_current_dir(self):
        """Get the directory object for the current path."""
        return self._get_directory(self.current_path)

    def _get_directory(self, path):
        """Traverse the file system and return the directory at the given path."""
        parts = path.strip("/").split("/")
        current = self.file_system["/"]
        for part in parts:
            if not part:  # Skip empty parts for root
                continue
            if part in current["contents"] and current["contents"][part]["type"] == "dir":
                current = current["contents"][part]
            else:
                return None
        return current


if __name__ == "__main__":
    emulator = ShellEmulator()
    emulator.run()
