import json


def get_words_to_learn():
    with open("data/words_to_learn.json", "r") as words_to_learn_file:
        words_to_learn = json.load(words_to_learn_file)
        return words_to_learn


def get_words_learned():
    with open("data/words_learned.json", "r") as words_learned_file:
        words_learned = json.load(words_learned_file)
        return words_learned


class WordBank:

    def __init__(self):
        self.words_to_learn = None
        self.words_learned = None
        self.words_to_learn_count = None
        self.words_learned_count = None
        self.get_progress()

    def get_progress(self):
        self.words_to_learn = get_words_to_learn()
        self.words_learned = get_words_learned()
        self.words_to_learn_count = len(self.words_to_learn)
        self.words_learned_count = len(self.words_learned)

    def reset_progress(self):
        empty_dict = {}
        with open("data/words_learned.json", "w") as words_learned_file:
            json.dump(empty_dict, words_learned_file)
        with open("data/words_database.json", "r") as words_database_file:
            words_database = json.load(words_database_file)
        with open("data/words_to_learn.json", "w") as words_to_learn_file:
            json.dump(words_database, words_to_learn_file, ensure_ascii=False, indent=4)
        self.get_progress()

    def word_learned(self, spanish_word):
        pair_learned = {spanish_word: self.words_to_learn[spanish_word]}
        self.words_learned.update(pair_learned)
        with open("data/words_learned.json", "w") as words_learned_file:
            json.dump(self.words_learned, words_learned_file, ensure_ascii=False, indent=4)
        del self.words_to_learn[spanish_word]
        with open("data/words_to_learn.json", "w") as words_to_learn_file:
            json.dump(self.words_to_learn, words_to_learn_file, ensure_ascii=False, indent=4)



