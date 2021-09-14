from .instruction import Instruction


class JumpOutOfBoundsException(Exception):
    pass


class Machine:

    def __init__(self):
        self.accumulator = 0
        self.cursor = 0
        self.program = []
        self._line_visit_count = {}

    @property
    def program_length(self):
        return len(self.program)

    def has_visited(self, line_number):
        return self.line_visit_count(line_number) > 0

    def line_visit_count(self, line_number):
        if line_number in self._line_visit_count.keys():
            return self._line_visit_count[line_number]
        else:
            return 0

    def append_instruction(self, instruction_name, argument):
        self.program.append(Instruction(instruction_name, argument))

    def run_one_instruction(self, instruction: Instruction):
        if instruction.name == "acc":
            self.run_acc(instruction)
        if instruction.name == "jmp":
            self.run_jmp(instruction)

    def run_acc(self, instruction):
        self.accumulator += instruction.argument

    def run_jmp(self, instruction):
        self.cursor += instruction.argument
        if self.cursor > self.program_length:
            raise JumpOutOfBoundsException("Jump out of bounds!")

    def run_program(self):
        while self.cursor != self.program_length:
            self._line_visit_count[self.cursor] = 1
            self.run_one_instruction(self.program[self.cursor])
            self.cursor += 1