"""This module contains all branching instructions."""

import binary

def bu_fun(virtual_machine):
    """Where dest is and address."""
    dest = binary.opcode_address_argument(virtual_machine, 1)
    virtual_machine.EXP = dest


def be_fun(virtual_machine):
    """Where dest is and address."""
    dest = binary.opcode_address_argument(virtual_machine, 1)
    if virtual_machine.EF:
        virtual_machine.EXP = dest


def bg_fun(virtual_machine):
    """Where dest is and address."""
    dest = binary.opcode_address_argument(virtual_machine, 1)
    if virtual_machine.GF:
        virtual_machine.EXP = dest


def bl_fun(virtual_machine):
    """Where dest is and address."""
    dest = binary.opcode_address_argument(virtual_machine, 1)
    if virtual_machine.LF:
        virtual_machine.EXP = dest


def bz_fun(virtual_machine):
    """Where dest is and address."""
    dest = binary.opcode_address_argument(virtual_machine, 1)
    if virtual_machine.ZF:
        virtual_machine.EXP = dest
