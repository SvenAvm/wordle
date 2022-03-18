import sys
from valid_words import valid_words
import random

CHOSEN_WORD = random.choice(valid_words)
GUESS_COUNT = 6

class Color:
    PREIFIX = "\033"
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    c = "p"
    PERSISTENT_COLORS = [RED, GREEN]

class GuessWord:
    counter = 1
    used_words = []
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }

    def __init__(self, w_str: str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""

    def jump_turn(self):
        GuessWord.counter += 1

    def is_valid(self):
        return self.w_str in valid_words

    def apply_green(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = CHOSEN_WORD[i]
            guess_char = self.w_chars[i]
            if actual_char == guess_char:
                colored_char = f"{Color.GREEN}{actual_char}{Color.BASE}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(actual_char, colored_char)

    def apply_yellow(self):
        for i, _ in enumerate(self.w_chars):
            guess_char = self.w_chars[i]
            guessed_char_is_not_green = Color.GREEN not in GuessWord.alphabet.get(guess_char, "")
            if guess_char in CHOSEN_WORD and guessed_char_is_not_green:
                colored_char = f"{Color.YELLOW}{guess_char}{Color.BASE}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(guess_char, colored_char)
            else:
                colored_char = f"{Color.RED}{guess_char}{Color.BASE}"
                self.edit_alphabet(guess_char, colored_char)

    def apply_guesses(self):
        self.apply_green()
        self.apply_yellow()
        self.post_guess_w_str = "".join(self.w_chars)
        GuessWord.used_words.append(self.post_guess_w_str)
        print(self.post_guess_w_str)

    def check_perfect_guess(self):
        if self.w_str == CHOSEN_WORD:
            print(f"Congratulations! you beat Wordle in {GuessWord.counter} valid attempt/s, with {6 - GuessWord.counter} attempt/s remaining!")
            for element in GuessWord.used_words:
                print("attempt: ", element)
            sys.exit(1)

    def check_game_loss(self):
        if GuessWord.counter == GUESS_COUNT + 1:
            print(f"You lost the game, The word was {CHOSEN_WORD}.")
            sys.exit(1)

    def edit_alphabet(self, k, v):
        if k not in GuessWord.alphabet.keys():
            # new key value pair being added
            return
        # do not modify key value pairs that are already green or red
        older_value = GuessWord.alphabet.get(k, "")
        modify_color = True
        for c in Color.PERSISTENT_COLORS:
            if c in older_value:
                modify_color = False

        if modify_color:
            GuessWord.alphabet[k] = v