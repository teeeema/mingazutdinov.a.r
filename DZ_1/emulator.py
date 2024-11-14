import os
import zipfile
import csv
import xml.etree.ElementTree as ET
from datetime import datetime

class ShellEmulator:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.hostname = self.config['hostname']
        self.vfs_path = self.config['vfs_path']
        self.log_path = self.config['log_path']
        self.current_dir = '/'  # Текущая директория внутри VFS
        self.vfs = {}           # Структура для файловой системы в виде словаря
        self.load_vfs()         # Загрузка виртуальной файловой системы

    def load_config(self, config_path):
        tree = ET.parse(config_path)
        root = tree.getroot()
        return {
            'hostname': root.find('hostname').text,
            'vfs_path': root.find('vfs_path').text,
            'log_path': root.find('log_path').text
        }

    def load_vfs(self):
        """Загружает файловую систему из zip-архива"""
        with zipfile.ZipFile(self.vfs_path, 'r') as zipf:
            for file in zipf.namelist():
                self.vfs[file] = zipf.read(file)

    def log_action(self, action):
        """Записывает действие в лог-файл с отметкой времени"""
        with open(self.log_path, 'a', newline='') as log_file:
            log_writer = csv.writer(log_file)
            log_writer.writerow([datetime.now().isoformat(), action])

    def run(self):
        """Запуск основного цикла эмулятора"""
        while True:
            command = input(f"{self.hostname}:{self.current_dir}$ ")
            if command == 'exit':
                self.log_action("exit")
                raise SystemExit  # Вызываем исключение для выхода
            self.execute_command(command)


    def execute_command(self, command):
        """Выполнение команд оболочки"""
        args = command.split()
        cmd = args[0]

        if cmd == 'ls':
            self.ls()
        elif cmd == 'cd':
            if len(args) > 1:
                self.cd(args[1])
            else:
                print("cd: missing operand")
        elif cmd == 'mkdir':
            if len(args) > 1:
                self.mkdir(args[1])
            else:
                print("mkdir: missing operand")
        elif cmd == 'echo':
            print(" ".join(args[1:]))
        elif cmd == 'exit':
            raise SystemExit  # Вызываем исключение при exit
        else:
            print(f"{cmd}: command not found")
        self.log_action(command)

        
    def ls(self):
        """Реализация команды ls"""
        files = [file for file in self.vfs if file.startswith(self.current_dir)]
        print("\n".join(files))
        return files  # Возвращаем список файлов для тестирования

    def cd(self, path):
        """Реализация команды cd"""
        # Если путь равен корневому, переходите сразу
        if path == '/':
            self.current_dir = '/'
            return
        
        # Построение полного пути
        new_path = os.path.join(self.current_dir, path) if path != '/' else '/'
        
        # Проверка на существование пути в vfs
        if new_path in self.vfs:
            self.current_dir = new_path  # Обновляем текущий каталог
        else:
            print(f"cd: {path}: No such file or directory")
            raise Exception("No such file or directory")



    def mkdir(self, dir_name):
        """Реализация команды mkdir"""
        new_dir = os.path.join(self.current_dir, dir_name)
        if new_dir in self.vfs:
            print(f"mkdir: cannot create directory '{dir_name}': File exists")
            raise Exception("File exists")
        else:
            self.vfs[new_dir] = {}  # Добавляем пустой словарь для новой директории в vfs
            print(f"Directory '{dir_name}' created.")


            
    def echo(self, *args):
        """Метод для тестов, выполняющий команду echo"""
        output = " ".join(args)
        print(output)
        return output

if __name__ == "__main__":
    emulator = ShellEmulator('config.xml')
    emulator.run()
