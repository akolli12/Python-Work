from os import system
from termcolor import colored

class WordList:

    def __init__(self, words, codes):
        self.__words = words
        self.__codes = codes

    def countCodes(self, code):
        return self.__codes.count(code)

    def printGrid(self, list_to_print, red_score, blue_score):
        system("clear")
        print(colored(red_score, 'red'), '/', colored(blue_score, 'blue'), '\n\n')
    
        for i in range(0, 5):
            for j in range(0, 5):
                print(list_to_print[i*5 + j], end = "")
            print("\n")

