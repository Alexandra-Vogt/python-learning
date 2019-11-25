import prng
import mhash

PAD_END_MARKER = "END_PADDING"


def xor_message(message, key_sequence):
    xored_message = []
    for pair in zip(message, key_sequence):
        xored_message.append(pair[0] ^ pair[1])
    return xored_message


def pad_message(message):
    """Makes all messages fit in 1000 char blocks."""
    message += PAD_END_MARKER
    pad_length = 1000 - len(message) % 1000
    for val in prng.sequence(666, pad_length):
        message += chr(val % 1114112)
    return [ord(char) for char in message]


def crypt(message, key):
    key_sequence = prng.sequence(mhash.hash_string(key), len(message))
    return xor_message(message, key_sequence)


def encrypt(cleartext, key):
    return crypt(pad_message(cleartext), key)


def decrypt(ciphertext, key):
    cleartext_string = ""
    for val in crypt(ciphertext, key):
        cleartext_string += chr(val)
    return cleartext_string[0 : cleartext_string.find(PAD_END_MARKER)]
