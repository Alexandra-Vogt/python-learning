#!/usr/bin/env python3

import prng
import random


def slotmachine(betval):
    """This is a slot machine emulator."""
    slots = [":)", ":/", ":|", ":("]
    print(
        [slots[val % len(slots)] for val in prng.sequence(random.randrange(1, 20), 3)]
    )


def texas_holdem(betval):
    """This is a texas holdem emulator."""


slotmachine(200)
