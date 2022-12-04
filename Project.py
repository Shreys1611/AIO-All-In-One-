import time         # import time module
import random       # import random module
import math         # import math module
print("\nHello Welcome to AIO!!")
name = input("Enter your name: ")

print("\nWhat would you like to do?\n")
print("1. Play Hangman Game")
print("2. Play Tic-Tac-Toe Game")
print("3. Play Number Guessing Game")
print("4. Exit\n")

choice = int(input("Choose Your Option: "))

if (choice == 1):
    print("\nWelcome to Hangman game!!\n")      # Initial Steps to invite in the game:
    print("Hello " + name + "! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\n Let's play Hangman!")
    time.sleep(3)
    
    def main():         # The parameters we require to execute the game:
        global count
        global display
        global word
        global already_guessed
        global length
        global play_game
        words_to_guess = ["java","codetantra","computer","chair","table","program","mango","python","university","orange"]
        word = random.choice(words_to_guess)
        length = len(word)
        count = 0
        display = '_' * length
        already_guessed = []
        play_game = ""

    def play_loop():            # A loop to re-execute the game when the first round ends:
        global play_game
        play_game = input("Do You want to play again? y = yes, n = no \n")
        while play_game not in ["y", "n","Y","N"]:
            play_game = input("Do You want to play again? y = yes, n = no \n")
        if play_game == "y":
            main()
        elif play_game == "n":
            print("Thanks For Playing! We expect you back again!")
            time.sleep(4)
            exit()

    def hangman():          # Initializing all the conditions required for the game:
        global count
        global display
        global word
        global already_guessed
        global play_game
        limit = 5
        guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
        guess = guess.strip()
        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
            print("Invalid Input, Try a letter\n")
            hangman()

        elif guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
            print(display + "\n")

        elif guess in already_guessed:
            print("Try another letter.\n")

        else:
            count += 1

            if count == 1:
                time.sleep(1)
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

            elif count == 2:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

            elif count == 3:
                time.sleep(1)
                print("   _____ \n"
                     "  |     | \n"
                     "  |     |\n"
                     "  |     | \n"
                     "  |      \n"
                     "  |      \n"
                     "  |      \n"
                     "__|__\n")
                print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

            elif count == 4:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

            elif count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("Wrong guess. You are hanged!!!\n")
                print("The word was:",already_guessed,word)
                play_loop()

        if word == '_' * length:
            print("Congrats! You have guessed the word correctly!")
            play_loop()

        elif count != limit:
            hangman()

    main()
    hangman()

elif (choice == 2):
    print("\n\tTic-Tac-Toe Game\n\tIN PROGRESS")
    time.sleep(3)

elif (choice == 3):
    print("\nWelcome to Number Guessing game!!\n")
    print("Hello " + name + "! Best of Luck!")
    time.sleep(2)
    lower = int(input("Enter Lower bound:- "))          # Taking Inputs
    upper = int(input("Enter Upper bound:- "))
    print("The game is about to start!!")
    time.sleep(3)
    
    x = random.randint(lower, upper)    # generating random number between the lower and upper
    print("\n\tYou've got only",round(math.log(upper - lower + 1, 2)),"chances to guess the number!\n")
 
    count = 0   # Initializing the number of guesses.

    while count < math.log(upper - lower + 1, 2):   # for calculation of minimum number of guesses depends upon range
        count += 1
        guess = int(input("Guess a number:- "))

        if x == guess:  # Condition testing
            print("Congratulations you did it in",count,"tries")
            time.sleep(2)
            break   # Once guessed, loop will break

        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")

    # If Guessing is more than required guesses, show this output.
    if count >= math.log(upper - lower + 1, 2):
        print("\nThe number was %d" % x)
        print("\tBetter Luck Next time!")
        time.sleep(5)

elif (choice == 4):
    print("Thank You for using AIO!!")
    time.sleep(3)

else:
    print("You have put Wrong Input.\t[Try Between 1-4]")
    time.sleep(2)