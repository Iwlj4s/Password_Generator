import random


def generate_password(length, chars):  # Generating One Password
    random.shuffle(list(chars))
    password = ''.join(random.choice(chars) for _ in range(length))

    return password


