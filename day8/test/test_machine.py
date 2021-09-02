import pytest

from day8.machine import Machine, Instruction, JumpOutOfBoundsException


def test_empty_machine():
    machine = Machine()
    assert machine.program_length == 0
    assert machine.accumulator == 0
    machine.run_program()
    assert machine.program_length == 0
    assert machine.accumulator == 0


def test_nop():
    machine = Machine()
    machine.append_instruction("nop", 1)
    machine.append_instruction("nop", -1)
    machine.append_instruction("nop", 19)
    assert machine.program_length == 3
    assert machine.accumulator == 0
    assert not machine.has_visited(0)
    assert not machine.has_visited(1)
    assert not machine.has_visited(2)
    machine.run_program()
    assert machine.has_visited(0)
    assert machine.has_visited(1)
    assert machine.has_visited(2)
    assert machine.accumulator == 0


def test_acc_1():
    machine = Machine()
    machine.append_instruction("acc", 1)
    assert machine.accumulator == 0
    machine.run_program()
    assert machine.accumulator == 1


def test_acc_2():
    machine = Machine()
    machine.append_instruction("acc", 2)
    assert machine.accumulator == 0
    machine.run_program()
    assert machine.accumulator == 2


def test_acc_multiple():
    machine = Machine()
    machine.append_instruction("acc", 3)
    machine.append_instruction("acc", 5)
    machine.append_instruction("acc", -3)
    machine.append_instruction("acc", 0)
    assert machine.accumulator == 0
    machine.run_program()
    assert machine.accumulator == 5


def test_instruction_equality():
    nop1 = Instruction("nop", 1)
    nop2 = Instruction("nop", 1)
    acc = Instruction("acc", 2)
    assert nop1 == nop2
    assert nop2 == nop1
    assert not acc == nop1
    assert not acc == nop2
    assert not nop1 == acc
    assert not nop2 == acc


def test_jmp():
    machine = Machine()
    machine.append_instruction("jmp", 2)
    machine.append_instruction("acc", 1)
    machine.append_instruction("nop", 0)
    assert machine.accumulator == 0
    assert machine.cursor == 0
    machine.run_program()
    assert machine.accumulator == 0
    assert machine.cursor == 3


def test_jmp_out_of_bounds():
    machine = Machine()
    machine.append_instruction("jmp", 100)
    with pytest.raises(JumpOutOfBoundsException):
        machine.run_program()