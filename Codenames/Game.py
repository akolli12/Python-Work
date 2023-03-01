from WordList import WordList
from PlayerList import PlayerList
from SpymasterList import SpymasterList
import random
import sys

class Game():

    def __init__(self, filename):

        words = self.read_txt(filename)
        random.shuffle(words)
        self.__words = words[0:25]

    def newWords(self, filename):

        words = self.read_txt(filename)
        random.shuffle(words)
        self.__words = words[0:25]
        
    def read_txt(self, filename):
        
        f = open(filename, "r")
        list1 = [] 
        for line in f:
            list1.append(line[:-1])
        f.close()
        return list1

    def words(self):
        return self.__words

    def check_end_game(self, spy, player):
    # check death word
        spycodes = spy.codes()
        playercodes = player.pcodes()
        death = [i for i in playercodes if i == 'D']
        if len(death) > 0:
            return death
    # check if red has all codes
        ctrr = 0
        for i in playercodes:
            if i == 'R':
                ctrr += 1
        if ctrr == spycodes.count('R'):
            return 'R'
    # check if blue has all codes
        ctrb = 0
        for i in playercodes:
            if i == 'B':
                ctrb += 1
        if ctrb == spycodes.count('B'):
            return 'B'
        return 'none'

    def playagain(self, filename):
        again = input("do you want to play again (y or n): ")
        if again == 'y':
            self.newWords(filename)
            self.playgame(filename)
        else:
            print('thanks for playing!')

    def playgame(self, filename):
        player = PlayerList(self.__words)
        spy = SpymasterList(self.__words)
        while self.check_end_game(spy, player) == 'none':
        # print grid
            player.print_grid(spy.codes())
        # ask for guess
            guess = input("guess a word or press enter to switch lists: ").strip()
            if guess == '':
                spy.print_grid(player.pcodes())
                hello = input("press enter to switch back to player mode: ")
            else:
        # uncover fn with the guess and update playerlist
                player.uncover(guess, spy.codes())
        # print updated grid
            player.print_grid(spy.codes())
        # display score
        
    # print some game over message - congratulate winner or point out death word
        print("game over!", end = " ")
        if self.check_end_game(spy, player) == 'R':
            print("congratulations red team!!")
        elif self.check_end_game(spy, player) == 'B':
            print("congratulations blue team!!")
        else:
            print("the death word was " + guess + ".")
    # play again
        self.playagain(filename)
