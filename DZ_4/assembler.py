import struct
import yaml
import sys

# Описание команд
COMMANDS = {
    "LOAD": 0xAA,  # Загрузка константы
    "READ": 0xB7,  # Чтение из памяти
    "WRITE": 0x79,  # Запись в память
    "ABS": 0x69,    # Унарная операция abs()
}

def assemble(input_path, output_path, log_path):
    with open(input_path, "r") as source, open(output_path, "wb") as binary, open(log_path, "w") as log:
        log_data = []
        for line in source:
            parts = line.strip().split()
            cmd = parts[0]
            if cmd == "LOAD":
                opcode = COMMANDS[cmd]
                const = int(parts[1])
                binary.write(struct.pack("B", opcode))
                binary.write(struct.pack("<i", const))  # Используем знаковый формат
                log_data.append({"command": "LOAD", "opcode": opcode, "constant": const})
            elif cmd == "READ":
                opcode = COMMANDS[cmd]
                binary.write(struct.pack("B", opcode))
                log_data.append({"command": "READ", "opcode": opcode})
            elif cmd == "WRITE":
                opcode = COMMANDS[cmd]
                addr = int(parts[1])
                binary.write(struct.pack("B", opcode))
                binary.write(struct.pack("<I", addr))  # Память по-прежнему беззнаковая
                log_data.append({"command": "WRITE", "opcode": opcode, "address": addr})
            elif cmd == "ABS":
                opcode = COMMANDS[cmd]
                addr = int(parts[1])
                binary.write(struct.pack("B", opcode))
                binary.write(struct.pack("<I", addr))
                log_data.append({"command": "ABS", "opcode": opcode, "address": addr})
        
        yaml.dump(log_data, log)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 assembler.py <input_path> <output_path> <log_path>")
        sys.exit(1)
    assemble(sys.argv[1], sys.argv[2], sys.argv[3])
