#Instructions for running the game on the terminal: $ python3 hangman.py

#Game instructions:
# 1. Incorrect guess letters are penalized once for each wrong letter.

# 2. 6 chances of wrong letters

# 3 If a letter is present multiple times. Guessing it once is enough.
# It shows up at all places.

# 4 Input game level from 1-4 easy, medium, had, superhard

import urllib.request as request
import numpy as np
import random
import os


target_url = "http://www.norvig.com/ngrams/sowpods.txt"
data = request.urlopen(target_url)

words=[]
for word in data:
    words.append(word.decode("utf-8").strip())

L=len(words)
#print(len(min(words, key = len) ))
word_list_e=[]
word_list_m=[]
word_list_h=[]
word_list_sh=[]

# putting words in 4 different list of easy, medium, hard and super-hard
for w in words:
    if len(w) <= 5:
        word_list_e.append(w)
    elif len(w)>5 and len(w) <= 8:
        word_list_m.append(w)
    elif len(w)>8 and len(w) <= 11:
        word_list_h.append(w)
    elif len(w)>11 and len(w) <= 15:
        word_list_sh.append(w)
Total_words=[word_list_e,word_list_m,word_list_h,word_list_sh]

class player:
    # input : has a name
    # input: guess letters
    # has number of chances
    # displays list of wrong letters already used
    # keeps players score for a current game(have not implemented)

    def __init__(self, n=input("Enter your name: ")):

        self.name = str(n)
        self.chance = 7
        self.all_wrong_guess=[]

    # inputs guess letter and calculates chances left

    def guess_letter(self,w):
        print("Incorrect guess so far: ",self.all_wrong_guess)
        print("chances left: ",self.chance -1)
        l = str(input("Enter letter: ")).upper()

        if l not in w.guess_word:
            if l not in self.all_wrong_guess:
                self.all_wrong_guess.append(l)
                self.chance = self.chance - 1


        return l



class word:

    # asks user for level of game from 1-4.
    # initiates game with a random word from that level.
    # checks if guess letter is correct, if yes then displayed
    # tracks correct guess letters
    def __init__(self):
        self.word_size = int(input("Enter level Number -> '1 = Easy: Len<=5',  '2 = Medium: Len<=8' ,  '3 = Hard: Len<=11' ,  '4 = Super-Hard: Len<=15' :  "))
        self.guess_word = ''
        self.random_word()
        #print(self.guess_word)

    # initiates random word from selected word level list

    def random_word(self):
        #self.guess_word = words[random.randint(0,L)]
        self.guess_word = Total_words[self.word_size-1][random.randint(0, len(Total_words[self.word_size-1]))]

    # displays correct guessed letters at correct position
    def correct_letter_pos(self, s):
        index = []
        for i in range(len(self.guess_word)):
            if self.guess_word[i] == s:
                index.append(i)
        return index

    # checks if guessed letters present in word
    def is_letter(self,s):
        if s in self.guess_word:
            return True
        else:
            return False



class display_word:
    # starts display word with blanks spaces
    # for each correct guess unmask letter
    # display all incorrectly guessed letters

    def __init__(self,w):
        self.word = w.guess_word
        self.letters = [i for i in self.word]
        self.word_len = len(self.letters)
        self.cells = [' ' for i in self.letters]

    # diplay cells for words
    def show_letters(self):
        str_print = ''
        for j in range(self.word_len):
            str_print += self.cells[j]+' ' + '|'
        print(str_print)

        print(''.join(['_'] * 3 * self.word_len))

    # update cell after every guess
    def update_cells(self,s,w):
        if w.is_letter(s):
            ind = w.correct_letter_pos(s)
            for i in ind:
                self.cells[i] = self.letters[i]






class display_hangman:
    # display hangman with every guess, has 7 states
    def __init__(self,p):
        self.options = self.all_options()
        self.p_chance =p.chance-1

    def all_options(self):

        o7 = """
        __________
        ||       |
        ||      ( )
        ||      _|_   
        ||     / | \\
        ||     _/ \_  
        ||     Oh No!
        """

        o6 = """
        __________
        ||       |
        ||      ( )
        ||      _|_   
        ||     / | \\
        ||     _/   
        ||     
        """

        o5 = """
        __________
        ||       |
        ||      ( )
        ||      _|_   
        ||     / | \\
        ||       
        ||     
        """
        o4 = """
        __________
        ||       |
        ||      ( )
        ||      _|_   
        ||     / | 
        ||       
        ||     
        """

        o3 = """
        __________
        ||       |
        ||      ( )
        ||      _|_   
        ||       
        ||       
        ||     
        """
        o2 = """
        __________
        ||       |
        ||      ( )
        ||         
        ||       
        ||       
        ||     
        """

        o1 = """
        __________
        ||       |
        ||     ALIVE
        ||         
        ||       
        ||       
        ||     
        """
        o = [o7, o6, o5, o4, o3, o2, o1]
        return o



    def show_hangman(self):

        print(self.options[self.p_chance])



class game:
    def __init__(self):
        self.G = self.start_game()
    # clears screen and shows current word cells and hangman state
    def reload_display_all(self, D, H):
        os.system("clear")
        print("Game in progress")
        D.show_letters()
        H.show_hangman()

    # main game loop runs until all 6 guess chances expire
    def start_game(self):
        P = player()
        print("Hi " + P.name + " !")
        W = word()
        D = display_word(W)
        H = display_hangman(P)
        self.reload_display_all(D,H)
        while True:

            D.update_cells(P.guess_letter(W), W)
            H = display_hangman(P)
            self.reload_display_all(D,H)
            self.did_win(D)
            self.is_game_over(P, W)

    # checks that if game won
    def did_win(self,D):
        if D.cells == D.letters:
            print("you won!")
            I = input("Do you want to play again? Y/N? ").upper()
            if I == 'Y':
                G = game()
            else:
                print("bye")
                exit()

    # checks if game over with all chances expired and word cells still empty
    def is_game_over(self,p,w):
        if p.chance == 1:
            print("you lost")
            print("your word was: ", w.guess_word)
            self.regame()

    # asks user for rematch after win or loss
    def regame(self):
        I= input("Do you want to play again? Y/N? ").upper()
        if I=='Y':
            G = game()
        else:
            print("bye")
            exit()


if __name__ == "__main__":

    G=game()
