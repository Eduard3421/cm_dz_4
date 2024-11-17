import sys
import json

def assemble(instruction):
    parts = instruction.split()
    if len(parts) != 2:
        raise ValueError("Invalid instruction format. Expected two numbers.")
    op_code = int(parts[0])
    value = int(parts[1])

    # коды для команд
    if op_code == 164:  # загрузка константы
        return [op_code, value]
    elif op_code == 144:  # чтение из памяти
        shift_count = 0
        while value > 255:
            value -= 256
            shift_count += 1
        return [op_code, value, shift_count]
    elif op_code == 29:  # запись в память
        shift_count = 0
        while value > 255:
            value -= 256
            shift_count += 1
        return [op_code, value, shift_count]
    elif op_code == 74:  # побитовый циклический сдвиг влево
        shift_count = 0
        while value > 255:
            value -= 256
            shift_count += 1
        return [op_code, value, shift_count]
    else:
        raise ValueError("Unknown op_code")

class UVMInterpreter:
    def __init__(self, binary_code):
        self.binary_code = binary_code # инструкции
        self.memory = [0] * 1024  # память
        self.stack = [] # регистр-аккумулятор (стек)
        self.ip = 0  # текущее место в инструкциях

    def execute(self):
        while self.ip < len(self.binary_code):
            op_code = self.binary_code[self.ip]
            self.ip += 1
            if op_code == 164:  # загрузка константы
                const = self.binary_code[self.ip]
                self.ip += 1
                self.stack.append(const)
            elif op_code == 144:  # чтение из памяти
                addr = self.stack.pop()
                self.stack.append(self.memory[addr + self.binary_code[self.ip] + 256 * self.binary_code[self.ip + 1]])
                self.ip += 2
            elif op_code == 29:  # запись в память
                addr = self.binary_code[self.ip]
                offset = self.binary_code[self.ip + 1]
                self.ip += 2
                value = self.stack.pop()
                self.memory[addr + offset * 256] = value
            elif op_code == 74:  # побитовый циклический сдвиг влево
                value = self.stack.pop()
                addr = self.binary_code[self.ip]
                shift = self.binary_code[self.ip + 1]
                self.ip += 2
                val = addr + shift * 256
                val *= 2 ** value
                self.stack.append(val)
            else:
                raise ValueError("Unknown operation code")


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    log_file = sys.argv[3]
    input_binary_file = sys.argv[4]
    start = int(sys.argv[5])
    end = int(sys.argv[6])
    output_result_file = sys.argv[7]
    # input_file = "C:\\Users\\Edward\\PycharmProjects\\pythonProject2\\input_file.txt"
    # output_file = "C:\\Users\\Edward\\PycharmProjects\\pythonProject2\\file.bin"
    # log_file = "C:\\Users\\Edward\\PycharmProjects\\pythonProject2\\logfile.json"

    with open(input_file, 'r') as f:
        instructions = f.readlines()

    binary_code = []
    log_data = []

    for i, instruction in enumerate(instructions):
        instruction = instruction.strip()
        try:
            binary_instruction = assemble(instruction)
            binary_code.extend(binary_instruction)
            log_data.append({'instruction': instruction, 'binary': binary_instruction})
        except ValueError as e:
            print(f"Error on line {i+1}: {e}")
            return

    with open(output_file, 'wb') as f:
        f.write(bytes(binary_code))

    if log_file:
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=4)


    # input_binary_file = "C:\\Users\\Edward\\PycharmProjects\\pythonProject2\\file.bin"
    # memory_range = 0, 1024
    # output_result_file = "C:\\Users\\Edward\\PycharmProjects\\pythonProject2\\result.json"
    with open(input_binary_file, 'rb') as f:
        binary_code = list(f.read())

    interpreter = UVMInterpreter(binary_code)
    interpreter.execute()
    result = interpreter.memory[start:end]

    with open(output_result_file, 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    main()
