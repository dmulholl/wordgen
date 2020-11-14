#!/usr/bin/env python3

import sys
import wordgen


def add_words(generator, wordfile):
    with open(wordfile) as file:
        for line in file:
            word = line.strip().lower()
            if word and word.isalpha():
                generator.add_word(word)


def main():
    if len(sys.argv) == 1:
        print("Supply an argument to select a word source.")
        sys.exit()

    gen = wordgen.WordGenerator()

    # The English Open Word List. Approx. 129,000 words.
    # https://diginoodles.com/projects/eowl
    if 'eowl' in sys.argv:
        add_words(gen, './data/eowl.txt')

    # DWYL English word list. Approx. 465,000 words.
    # https://github.com/dwyl/english-words
    if 'dwyl' in sys.argv:
        add_words(gen, './data/dwyl.txt')

    # Mieliestronk's English word list. Approx. 58,000 words.
    # http://www.mieliestronk.com/wordlist.html
    if 'mielie' in sys.argv:
        add_words(gen, './data/mieliestronk.txt')

    # List of personal names. Approx. 8,600 words.
    # https://www.outpost9.com/files/WordLists.html
    if 'names1' in sys.argv:
        add_words(gen, './data/names-1.txt')

    # List of personal names. Approx. 20,000 words.
    # https://github.com/smashew/NameDatabases
    if 'names2' in sys.argv:
        add_words(gen, './data/names-2.txt')

    # List of English nouns. Approx. 6,750 words.
    # http://www.desiquintans.com/nounlist
    if 'nouns' in sys.argv:
        add_words(gen, './data/nouns.txt')

    for _ in range(25):
        word = gen.get_word()
        print(word)


if __name__ == '__main__':
    main()

