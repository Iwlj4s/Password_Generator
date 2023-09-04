import random
import main


def generate_password(length, chars):  # Generating One Password
    random.shuffle(list(chars))
    password = ''.join(random.choice(chars) for _ in range(length))

    return password


#for _ in range(number_of_passwords_to_generate):  # Generation Of The Required Number Of Passwords
 #   password = generate_password(password_length, chars)
