#!/usr/bin/env python

import string


alphabet = list(string.ascii_lowercase)


def increment_password(pw):
    password = list(pw)
    password.reverse()

    for index, char in enumerate(password):
        new_index = (alphabet.index(char) + 1) % len(alphabet)
        password[index] = alphabet[new_index]

        if char != "z":
            break

    password.reverse()
    return "".join(password)


def is_valid(pw):
    return (
        not has_bad_chars(pw)
        and has_straight(pw)
        and has_dual_pairs(pw)
    )


def has_straight(pw):
    for i in range(len(pw) - 2):
        if pw[i:i + 3] in "".join(alphabet):
            return True

    return False


def has_dual_pairs(pw):
    pairs = set()
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1]:
            pairs.add(pw[i])

    return len(pairs) >= 2


def has_bad_chars(pw):
    return any(letter in pw for letter in ["i", "o", "l"])


password = input()

# find first password for part 1
while not is_valid(password):
    password = increment_password(password)
print(password)

# find next password for part 2
password = increment_password(password)
while not is_valid(password):
    password = increment_password(password)
print(password)
