"""This is the assembler."""

#!/usr/bin/env python3

from instructions import INSTRUCTION_TABLE

DIRECT_TRANSLATION_TABLE = {}


print("Thanks for using V-ASM.")
print("> building direct translation table from instruction table...")
for instruction in INSTRUCTION_TABLE:
    DIRECT_TRANSLATION_TABLE[instruction.symbol] = instruction.opcode
print("> building direct translation table from register table...")
print("> ")
print(DIRECT_TRANSLATION_TABLE)

DIRECT_TRANSLATION_TABLE = {
    # Registers
    "ACC": 0x0,
    "ARA": 0x1,
    "ARB": 0x2,
    "ARC": 0x3,
    "ARD": 0x4,
    "EXP": 0x5,
    "SBP": 0x6,
    "SHP": 0x7,
}

DATA_TRANSLATION_TABLE = {}



def tokenize(data):
    d


def parse_data_section(data_section, offset):
    for line in data_section.split("\n"):
        line


def parse_code_section(code_section, offset):
    for line in code_section.split("\n"):
        tokenized_line = line.split(" ")


lexer(input_string)

parser(tokens)
