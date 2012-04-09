#!/usr/bin/env python
"""Quick and dirty script for grabbing dictionary definitions from the Wordnik
API and printing them to the terminal.
"""

__author__ = "Robert Berry"
__email__ = "rjberry@gmail.com"

import sys

from wordnik import Wordnik

ARGUMENTS_ERROR = 1
API_KEY = "" # fill in

def define(client, word):
    defs = client.word_get_definitions(word)
    for i, definition in enumerate(defs):
        print "%d. %s" % (i + 1, definition['text'])

def usage():
    print "%s word" % sys.argv[0]
    exit(ARGUMENTS_ERROR)

def main():
    if len(sys.argv) != 2:
        usage()
    
    client = Wordnik(API_KEY)
    define(client, sys.argv[1])

if __name__ == "__main__": main()
