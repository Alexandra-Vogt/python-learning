#!/usr/bin/env python3

import ast

import prng
import crypt


def encrypt_file(key, file_path, keys):
    """Takes list of keys and converts it into a encrypted file."""
    try:
        key_file = open(file_path, "w")
        key_file.write(str(crypt.encrypt(str(keys), key)))
    except:
        newfile = input("Create new keyfile(Y/n)? ")
        if newfile != "n":
            key_file = open(file_path, "w+")
            key_file.write(str(crypt.encrypt(keys, key)))
        else:
            print("> ending program")
            exit(0)
    finally:
        key_file.close()


def decrypt_file(key, file_path):
    """Takes key and decrypts file."""
    keys = {}
    try:
        key_file = open(file_path, "r")
        decrypted_file = crypt.decrypt(ast.literal_eval(key_file.read()), key)
        keys = ast.literal_eval(decrypted_file)
    except:
        print("> error, file not found")
    finally:
        key_file.close()
    return keys


def menu(key, file_path, keys):
    quit_program = False
    print(key)
    print(file_path)
    print(keys)
    print("Choose option:")
    print("n -- newkey")
    print("f -- findkey")
    print("d -- deletekey")
    print("q -- quit")
    while not quit_program:
        try:
            choice = input("selection: ")
            if choice == "n":
                account = input("Account: ")
                key = input("Key: ")
                keys[account] = key
                print("> created account\n")
            elif choice == "f":
                account = input("Account: ")
                print("> " + keys[account] + "\n")
            elif choice == "d":
                account = input("Account: ")
                keys.pop(account)
                print("> account deleted\n")
            elif choice == "q":
                encrypt_file(key, file_path, keys)
                quit_program = True
            else:
                print("> parse error\n")
        except Exception as e:
            print("> " + str(e) + "\n")


file_path = input("Please enter keyfile location (default: keyfile.crypt): ")
key = input("Enter decryption key: ")

if not file_path:
    file_path = "keyfile.crypt"
keys = decrypt_file(key, file_path)
menu(key, file_path, keys)
