class Instruction:
    def __init__(self, command, value):
        self.command = command
        self.value = int(value)
        self.executed = False


class Computer:
    def __init__(self, instructions):
        self.accumulator = 0
        self.instructions = [
            Instruction(i.split(' ')[0], i.split(' ')[1]) for i in instructions
        ]

    def run_instruction_number(self, number):
        instruction = self.instructions[number]

        if instruction.executed:
            raise RuntimeError(
                'Infinite loop, accumulator is {}'.format(self.accumulator))

        offset = 1

        if instruction.command == 'acc':
            self.accumulator += instruction.value
        elif instruction.command == 'nop':
            pass
        elif instruction.command == 'jmp':
            offset = instruction.value

        instruction.executed = True

        return offset

    def execute(self):
        next_instruction = 0

        while True:
            if next_instruction >= len(self.instructions):
                return self.accumulator

            next_instruction += self.run_instruction_number(next_instruction)
