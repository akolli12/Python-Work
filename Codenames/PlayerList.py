from WordList import WordList
from termcolor import cprint, colored
from os import system

class PlayerList(WordList):

    def __init__(self, words):
        pcodes = 25 * ['_']
        self.__words = words
        self.__pcodes = pcodes

    def uncover(self, guess, spycodes):
        self.__pcodes = [spycodes[i] if guess == self.__words[i] else self.__pcodes[i] for i in range(0, len(self.__words))]

    def pcodes(self):
        return self.__pcodes

    def print_grid(self, spycodes):
        play_to_print = []
        color_code = {'R': 'red', 'B': 'blue', 'D': 'magenta', 'N': 'grey'}

        red_score = spycodes.count('R') - self.__pcodes.count('R')
        blue_score = spycodes.count('B') - self.__pcodes.count('B')
        
        for i in range(0, 25):
            word = self.__words[i]
            if self.__pcodes[i] != '_':
                textcolor = 'white'
                background = color_code[self.__pcodes[i]]
                play_to_print.append(colored(word.center(15), textcolor, 'on_' + background))
            else:
                textcolor = 'grey'
                play_to_print.append(colored(word.center(15), textcolor))
        WordList.printGrid(self, play_to_print, red_score, blue_score)
