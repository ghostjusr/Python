import string
import requests
import random

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

INTERNET_DOWNLOAD = False


class WordDict:
    '''World utils'''

    def __init__(self, wordlen: int = 5):
        self.wordlist = self.download_wordlist(wordlen=5)
        self.alphabet = set(string.ascii_lowercase)
        self.digits = set(string.digits)
        self.vowels = set("aeiou")
        self.consenents = self.alphabet.difference(self.vowels)

    def download_wordlist(self, wordlen: int = 5, remove_proper_nouns: bool = True):
        # download and curate default wordlist
        if INTERNET_DOWNLOAD:
            url = "https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
            r = requests.get(url, headers={'User-Agent': 'Custom'})
            wordlist = wordlist = r.content.decode('utf=8').split()
        else:
            filename = '/Users/stauffer/dev/stauffer/StaufferPlayground/PythonPlay/games/words/dict-eng-61k.txt'
            with open(filename, 'r') as f:
                wordlist = f.read().split()
        wordlist = [word for word in wordlist if len(word) == wordlen]
        if remove_proper_nouns:
            wordlist = [word for word in wordlist if word.lower() == word]
        return wordlist

    def remove(self, word):
        self.wordlist.remove(word)

    def get_random_word(self):
        """Get a random word"""
        return random.choice(self.wordlist)

    def __len__(self):
        return len(self.wordlist)
