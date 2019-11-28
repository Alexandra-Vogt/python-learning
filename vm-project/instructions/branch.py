def bu_fun(vm, dest):
    """Where dest is and address."""
    vm.EXP = dest


def be_fun(vm, dest):
    """Where dest is and address."""
    if vm.EF:
        vm.EXP = dest


def bg_fun(vm, dest):
    """Where dest is and address."""
    if vm.GF:
        vm.EXP = dest


def bl_fun(vm, dest):
    """Where dest is and address."""
    if vm.LF:
        vm.EXP = dest


def bz_fun(vm, dest):
    """Where dest is and address."""
    if vm.ZF:
        vm.EXP = dest
