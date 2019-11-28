"""This is a table of instructions."""

import instructions.branch as branch
import instructions.logic as logic
import instructions.arithmetics as arithmetics
import instructions.special as special


class instruction:
    """This is the class for instructions."""

    def __init__(self, symbol, opcode, function):
        self.symbol = symbol
        self.opcode = opcode
        self.function = function

    def execute(self, virtual_machine):
        """Executes instruction on a virtual machine."""
        self.function(virtual_machine)


INSTRUCTION_TABLE = [
    instruction("BU", 0x00, branch.bu_fun),
    instruction("BE", 0x01, branch.be_fun),
    instruction("BG", 0x02, branch.bg_fun),
    instruction("BL", 0x03, branch.bl_fun),
    instruction("BZ", 0x04, branch.bz_fun),
    instruction("ADD", 0x05, arithmetics.add_fun),
    instruction("SUB", 0x06, arithmetics.sub_fun),
    instruction("MUL", 0x07, arithmetics.mul_fun),
    instruction("DIV", 0x08, arithmetics.div_fun),
    instruction("FADD", 0x09, arithmetics.fadd_fun),
    instruction("FSUB", 0x0A, arithmetics.fsub_fun),
    instruction("FMUL", 0x0B, arithmetics.fmul_fun),
    instruction("FDIV", 0x0C, arithmetics.fdiv_fun),
    instruction("NOT", 0x0D, logic.not_fun),
    instruction("AND", 0x0E, logic.and_fun),
    instruction("OR", 0x0F, logic.or_fun),
    instruction("COMP", 0x10, special.comp_fun),
    instruction("LOAD", 0x11, special.load_fun),
    instruction("PUSH", 0x12, special.push_fun),
    instruction("POP", 0x13, special.pop_fun),
]
