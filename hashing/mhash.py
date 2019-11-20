"This is my hashing function."


def hash_string(string):
    "This returns a hash of the string of at most 64 bits in length."
    hash_code = 0
    vals = [ord(val) for val in string]
    i = 0
    while i < len(vals):
        hash_code += vals[i] * (56 ^ i)
        i += 1
    hash_code = hash_code % 9223372036854775807
    return hash_code
