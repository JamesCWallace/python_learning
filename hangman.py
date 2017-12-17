
def hangmangame():
    while True:
        import random
        import time

        # hangman
        print(" ")
        print(" ")
        print("Welcome to hangman!\nGuess the country\nOne letter at a time... before the hangman gets you")
        """ Generate list of words and pick one at random """
        words = []
        with open('hangmanwords.txt', 'r') as f:
            for line in f:
                if " " not in line and "-" not in line:
                    words.append(line.strip().lower())
        hangman = random.choice(words)


        # illustration for correct guesses

        drawing = (
            """
            -----
            |   |
            |
            |
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            |
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            |  -+-
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | 
            |  | 
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | 
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            | _| |_ 
            |
            --------
            """)

        # Show number of letters and eventually show
        # correct guesses and where they are in the word
        # i.e _ _ g _ e _

        hlist = []
        clue = []
        for e in hangman:
            hlist.append(e)
        for i in hlist:
            clue.append("_ ")

        # guess counter & list of correct guesses
        guesses = 1
        guessed = []
        to_guess = hlist
        play = True
        # Take input and make sure it's valid, print clue
        while play:
            print(" ")
            print(drawing[guesses - 1])
            for i in clue:
                print(i, end=" ")
            print(" ")
            guess = input("What letter do you guess? : ")
            result = "Incorrect"
            if len(guess) > 1:
                print("You can only guess one letter at a time! Try again.")
                result = " "
            if guess in guessed:
                print("You've already guessed that")
                result = " "
                # Now check if the guess is correct
            else:
                count = 0
                for e in to_guess:
                    if guess == e:
                        clue[count] = to_guess[count]
                        result = "Correct"
                    count += 1
            print(result)
            if clue == to_guess:
                print("Hooray! You got the whole word, well fucking done!!")
                print("\ (¬‿¬) /")
                play = False
            if result == "Incorrect":
                guesses += 1
            guessed.append(guess)
            if guesses == 11:
                print(drawing[-1])
                print("Too many guesses, you're dead! Try to be less pish next time")
                play = False
            time.sleep(1)
        print(" ")
        print(" ")
        play_again = input("Do you want to play again? : ")
        if play_again != "yes":
            return False


hangmangame()









