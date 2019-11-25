def sequence(seed, length):
    """Uses LCG to make random numbers."""
    nums = []
    for i in range(length):
        seed = (1103515245 * seed + 12345) % 2147483648
        nums.append(seed)
    return nums
