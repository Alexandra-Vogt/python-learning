"""This module contains the arithmetic oriented."""


import binary


def add_fun(virtual_machine):
    """Where dest, a, and b are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    result = (
        virtual_machine.registers[a_register] + virtual_machine.registers[b_register]
    )
    if result // (2 ^ 64) != 0:
        virtual_machine.flags["OF"] = 1
    virtual_machine.registers[dest_register] = result % 2 ^ 64


def sub_fun(virtual_machine):
    """Where dest, a, and b_val are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    result = (
        virtual_machine.registers[a_register] - virtual_machine.registers[b_register]
    )
    if result // (2 ^ 64) != 0:
        virtual_machine.flags["OF"] = 1
    virtual_machine.registers[dest_register] = result % 2 ^ 64


def mul_fun(virtual_machine):
    """Where dest, a, and b_val are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    result = (
        virtual_machine.registers[a_register] * virtual_machine.registers[b_register]
    )
    if result // (2 ^ 64) != 0:
        virtual_machine.flags["OF"] = 1
    virtual_machine.registers[dest_register] = result % 2 ^ 64

def div_fun(virtual_machine):
    """Where dest, a, and b are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    result = (
        virtual_machine.registers[a_register] / virtual_machine.registers[b_register]
    )
    if result // (2 ^ 64) != 0:
        virtual_machine.flags["OF"] = 1
    virtual_machine.registers[dest_register] = result % 2 ^ 64


# These functions treat the numbers in the registers as my own absurd float format.
def fadd_fun(virtual_machine):
    """Where dest, a, and b are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    a_val = binary.to_float(virtual_machine.registers[a_register])
    b_val = binary.to_float(virtual_machine.registers[b_register])
    result = a_val + b_val
    virtual_machine.registers[dest_register] = binary.to_int(result)


def fsub_fun(virtual_machine):
    """Where dest, a, and b_val are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    a_val = binary.to_float(virtual_machine.registers[a_register])
    b_val = binary.to_float(virtual_machine.registers[b_register])
    result = a_val - b_val
    virtual_machine.registers[dest_register] = binary.to_int(result)


def fmul_fun(virtual_machine):
    """Where dest, a, and b are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    a_val = binary.to_float(virtual_machine.registers[a_register])
    b_val = binary.to_float(virtual_machine.registers[b_register])
    result = a_val * b_val
    virtual_machine.registers[dest_register] = binary.to_int(result)


def fdiv_fun(virtual_machine):
    """Where dest, a, and b are registers."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    a_register = binary.opcode_register_argument(virtual_machine, 2)
    b_register = binary.opcode_register_argument(virtual_machine, 3)
    a_val = binary.to_float(virtual_machine.registers[a_register])
    b_val = binary.to_float(virtual_machine.registers[b_register])
    result = a_val / b_val
    virtual_machine.registers[dest_register] = binary.to_int(result)
