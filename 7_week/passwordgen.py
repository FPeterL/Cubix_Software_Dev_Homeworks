import random
import string
import os


def passwordgen(length):
    pass_chars = string.ascii_letters + string.digits + "!@#$%^&*()"


    password = ""
    for i in range(length):
        char = random.choice(pass_chars)
        password = password + char

    if length <= 8:
        print("Figyelem: A jelszó túl rövid lehet.")

    return password


# Nem használt változó
default_length = 12

print(passwordgen(10))