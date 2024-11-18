import struct
import yaml
import sys

MEMORY_SIZE = 1024

class VirtualMachine:
    def __init__(self):
        self.memory = [0] * MEMORY_SIZE
        self.accumulator = 0

    def load(self, const):
        self.accumulator = const

    def read(self):
        self.accumulator = self.memory[self.accumulator]

    def write(self, addr):
        self.memory[addr] = self.accumulator

    def abs(self, addr):
        self.memory[addr] = abs(self.accumulator)

    def execute(self, program_path, result_path, mem_range):
        with open(program_path, "rb") as binary, open(result_path, "w") as result:
            while byte := binary.read(1):
                opcode = struct.unpack("B", byte)[0]
                if opcode == 0xAA:  # LOAD
                    const = struct.unpack("<i", binary.read(4))[0]  # Знаковое значение
                    self.load(const)
                elif opcode == 0xB7:  # READ
                    self.read()
                elif opcode == 0x79:  # WRITE
                    addr = struct.unpack("<I", binary.read(4))[0]
                    self.write(addr)
                elif opcode == 0x69:  # ABS
                    addr = struct.unpack("<I", binary.read(4))[0]
                    self.abs(addr)
            
            start, end = mem_range
            result_data = {"memory": self.memory[start:end]}
            yaml.dump(result_data, result)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 interpreter.py <binary_path> <result_path> <mem_start> <mem_end>")
        sys.exit(1)

    binary_path = sys.argv[1]
    result_path = sys.argv[2]
    mem_start = int(sys.argv[3])
    mem_end = int(sys.argv[4])

    vm = VirtualMachine()
    vm.execute(binary_path, result_path, (mem_start, mem_end))
