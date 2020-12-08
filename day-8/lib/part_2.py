#!/usr/bin/env python3

from .computer import Computer


def part_2(original_instructions):
    # Change one jmp to nop or one nop to jmp
    for i in range(len(original_instructions)):
        instruction_copy = original_instructions[:]
        command = original_instructions[i].split(' ')[0]

        if command == 'nop':
            instruction_copy[i] = instruction_copy[i].replace(command, 'jmp')
        elif command == 'jmp':
            instruction_copy[i] = instruction_copy[i].replace(command, 'nop')

        c = Computer(instruction_copy)

        try:
            return c.execute()
        except BaseException:
            continue
