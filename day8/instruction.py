class Instruction:
    def __init__(self, name, argument):
        self.name = name
        self.argument = argument

    def __eq__(self, other) -> bool:
        if isinstance(other, Instruction) and \
                self.name == other.name and \
                self.argument == other.argument:
            return True
        return False

