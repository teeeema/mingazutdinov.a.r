import os
import sys
import zipfile
import csv
import xml.etree.ElementTree as ET
from datetime import datetime


class ShellEmulator:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.current_path = "/"
        self.virtual_fs = {}
        self.log_file = open(self.logfile_path, "a", newline="")
        self.logger = csv.writer(self.log_file)
        self.load_filesystem()

    def load_config(self, config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()
        self.hostname = root.find("hostname").text
        self.filesystem_path = root.find("filesystem_path").text
        self.logfile_path = root.find("logfile_path").text

    def log_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logger.writerow([timestamp, action])
        self.log_file.flush()

    def load_filesystem(self):
        with zipfile.ZipFile(self.filesystem_path, "r") as zip_fs:
            for file_info in zip_fs.infolist():
                self.virtual_fs[file_info.filename] = zip_fs.read(
                    file_info.filename
                ).decode()

    def list_directory(self):
        current_dir = self.get_current_directory()
        for file in self.virtual_fs:
            if file.startswith(current_dir) and file != current_dir:
                print(file.replace(current_dir, "").split("/")[0])
        self.log_action("ls")

    def change_directory(self, path):
        if path == "/":
            self.current_path = "/"
        elif path == "..":
            self.current_path = (
                "/".join(self.current_path.strip("/").split("/")[:-1]) or "/"
            )
        else:
            potential_path = os.path.join(self.current_path, path).replace("\\", "/")
            if potential_path in self.virtual_fs:
                self.current_path = potential_path
            else:
                print(f"cd: no such file or directory: {path}")
        self.log_action(f"cd {path}")

    def make_directory(self, dirname):
        new_dir_path = os.path.join(self.current_path, dirname).replace("\\", "/")
        if new_dir_path not in self.virtual_fs:
            self.virtual_fs[new_dir_path + "/"] = ""
            print(f"Directory {dirname} created.")
        else:
            print(f"mkdir: cannot create directory '{dirname}': File exists")
        self.log_action(f"mkdir {dirname}")

    def echo(self, message):
        print(message)
        self.log_action(f"echo {message}")

    def exit_shell(self):
        self.log_action("exit")
        self.log_file.close()
        print("Exiting...")
        sys.exit(0)

    def run(self):
        while True:
            command = input(f"{self.hostname}:{self.current_path}$ ")
            self.handle_command(command)

    def handle_command(self, command):
        args = command.strip().split()
        if not args:
            return
        cmd, *params = args

        if cmd == "ls":
            self.list_directory()
        elif cmd == "cd":
            self.change_directory(params[0] if params else "/")
        elif cmd == "mkdir":
            self.make_directory(params[0] if params else "")
        elif cmd == "echo":
            self.echo(" ".join(params))
        elif cmd == "exit":
            self.exit_shell()
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    config_path = "config.xml"  # PQQQ P: P:P>P=QP8P3QQ