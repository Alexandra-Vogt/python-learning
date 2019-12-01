"""This contains the special functions"""

import binary

def comp_fun(virtual_machine):
    """This compares the two specified registers."""
    register_a = binary.opcode_register_argument(virtual_machine, 1)
    register_b = binary.opcode_register_argument(virtual_machine, 2)
    value_a = virtual_machine.registers[register_a]
    value_b = virtual_machine.registers[register_b]
    if value_a == value_b:
        virtual_machine.flags["EF"] = 1
    else:
        virtual_machine.flags["EF"] = 0


def load_fun(virtual_machine):
    """This loads the address specified into a register."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    source_addr = binary.opcode_address_argument(virtual_machine, 2)
    source_val = binary.get_int_64(virtual_machine, source_addr)
    virtual_machine.registers[dest_register] = source_val

def pull_fun(virtual_machine):
    """This pulls the register specified into an address."""
    dest_addr = binary.opcode_address_argument(virtual_machine, 1)
    source_register = binary.opcode_address_argument(virtual_machine, 9)
    source_val = virtual_machine.registers[source_register]
    binary.set_int_64(virtual_machine, dest_addr, source_val)

def psh_fun(virtual_machine):
    """This pushes the register provided onto the stack."""
    source_register = binary.opcode_register_argument(virtual_machine, 1)
    stack_head = virtual_machine.registers["SHP"]
    virtual_machine.stack[stack_head] = virtual_machine.registers[source_register]
    virtual_machine.registers["SHP"] += 1


def pop_fun(virtual_machine):
    """This pops the top value from the stack and places it in an register."""
    dest_register = binary.opcode_register_argument(virtual_machine, 1)
    stack_head = virtual_machine.registers["SHP"]
    virtual_machine.registers[dest_register] = virtual_machine.stack[stack_head]
    virtual_machine.registers["SHP"] -= 1
