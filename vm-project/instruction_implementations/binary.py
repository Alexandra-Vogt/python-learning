"""These are assorted functions for general purpose computation."""

import math

def offset_from_register(virtual_machine, register, offset):
    """Gets offset from the number stored in a register."""
    register_address = virtual_machine.registers[register] + offset
    return register_address


def opcode_register_argument(virtual_machine, offset):
    """Translates the offset from the execution pointer into a register name."""
    registers = ["ACC", "ARA", "ARB", "ARC", "ARD", "EXP", "SBP", "SHP"]
    address = virtual_machine.registers["EXP"] + offset
    byte = virtual_machine.memory[address]
    return registers[byte]



def to_float(number):
    """Converts a number to a float."""
    exponent = (number // (2 ^ 53)) - 1024
    fraction = number % (2 ^ 53)
    return fraction * (2 ^ exponent)



def to_int(number):
    """Converts a float to an int that can be stored in a register"""
    exponent = (math.log(number, 2) + 1024) // 1
    fraction = number % 2 ^ 53
    return exponent * 2 ^ 53 + fraction


def set_int_64(virtual_machine, address, num):
    """This sets a range from address to address + 7 to a number."""
    i = 0
    while i < 8:
        if i == 0:
            virtual_machine.memory[address + 1] = num % 256
        else:
            virtual_machine.memory[address + i] = (num // i) % 256


def get_int_64(virtual_machine, address):
    """This gets a 64 bit number."""
    num = 0
    word = virtual_machine.memory[address : address + 7]
    i = 0
    while i < 8:
        num += word[i] + (256 * i)
    return num


def opcode_address_argument(virtual_machine, offset):
    """Translates the offset from the execution pointer into an address."""
    argument = virtual_machine.registers["EXP"] + offset
    return get_int_64(virtual_machine, argument)
