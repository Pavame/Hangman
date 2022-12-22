import random

# User will decide to start game w/ start_game() function

def start_game():  # function to begin game
    hang_man()
    start_op = input("START | EXIT | HIGH-SCORE\n")[0].upper()

    if start_op == 'S':                       # If user chooses to start game
        diff_level = input("Please select your difficulty level: \n Easy \n Medium \n Hard \n")[0].upper()
        if diff_level == 'E':                 # Easy difficulty
            print("EASY MODE - 3 LETTERS")
            blank_man()
            easy()
        elif diff_level == 'M':               # Medium difficulty
            print("MEDIUM MODE - 6 LETTERS")
            blank_man()
            medium()
        elif diff_level == 'H':               # Hard difficulty
            print("HARD MODE - 7 LETTERS")
            blank_man()
            hard()
        #elif diff_level == 'X':               # Extreme difficulty
         #   print("EXTREME MODE - 15 LETTERS")
         #   blank_man()
        else:                                 # If user chooses to exit game
            print("Exiting game. . . ")
    elif start_op == 'H':                     # If user chooses to view high-score
        pass  # Code high-score portion
    else:
        print("Exiting Game. . . ")           # If user types any other character, game exits

def hang_man():                               # Function that shows full hangman art
    print("H A N G M A N")
    print("   _______ ")
    print("  |    | ")
    print("  |    o ")
    print("  |   /|\ ")
    print("  |    | ")
    print("  |   / \ ")
    print(" _|_ ")
    print("|   |______ ")
    print("|          | ")
    print("|__________| ")
    print(f'===============')
def blank_man():                              # Displays empty/starter hangman canvas
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |          ')
    print(f'  |          ')
    print(f'  |          ')
    print(f'  |          ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')

def one_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |          ')
    print(f'  |          ')
    print(f'  |          ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
def two_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |    |     ')
    print(f'  |          ')
    print(f'  |          ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
def three_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |    |     ')
    print(f'  |    |     ')
    print(f'  |          ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
def four_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |   /|     ')
    print(f'  |    |     ')
    print(f'  |          ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
def five_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |   /|\    ')
    print(f'  |    |     ')
    print(f'  |          ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
def six_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |   /|\    ')
    print(f'  |    |     ')
    print(f'  |   /      ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
def seven_c():                              
    print(f'   _______   ')
    print(f'  |    |     ')
    print(f'  |    o     ')
    print(f'  |   /|\    ')
    print(f'  |    |     ')
    print(f'  |   / \    ')
    print(f' _|_         ')
    print(f'|   |______  ')
    print(f'|          | ')
    print(f'|__________| ')
    print(f'|__________| ')
    print(f'===============')
    replay = input("Oh no! You lost! \nWould you like to play again?")[0].upper()
    if replay == 'Y':
        start_game()
    else:
        quit()

def easy():                                   # Easy mode, level 1
    count = 0
    letters = []
    correct = []
    three_letters = ['CAT', 'DOG', 'FIG', 'SIT', 'URN', 'EAT', 'INK', 'AGO', 'EGO', 'ARK',
                     'FOG', 'GAP', 'IVY', 'NET', 'VAC', 'BIX', 'BAE', 'CHI', 'DRY', 'HOG',
                     'EMU', 'LIE', 'MAX', 'MIN', 'OAK', 'PEN', 'LOW', 'JAM', 'HUT', 'FAB']
    #three_letters = ['FEE', 'FEE', 'FEE', 'FEE', 'FEE', 'FEE', 'FEE', 'FEE', 'FEE', 'FEE'] Test same letter appearing mult times
    word = random.choice(three_letters)
    #print(word)                               # print word for testing; remove later
    x = '_'
    y = '_'
    z = '_'
    print(x + y + z)

    word_guessed = False

    while word_guessed == False:
        new_guess = input("Enter your guess: ")[0].upper()
        if new_guess in letters or correct:
            print("You guessed that letter already!")
        else:
            letters.append(new_guess)

        if new_guess in word:
            count = count
            correct.append(new_guess)
            print(f'This letter is in your word!')
            a = word.find(new_guess)
            if a == 0:
                x = new_guess
            elif a == 1:
                y = new_guess
            elif a == 2:
                z = new_guess
        else:
            print(f'Try again!')
            count = count + 1
            if count == 1:
                one_c()
            elif count == 2:
                two_c()
            elif count == 3:
                three_c()
            elif count == 4:
                four_c()
            elif count == 5:
                five_c()
            elif count == 6:
                six_c()
            elif count == 7:
                seven_c()

        print(x + y + z)
        print(f'GUESSED: {letters}')
        print(f'CORRECT: {correct}')

        if (x + y + z) == word:
            word_guessed = True
            print("You've guessed the correct word!")
            replay = input("Would you like to play again?")[0].upper()
            if replay == 'Y':
                start_game()
            else:
                quit()
def medium():                                       # Medium mode, level 1
    count = 0
    letters = []
    correct = []
    six_letters = ['ACTION', 'COURSE', 'DANGER', 'GOLDEN', 'INVEST', 'RANDOM', 'VOLUME', 'SYMBOL', 'MOSTLY', 'WINTER',
                   'QUEAZY', 'BANJAX', 'QUARTZ', 'HIJACK', 'JIMPLY', 'HABILE', 'HABITS', 'IAMBUS', 'JABIRU', 'JABOTS',
                   'MACERS', 'MACHES', 'NACHOS', 'PACIFY', 'XENIAL', 'YACHTS', 'UBIETY', 'TABERS', 'SABINS', 'PACERS']
    word = random.choice(six_letters)
    #print(word)                               # print word for testing; remove later
    x = '_'
    y = '_'
    z = '_'
    q = '_'
    r = '_'
    s = '_'
    print(x + y + z + q + r + s)
    
    word_guessed = False

    while word_guessed == False:
        new_guess = input("Enter your guess: ")[0].upper()
        if new_guess in letters or correct:
            print("You guessed that letter already!")
        else:
            letters.append(new_guess)

        if new_guess in word:
            count = count
            correct.append(new_guess)
            print(f'This letter is in your word!')
            a = word.find(new_guess)
            if a == 0:                                  # If letter guessed matches index 0, letter is in first position
                x = new_guess
            elif a == 1:                                # If letter guessed matches index 1, letter is in second position
                y = new_guess
            elif a == 2:
                z = new_guess
            elif a == 3:
                q = new_guess
            elif a == 4:
                r = new_guess
            elif a == 5:
                s = new_guess
        else:
            print(f'Try again!')
            count = count + 1
            if count == 1:
                one_c()
            elif count == 2:
                two_c()
            elif count == 3:
                three_c()
            elif count == 4:
                four_c()
            elif count == 5:
                five_c()
            elif count == 6:
                six_c()
            elif count == 7:
                seven_c()

        print(x + y + z + q + r + s)
        print(f'GUESSED: {letters}')
        print(f'CORRECT: {correct}')

        if (x + y + z + q + r + s) == word:
            word_guessed = True
            print("You've guessed the correct word!")
            replay = input("Would you like to play again?")[0].upper()
            if replay == 'Y':
                start_game()
            else:
                quit()
def hard():                                       # Medium mode, level 1
    count = 0
    letters = []
    correct = []
    seven_letters = ['OARFISH', 'QINDARS', 'SABOTED', 'UGLIEST', 'VACUITY', 'WACKILY', 'XANTHIC', 'ICEFALL', 'FABRICS', 'DABSTER',
                     'ABOLISH', 'ABSCOND', 'ACETIFY', 'ACOLYTE', 'BEARHUG', 'BEARISH', 'BEASTLY', 'CLUMPED', 'PENALTY', 'REBIRTH',
                     'SENDALS', 'SHACKLE', 'TENDRIL', 'UNLOCKS', 'VAMPIRE', 'WEARILY', 'YOWLERS', 'ZEALOUS', 'WINTERY', 'UNCAGED']
    word = random.choice(seven_letters)
    #print(word)                               # print word for testing; remove later
    x = '_'
    y = '_'
    z = '_'
    q = '_'
    r = '_'
    s = '_'
    t = '_'
    print(x + y + z + q + r + s + t)
    
    word_guessed = False

    while word_guessed == False:
        new_guess = input("Enter your guess: ")[0].upper()
        if new_guess in letters or correct:
            print("You guessed that letter already!")
        else:
            letters.append(new_guess)

        if new_guess in word:
            count = count
            correct.append(new_guess)
            print(f'This letter is in your word!')
            a = word.find(new_guess)
            if a == 0:                                  # If letter guessed matches index 0, letter is in first position
                x = new_guess
            elif a == 1:                                # If letter guessed matches index 1, letter is in second position
                y = new_guess
            elif a == 2:
                z = new_guess
            elif a == 3:
                q = new_guess
            elif a == 4:
                r = new_guess
            elif a == 5:
                s = new_guess
            elif a == 6:
                t = new_guess
        else:
            print(f'Try again!')
            count = count + 1
            if count == 1:
                one_c()
            elif count == 2:
                two_c()
            elif count == 3:
                three_c()
            elif count == 4:
                four_c()
            elif count == 5:
                five_c()
            elif count == 6:
                six_c()
            elif count == 7:
                seven_c()

        print(x + y + z + q + r + s + t)
        print(f'GUESSED: {letters}')
        print(f'CORRECT: {correct}')

        if (x + y + z + q + r + s + t) == word:
            word_guessed = True
            print("You've guessed the correct word!")
            replay = input("Would you like to play again?")[0].upper()
            if replay == 'Y':
                start_game()
            else:
                quit()

start_game()
