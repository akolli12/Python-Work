from WordList import WordList
import random
from termcolor import cprint, colored
from os import system

class SpymasterList(WordList):

    def __init__(self, words):
        extra = round(random.random())
        codes = (8 + extra) * ['R'] + (9 - extra) * ['B'] + 1 * ['D'] + 7 * ['N']
        random.shuffle(codes)
        assert(len(codes)==25)

        self.__words = words
        self.__codes = codes

    def codes(self):
        return self.__codes

    def print_grid(self, pcodes):
        spy_to_print = []
        color_code = {'R': 'red', 'B': 'blue', 'D': 'magenta', 'N': 'grey'}

        red_score = self.__codes.count('R') - pcodes.count('R')
        blue_score = self.__codes.count('B') - pcodes.count('B')
    
        for i in range(0, 25):
            word = self.__words[i]
            if pcodes[i] == '_':
                textcolor = color_code[self.__codes[i]]
                spy_to_print.append(colored(word.center(15), textcolor))
            else:
                textcolor = 'white'
                background = color_code[self.__codes[i]]
                spy_to_print.append(colored(word.center(15), textcolor, 'on_' + background))
        WordList.printGrid(self, spy_to_print, red_score, blue_score)

        
