#!/usr/bin/env python3

# Standard Libary Imports
import random

# Insults tuple
INSULTS = (
    "lily-liver'd",
    "pigeon-liver'd",
    "lack gall",
    "scurvy",
    "pitiable",
    "foolish",
    "fat gutted",
    "rank",
    "moronic",
    "worm infested",
    "plague sore covered",
    "mindless",
    "fat as butter",
    "ugly",
    "revolting",
    "maggot covered",
    "cream faced",
    "damned",
    "satanic",
    "smooth tounge'd",
    "foul",
    "deformed",
    "sodden-witted"
    "base",
    "rascally",
    "bawdy",
    "lumpish",
    "fool-born",
    "fly-bitten",
    "goatish",
    "puny",
    "quailing",
    "reeky",
    "spleeny",
    "villainous",
    "fat faced",
    "slimy",
    "mangled",
    "rotten toothed",
    "lump headed",
    "perverted"
    )

# Heads tuple
HEADS = (
    "you",
    "defenestrate yourself,",
    "die,",
    "disappear,",
    "evade my vision,",
    "leave this place,",
    )

# Tails tuple
TAILS = (
    "trunk of humors",
    "dried gnat's-tongue",
    "parcel of dropsies",
    "worm",
    "elf-skin",
    "dick",
    "baffoon",
    "dingus",
    "fool",
    "vagabond",
    "loon",
    "scullion",
    "idiot",
    "villain",
    "pervert",
    "codpiece",
    "minnow",
    "wagtail",
    "puttock",
    "scut",
    "giglet",
    "clack-dish",
    "barnacle",
    "baggage",
    "coxcomb"
    )



def genSequence(sequenceLength, minval=0, maxval=1024):
    result = []
    while len(result) != sequenceLength:
        possibleVal = random.randrange(minval, maxval)
        if possibleVal not in result:
            result.append(possibleVal)
    return result

def makeInsultBody():
    sequence = genSequence(random.randrange(1, 8), maxval=len(INSULTS))
    insultTokens = [INSULTS[val] for val in sequence]
    insult = " ".join(insultTokens)
    return insult

def insultUser():
    head = random.choice(HEADS)
    tail = random.choice(TAILS)
    insult = head + " " + makeInsultBody() + " " + tail
    print(insult.capitalize() + "!")
    
    
while True:
    insultUser()
    input("> ")
