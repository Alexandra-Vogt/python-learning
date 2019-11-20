#!/usr/bin/env python3

# imports
import string
import random

# Module to be tested
import hashmap


def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_keyval(num):
    pairs = []
    for _ in range(num):
        pairs.append((generate_random_string(5), generate_random_string(20)))
    return pairs


def testHashmap(testmap):

    testmap.set_val("foo", "bar")
    assert testmap.get_val("foo") == "bar"
    try:
        testmap.set_val("foo", "blegh")
    except Exception:
        assert Exception == "duplicate key"

    for pair in generate_keyval(5000):
        try:
            testmap.set_val(*pair)
            assert testmap.get_val(pair[0]) == pair[1]
        except Exception:
            print("Duplicate key entered by automated test.")


testHashmap(hashmap.hashmap_chaining())
