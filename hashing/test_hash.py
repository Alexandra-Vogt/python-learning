#!/usr/bin/env python3

import mhash

assert mhash.hash_string("blegh")
assert mhash.hash_string("blegh") != mhash.hash_string("hgelb")
print("mhash hashes things, probably")
