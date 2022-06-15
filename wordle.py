# wordle
import random
words_5 = list(open('wordle-answers-alphabetical.txt', 'r'))
words_5 = list(map(lambda s: s.strip(), words_5))
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
count = 0
guesses = 0
score = 0
streak = 0
def wordleGame(): 
    print(color.BOLD + color.DARKCYAN + '\nWORDLE\n' + color.END)
    word = (words_5[random.randrange(0,len(words_5))]).lower()
    def guessingFunction():
        global count, guesses, score, streak       
        while True:
            try:
                word_guess = (input('Guess: ')).lower()
                if len(word_guess) != 5:
                    raise ValueError
                elif word_guess not in words_5:
                    raise ValueError
                break
            except ValueError:
                print(color.YELLOW + 'Guess must be 5 letters long & in the English dictionary' + color.END)
        if word_guess == word:
            print(color.GREEN + color.BOLD + word + '\n' + 'You Win!' + color.END)
            score += 1
            print(color.PURPLE + '\nScore: ' + color.BOLD + str(score) + color.END)
            streak += 1
            print(color.PURPLE + '\nStreak: ' + color.BOLD + str(streak) + color.END)
            count = 0
            guesses = 0
        elif word_guess != word:
            word_index = 0
            word_guess_ouput = []
            for letter in word_guess:
                if letter not in word:
                    word_index += 1
                    word_guess_ouput.append(letter)
                elif letter == word[word_index]:
                    word_index += 1
                    word_guess_ouput.append(color.GREEN + letter + color.END)
                    continue
                else:
                    word_guess_ouput.append(color.BLUE + letter + color.END)
                    word_index += 1
                    continue         
            count += 1
            guesses += 1
            print('Guess',str(guesses)+'/6:',"".join(word_guess_ouput))
            if count == 6:
                score += 0
                print(color.PURPLE + '\nScore: ' + color.BOLD + str(score) + color.END)
                streak = 0
                print(color.PURPLE + '\nStreak: ' + color.BOLD + str(streak) + color.END)
                print('\n' + color.RED + color.BOLD + 'You lose...\nThe correct word was:', color.UNDERLINE + color.YELLOW + word + color.END)
                count = 0
                guesses = 0
            else:
                guessingFunction()   
    guessingFunction()
    rerun = input('\nWould you like to play again?''\n(y/n): ')
    if rerun == 'y':
        wordleGame()
    else:
        print('Goodbye!\n')
        exit()
wordleGame()
