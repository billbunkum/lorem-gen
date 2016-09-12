from random import choice, randint

class Lorem():
    def __init__(self, words_file):
        with open(words_file, 'r') as lorem_file:
            all_lorem_text = lorem_file.read()

        self.words = all_lorem_text.split(" ")

    def get_lorem(self, min_words, max_words):
        rand_words = randint(min_words, max_words)
        selected_words = [
            choice(self.words)
            for x in range(rand_words)
        ]

        return cap_start(selected_words)

def cap_start(words):
    end_marks = [ "!", "?", "," "." ]
    new_words = []

    previous_word = ""
    for word in words:
        new_word = (word.title() if previous_word[-1:] in end_marks else word)

        previous_word = word
        new_words.append(new_word)

    return " ".join(new_words)