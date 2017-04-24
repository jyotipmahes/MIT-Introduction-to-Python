# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
def partial(guessword,used):
    out=''
    for e in guessword:
        if e in used:
            out=out+e
        else:
            out=out+' _'
    return out
        

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
guessword=choose_word(wordlist)
print("Welcome to the game, Hangman!")
print("I am thinking of a word that is "+str(len(guessword))+" letters long.") 

nguess=8
unused=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
used=''
wordgussed=False 

while nguess>0 and not wordgussed:
    print('-------------------')
    print("You have "+str(nguess)+" left.")
    print("Available letters: "+''.join(unused))
    g=input('Please guess a letter: ')
    if not g.isalpha():
        print("Oops! Please enter only letters(a-z): "+partial(guessword,used))
    
    elif g not in unused:
        print("Oops! seems you have already used the letter: "+partial(guessword,used))
    elif g not in guessword:
        used=used+g
        nguess=nguess-1
        unused.remove(g)
        print("Oops! That letter is not in my word: "+partial(guessword,used))
    else:
        used=used+g
        print("Good guess: "+partial(guessword,used))
    if guessword==partial(guessword,used):
        wordguess=True
if wordgussed:
        print ('Congratulations, you won!')
else:
        print ('Game over.')
    
