"""A basic virtual machine using my own custom assembly."""

import instructions

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

    def step(self):
        """Move execution forward by one step"""

    def 
