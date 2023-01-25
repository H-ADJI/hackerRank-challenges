'''
File: pangrams.py
-----
Author: KHALIL HADJI 
'''
import string


def pangrams(s):
    used_alphabet = set(s.lower())
    print(used_alphabet)
    alphabet = set(string.ascii_lowercase)
    if alphabet.intersection(used_alphabet) == alphabet:
        return "pangram"
    return "not pangram"
