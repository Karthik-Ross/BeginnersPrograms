import random
def hangman():
    word = random.choice(["superman", "spiderman", "flash", "thor", "Batman", "ironman", "cyborg", "antman", "aquaman", "groot", "wonderwoman", "venom"])
    validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word :
            print(main)
            print("Yeah, You Won..... Hurray!")
            break

        print("Guess the word : " , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid letter")
            guess = input()
        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left")
                print("  -----------  ")
            elif turns == 8:
                print("8 turns left")
                print("  -----------  ")
                print("       0       ")
            elif turns == 7:
                print("7 turns left")
                print("  -----------  ")
                print("       0       ")
                print("       |       ")
            elif turns == 6:
                print("6 turns left")
                print("  -----------  ")
                print("       0       ")
                print("       |       ")
                print("      /        ")
            elif turns == 5 :
                print("5 turns left")
                print("  -----------  ")
                print("       0       ")
                print("       |       ")
                print("      / \      ")
            elif turns == 4 :
                print("4 turns left")
                print("  -----------  ")
                print("     \ 0       ")
                print("       |       ")
                print("      / \      ")
            elif turns == 3 :
                print("3 turns left")
                print("  -----------  ")
                print("     \ 0 /     ")
                print("       |       ")
                print("      / \      ")
            elif turns == 2 :
                print("5 turns left")
                print("  -----------  ")
                print("     \ 0 / |   ")
                print("       |       ")
                print("      / \      ")
            elif turns == 1 :
                print("1 turns left")
                print("  -----------  ")
                print("Warning last chance,so choose wisely")
                print("     \ 0_|/    ")
                print("       |       ")
                print("      / \      ")
            elif turns == 0 :
                print("You Lost")
                print("You let a kind man die")
                print("   __________  ")
                print("       0_|     ")
                print("      /|\      ")
                print("      / \      ")
                break


name = input("Enter your name : ")
print("           Welcome  -----  ", name)
print("----------------------------------------------")
print("Try to guess the word in less than 10 attempts")
print("The words are DC and Avengers superheroes")
print()
hangman()
print("--------------------------")
