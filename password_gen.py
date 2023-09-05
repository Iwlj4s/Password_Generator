import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_password(length, chars, num_passwords):  # Generating One Password
    if not chars:
        raise ValueError("You must select at least one checkbox")

    passwords = []                                    # Generation Of The Required Number Of Passwords
    for _ in range(num_passwords):
        password = ''.join(random.choice(chars) for _ in range(length))
        passwords.append(password)

    return passwords

