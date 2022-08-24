import random
import word_bank

word_bank = word_bank.WordBank()


class Card:

    def __init__(self):
        self.spanish_word = None
        self.english_word = None

    def get_next_pair(self):
        self.spanish_word = random.choice(list(word_bank.words_to_learn.keys()))
        self.english_word = word_bank.words_to_learn[self.spanish_word]



