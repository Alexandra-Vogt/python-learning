#!/usr/bin/env python3

import password


def test_password_with_string(string):
    hash_code, salt = password.get_hash_and_salt(string)
    assert password.is_password(string, salt, hash_code)
    assert not password.is_password(string + "foobar", salt, hash_code)


test_password_with_string("swordfish")
print("hash_password() passed")
