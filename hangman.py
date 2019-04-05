#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import getpass
import math
import string

g = 3
n = 1021 * 113
tries = 3
alphabet = list(string.ascii_lowercase)


def is_prime(num):
    num = abs(num)
    if num == 1:
        return False
    # 2 and 3 are prime
    if num < 4:
        return True
    if num % 2 == 0:
        return False
    # Even numbers discarded above
    if num < 9:
        return True
    if num % 3 == 0:
        return False
    limit = math.floor(math.sqrt(num))
    i = 5
    while i <= limit:
        if num % i == 0:
            return False
        if num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_n_primes(count, start=2):
    count = abs(count)
    if count == 0:
        return
    i = start
    found = 0
    while found < count:
        if is_prime(i):
            found += 1
            yield i
        i += 1


primes = find_n_primes(len(alphabet))
char_to_prime = dict(zip(alphabet, primes))


word_to_guess = getpass.getpass("Word to guess: ")
solution = ["_"] * len(word_to_guess)
print(" ".join(solution))

# This is our set S of primes
word_chars = []
for char in word_to_guess:
    word_chars.append((char, char_to_prime[char]))


prod = lambda x: functools.reduce(lambda x, y: x * y, x)
# This is g ^ S % n
accumulator_total = pow(g, prod([word_char[1] for word_char in word_chars]), n)
print("Accumulator total: %d\n" % accumulator_total)

while tries > 0:
    # our guess G (prime mapped from candidate char)
    guess_index, guess_char = int(input("Index: ").strip()), input("Char: ").strip().lower()
    if guess_index >= len(word_to_guess):
        print("Word is only %d letters long" % len(word_to_guess))
        print("%s\n" % " ".join(solution))
        continue
    print("You're guessing: index %d, char %s (maps to prime %d)" % (guess_index, guess_char, char_to_prime.get(guess_char, 0)))

    guess_char_exp = 1
    for i, char in enumerate(word_to_guess):
        if i != guess_index:
            guess_char_exp *= char_to_prime[char]
    # Compute i = g ^ O % n where O is S - G
    guess_char_proof = pow(g, guess_char_exp, n)
    print("Guessed character proof: %d" % guess_char_proof)

    if guess_char == word_to_guess[guess_index]:
        print("Yes, it's an %s!" % guess_char)
        solution[guess_index] = guess_char
    else:
        print("Nope, it's not an %s!" % guess_char)
        tries -= 1

    # This is i ^ G % n = (g ^ O ^ G) % n = g ^ S % n
    print("I didn't lie! Proof: %d, Accumulator total: %d" % (pow(guess_char_proof, char_to_prime.get(guess_char, 0), n), accumulator_total))
    print("%s\n" % " ".join(solution))

print("No more guesses! Word was: %s" % word_to_guess)
