"""This gets numbers."""


def set_num_64(vm, addr, num):
    """This sets an address range to a number."""


def get_num_64(vm, addr):
    """This gets a 64 bit number."""
    num = 0
    word = vm.memory[addr : addr + 8]
    i = 0
    while i < 8:
        num += word[i] + (256 * i)
    return num
