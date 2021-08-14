import string
import random

def pas_gen(length = 8):
    str = string.ascii_letters+string.digits
    password = ''
    for char in range(length):
        char = random.choice(str)
        password += char
    return password

print(pas_gen())






