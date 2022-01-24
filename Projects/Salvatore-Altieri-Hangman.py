import random
word_list = ["Buenos Aires, Brasília, San Salvador, Cayenne, Sucre, Bogotá, Fort De France, Caracas, Santiago, Basse Terre"]

def get_world(world_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hang Hangman")
    print("Theme: Capitals of Latin America words")
    print(display_hangman(tries))
    print(word_completion)
    [print("\n")]
    while not guessed and tries > 0: 
        guess = input("Guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already tried", guess, "!")
            elif guess not in word:
                print("This isnt the word your looking for:(")
                tries -= 1
                guessed_letters.append(guess)

def display_hangman(tries):
    stages = [   """
                       --------
                       |    |
                       |    O
                       |   /|\\
                       |    |
                       |   / \\
                       -
                       """,
                       """
                        --------
                       |    |
                       |    O
                       |   /|
                       |    |
                       |   
                       -
                       """,
                       """
                        --------
                       |    |
                       |    O
                       |    |
                       |    |
                       |   
                       -
                       """,
                       """
                        --------
                       |    |
                       |    O
                       |   
                       |
                       |
                       -
                       """,
                       """
                        --------
                       |   |
                       |
                       |
                       |
                       |
                       -
                       """
]                  