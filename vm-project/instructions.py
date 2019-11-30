"""This is a table of instructions."""

import instruction_implementations.branch as branch
import instruction_implementations.logic as logic
import instruction_implementations.arithmetics as arithmetics
import instruction_implementations.special as special


class Instruction:
    """This is the class for instructions."""

    def __init__(self, symbol, opcode, function):
        self.symbol = symbol
        self.opcode = opcode
        self.function = function

    def execute(self, virtual_machine):
        """Executes instruction on a virtual machine."""
        self.function(virtual_machine)


INSTRUCTION_TABLE = [
    Instruction("BU", 0x00, branch.bu_fun),
    Instruction("BE", 0x01, branch.be_fun),
    Instruction("BG", 0x02, branch.bg_fun),
    Instruction("BL", 0x03, branch.bl_fun),
    Instruction("BZ", 0x04, branch.bz_fun),
    Instruction("ADD", 0x05, arithmetics.add_fun),
    Instruction("SUB", 0x06, arithmetics.sub_fun),
    Instruction("MUL", 0x07, arithmetics.mul_fun),
    Instruction("DIV", 0x08, arithmetics.div_fun),
    Instruction("FADD", 0x09, arithmetics.fadd_fun),
    Instruction("FSUB", 0x0A, arithmetics.fsub_fun),
    Instruction("FMUL", 0x0B, arithmetics.fmul_fun),
    Instruction("FDIV", 0x0C, arithmetics.fdiv_fun),
    Instruction("NOT", 0x0D, logic.not_fun),
    Instruction("AND", 0x0E, logic.and_fun),
    Instruction("OR", 0x0F, logic.or_fun),
    Instruction("COMP", 0x10, special.comp_fun),
    Instruction("LOAD", 0x11, special.load_fun),
    Instruction("PUSH", 0x12, special.push_fun),
    Instruction("POP", 0x13, special.pop_fun),
]
