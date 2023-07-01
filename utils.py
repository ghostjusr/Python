# utils.py
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Word and TermColor utils
# Use utils.TermColors["COLOR, REVERSE, NORMAL, BOLD, RESET"]
# as a variable with the print() command
# If you dont have internet, set the filename variable to the location of a dictionary file (A file with words, 1 per line)
# At the bottom it has the words = w.wordlist() function with the parameter for 'remove_proper_nouns'.
# Change this to either True or False to remove proper nouns or not.
#
# FUNCTIONS
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WordDict.wordlist(remove_proper_nouns: bool) - Returns a downloaded wordlist based on the INTERNET_DOWNLOAD variable and the first parameter.
# WordDict.get_random_word() - Randomly selects a word from the dictionary.
# clearterm()) – Clears the terminal of all text.

import string
import requests
import random
filename = ''

TermColors = {
    "RED": "\033[1;31m",
    "BLUE": "\033[1;34m",
    "CYAN": "\033[1;36m",
    "GREEN": "\033[0;32m",
    "YELLOW": "\033[0;33m",
    "WHITE": "\033[0;37m",
    "BLACK": "\033[1;30m",
    "RESET": "\033[0;0m",
    "BOLD": "\033[;1m",
    "REVERSE": "\033[;7m",
    "NORMAL": "\033[0;35m",
}

def clearterm():
    """ Clears the terminal the python project is running in.
    
    """
    print("\033[H\033[J")

alphabet = set(string.ascii_lowercase)
digits = set(string.digits)
vowels = set("aeiou")
consenents = alphabet.difference(vowels)

def wordlist(remove_proper_nouns: bool = True):
    """ Downloads and returns a wordlist from either online, or from a word file.
    
    """
    try:
        url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
        r = requests.get(url, headers={'User-Agent': 'Custom'})
        wordlist = wordlist = r.content.decode('utf=8').split()
    except:
        with open(filename, 'r') as f:
            wordlist = f.read().split()
    wordlist = [word for word in wordlist]
    if remove_proper_nouns:
        wordlist = [word for word in wordlist if word.lower() == word]
    return wordlist

def get_random_word():
    """Get a random word"""
    return random.choice(wordlist)

words = wordlist(remove_proper_nouns=True)
