import wordle
import os

os.system("cls") if os.name == "nt" else os.system("clear")

starting_message = """
'##:::::'##::'#######::'########::'########::'##:::::::'########:
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##: ##::::::: ##:::::::
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##: ##::::::: ######:::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##: ##::::::: ##:::::::
. ###. ###::. #######:: ##:::. ##: ########:: ########: ########:
:...::...::::.......:::..:::::..::........:::........::........::

Type "h" to see the entire alphabet, 
with guessed letters colored appropriately

"""

print(starting_message.replace("#", f"{wordle.Color.GREEN}#{wordle.Color.BASE}"))

if __name__ == "__main__":
    with open("cheat.txt", "w") as f:
        f.write(wordle.CHOSEN_WORD)
    while True:
        guess = wordle.GuessWord(
             w_str=input(f"attempt #{wordle.GuessWord.counter} >")
        )
        if guess.w_str == "h":
            list_values = list(wordle.GuessWord.alphabet.values())
            for element in list_values:
                print(element, end=" " if list_values[-1] != element else "\n")
            continue
        if guess.is_valid():
            guess.apply_guesses()
            guess.check_perfect_guess()
            guess.jump_turn()
            guess.check_game_loss()
