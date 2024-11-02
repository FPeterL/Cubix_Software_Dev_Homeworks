"""This module contains a function to generate a random password."""

import random
import string


def passwordgen(length):
    """Generate a random password with a given length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    pass_chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = ""
    for _ in range(length):
        char = random.choice(pass_chars)
        password += char

    if length <= 8:
        print("Attention!: The password may be too short!")
    return password


print(passwordgen(10))
