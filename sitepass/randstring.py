from random import choice
from string import \
    hexdigits, ascii_letters, ascii_lowercase, ascii_uppercase, digits

alpha = ascii_letters
lower = ascii_lowercase
upper = ascii_uppercase
hex = hexdigits
alphanum = digits + ascii_letters

def randstring(charset, length):
    chars = []
    for x in range(length):
        chars.append(choice(charset))
    return ''.join(chars)
