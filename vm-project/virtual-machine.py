"""A basic virtual machine using my own custom assembly."""

from instructions import INSTRUCTION_TABLE


class VirtualMachine:
    """A basic virtual machine."""

    def __init__(self):
        self.memory = [None for i in range(0, 0x8000)]
        self.registers = {
            "ACC": 0,
            "ARA": 0,
            "ARB": 0,
            "ARD": 0,
            "EXP": 0,
            "SPB": 0,
            "SHP": 0,
        }
        self.flags = {"ZF": 0, "NF": 0, "OF": 0, "EF": 0, "GF": 0, "LF": 0}
        self.instructions = INSTRUCTION_TABLE

    def start_vm(self):
        """Start the virtual machine."""

    def stop_vm(self):
        """Stop the virtual machine."""

    def get_next_16_bytes(self):
        """This is a 16 byte"""
        execution_pointer = self.registers["EXP"]
        return self.memory[execution_pointer : execution_pointer + 16]
