# utils.py
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Word and TermColor utils
# Use utils.TermColors["COLOR, REVERSE, NORMAL, BOLD, RESET, OR CLEARSCREEN GOES HERE"] 
# as a variable with the print() command
# TermColors["CLEARSCREEN"] completly clears the terminal
# Set INTERNET_DOWNLOAD to True if you have internet
# Set INTERNET_DOWNLOAD to False if you don't have internet
# If INTERNET_DOWNLOAD is False, set filename to the location of a dictionary file (A file with words, 1 per line)
# At the bottom it has the words = w.wordlist() function with the parameter for 'remove_proper_nouns'.
# Change this to either True or False to remove proper nouns or not.
#
# FUNCTIONS
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WordDict.wordlist(remove_proper_nouns: bool) - Returns a downloaded wordlist based on the INTERNET_DOWNLOAD variable and the first parameter

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
    "CLEARSCREEN": "\033[H\033[J",
}

INTERNET_DOWNLOAD = True


class WordDict:
    '''World utils'''

    def __init__(self, wordlen: int = 5):
        self.wordlist = self.download_wordlist(wordlen=5)
        self.alphabet = set(string.ascii_lowercase)
        self.digits = set(string.digits)
        self.vowels = set("aeiou")
        self.consenents = self.alphabet.difference(self.vowels)

    def wordlist(self, remove_proper_nouns: bool = True):
        if INTERNET_DOWNLOAD:
            url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
            r = requests.get(url, headers={'User-Agent': 'Custom'})
            wordlist = wordlist = r.content.decode('utf=8').split()
        else:
            with open(filename, 'r') as f:
                wordlist = f.read().split()
        wordlist = [word for word in wordlist if len(word) == wordlen]
        if remove_proper_nouns:
            wordlist = [word for word in wordlist if word.lower() == word]
        return wordlist

    def get_random_word(self):
        """Get a random word"""
        return random.choice(self.wordlist)

    def __len__(self):
        return len(self.wordlist)

w = WordDict()
words = w.wordlist(remove_proper_nouns=True)
