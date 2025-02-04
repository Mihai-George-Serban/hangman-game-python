import random


hangman = "______\n|    |\n     |\n     |\n     |"


def play(word, lives):
    pass


play('Codecool', 6)


def random_word():
    var = random.choice(open('hangman-python-DanCristian81/countries-and-capitals.txt').read().split("\n"))
    var2 = var.split("|")
    return var2[1].strip()


the_word = random_word()


def hide_word(word):
    the_list = []
    for elem in word:
        if elem != " ":
            the_list.append("_")
        else:
            the_list.append(" ")
    return " ".join(the_list)


print(the_word)
print(hide_word(the_word))
# hide_word(the_word)
