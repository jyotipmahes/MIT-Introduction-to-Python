from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    word=hand.copy()
    glist=[]
    
    size=len(word)
  
    for i in range(1, size+1):
        
        perms = get_perms(hand, i)
        glist.extend(perms)
        
    mScore = 0
    mWord = None
    for word in glist:
        if word in glist:
            pscore = get_word_score(word, HAND_SIZE)
            if  pscore >  mScore:
                
                mScore =  pscore
                mWord = word
    return mWord
            

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    check= True
    word=hand.copy()
    total=0
    print("list of letter are ;")
    display_hand(word)
    while check:
        rep=comp_choose_word(word, word_list)
        if rep==None :
            print("All the possible choices are exhausted")
            print("Total score: "+str(total))
            check=False
        else:
            
            print("The choosen word is: "+rep)
            score=get_word_score(rep,HAND_SIZE)
            total=total+get_word_score(rep,HAND_SIZE)
            print(" The score of given word :"+str(score))
            word=update_hand(word, rep)
            print("The remaining letter in the hand are  : ")
            display_hand(word)
        
        
        
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    Check=True
    while Check:
        a=input(" Please enter 'n': For new hand or 'r': To play last hand or 'e': to exit :")
        if a=='n':
            hand=deal_hand(HAND_SIZE)
            play_hand(hand,word_list)
            Last=hand.copy()
            Check=True
        elif a=='r':
            play_hand(Last,word_list)
            Check=False
        elif a=='e':
            exit()
        else:
            print("Wrong value")
        b=input(" Please enter 'u': To play 'c': To let computer play")
        if b=='u':
            hand=deal_hand(HAND_SIZE)
            play_hand(hand,word_list)
            Last=hand.copy()
            Check=True
        elif b=='c':
            hand=deal_hand(HAND_SIZE)
            comp_play_hand(hand,word_list)
            Check=True
        else:
            print("Wrong value")
        
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
