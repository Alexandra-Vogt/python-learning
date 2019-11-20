import random

# my imports
import mhash


def get_hash_and_salt(password):
    salt = random.randrange(0, 9223372036854775807)
    hash_code = mhash.hash_string(password) + salt % 9223372036854775807
    return hash_code, salt


def is_password(password, salt, hash_code):
    test_hash_code = mhash.hash_string(password) + salt % 9223372036854775807
    if hash_code == test_hash_code:
        return True
    else:
        return False
