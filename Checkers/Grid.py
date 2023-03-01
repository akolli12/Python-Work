from os import system
from Man import Man
from termcolor import colored
import string

class Grid:

    def __init__(self, background1, background2):

        self.__n = int(input('How many spaces long/wide do you want the grid to be? (Must be even and between 6 and 26): '))
        while (self.__n <= 6 and self.__n >= 26) or (self.__n % 2 == 1):
            print("Must be an even number between 6 and 26")
            self.__n = int(input('How many spaces long/wide do you want the grid to be? (Must be even and between 6 and 26): '))
            

        legalColors = ['grey', 'red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 'white']
        self.__background1 = background1
        self.__background2 = background2
        legalColors.remove(self.__background1)
        legalColors.remove(self.__background2)
        print("Your color options are:", end = " ")
        for color in legalColors:
            print(colored(color, color), end = '.' if color == legalColors[-1] else ", ")
        print(" ")
        self.__color1 = input("Pick a color from the listed options: ")
        while self.__color1 not in legalColors:
            print("Please pick a different color that is from the listed options.")
            self.__color1 = input("Pick a color from the listed options: ")
        self.__color2 = input("Pick another color from the listed options: ")
        while (self.__color2 not in legalColors) or (self.__color2 == self.__color1):
            self.__color2 = input("Please pick a different color from the listed options and cannot be " + colored(self.__color1, self.__color1) + '. ' + "Pick again: ")

        print("Your colors are " + colored(self.__color1, self.__color1) + " and " + colored(self.__color2, self.__color2) + '.')

        self.__men = self.spawnMen()

        self.__labels = self.labelGrid()

    def spawnMen(self):
        grid = []
        for i in range(1, self.__n + 1):
            for j in range(1, self.__n + 1):
                if (i + j) % 2 == 0:
                    grid.append(None)
                elif i <= 3:
                    grid.append(Man(self.__color1))
                elif i >= (self.__n - 2):
                    grid.append(Man(self.__color2))
                else:
                    grid.append(None)
        return grid
        
    def labelGrid(self):
        labels = []
        for row in range(1, self.__n + 1):
            for col in list(string.ascii_uppercase)[:self.__n]:
                labels.append(col + str(row))
        self.__labels = labels
        return labels

    def labels(self):
        return self.__labels

    def convert(self, position):
        index = self.__labels.index(position)
        return index

    def printGrid(self):
        print("".center(3),end = "")
        for i in range(self.__n):
             print(string.ascii_uppercase[i].center(7), end = '')
        print('')

        for i in range(len(self.__men)):
            # Get value of current man
            man = self.__men[i]
            # If we're about to start a row, then print a filler space row
            if i % self.__n == 0:
                print("".center(3), end = '')
                for j in range(self.__n):
                    background = self.__background1 if ((i // self.__n) + j) % 2 == 0 else self.__background2
                    print(colored("".center(7), "white", "on_" + background), end='')
                print('')
                print(str(i // self.__n + 1).center(3), end = '')
            # Getting the background color of the current spot
            background = self.__background1 if ((i // self.__n) + (i % self.__n)) % 2 == 0 else self.__background2
            
            # Print men line
            if man:
                print(colored("*".center(7), man.getColor(), "on_" + background), end='')
            else:
                print(colored("".center(7), "white", "on_" + background), end='')
        
            # If you're finishing a row, print another filler row
            if i % self.__n == (self.__n - 1):
                print('')
                print("".center(3), end = '')
                for j in range(self.__n):
                    background = self.__background1 if (i // self.__n + j) % 2 == 0 else self.__background2
                    print(colored("".center(7), "white", "on_" + background), end='')
                print('')
    def countMen(self):
        #Define empty color counts
        count1 = 0
        count2 = 0
        #Iterate through men grid
        for i in range(len(self.__men)):
            man = self.__men[i]
            #Check if men exists in spot
            if man and man.getColor() == self.__color1:
            #Add to appropriate color counts
                count1 += 1
            elif man and man.getColor() == self.__color2:
                count2 += 1
        return count1, count2

    def moveMan(self, initial, final, turn):
        # Check if final position is legal or what type of move it is
        move = self.moveType(initial, final, turn)
        if type(move) !=  type(" "): return move[1]
        
        self.__men[self.convert(final)] = self.__men[self.convert(initial)]
        self.killMan(self.convert(initial))
        if move == 'jump':
            self.killMan(int((self.convert(final) + self.convert(initial)) / 2))
        color = self.__men[self.convert(final)].getColor()
        row, col = self.convert2D(final)
        if color == self.__color1:
            if row == (self.__n - 1):
                self.__men[self.convert(final)].queen()
        elif color == self.__color2:
            if row == 0:
                self.__men[self.convert(final)].queen()

    def moveType(self, initial, final, turn):
        # Is it an odd row/column sum position?
        if sum(self.convert2D(final)) % 2 == 0:
            return False, f"Not a valid spot. Please only go on {self.__background2} spots."
        # Is there another piece there?
        index = self.convert(final)
        if self.__men[index] != None:
            return False, f"Another piece is on {final}"

        if not(self.__men[self.convert(initial)]):
            return False, f"no piece on {initial}."

        if turn != self.__men[self.convert(initial)].getColor():
            return False, f"it is {turn}'s turn."
        
        # Is it close? Is it a jump?
        rowF, colF = self.convert2D(final)
        rowI, colI = self.convert2D(initial)
        color = self.__men[self.convert(initial)].getColor()
        forward = 1 if color == self.__color1 else -1
        close = [1, -1] if self.__men[self.convert(initial)].isQueened() else [1 * forward]
        if self.checkPosition(close, [1, -1], rowF, colF, rowI, colI):
            return 'close'

        jump = [2, -2] if self.__men[self.convert(initial)].isQueened() else [2 * forward]
        if self.checkPosition(jump, [2, -2], rowF, colF, rowI, colI):
            # is there a man that we jumped over?
            jumpedOver = self.convertBack((rowF + rowI) / 2, (colF + colI) / 2)
            jumpman = self.__men[jumpedOver]
            if jumpman and jumpman.getColor() != color:
                return 'jump'
        return False, "illegal move"
    
    def checkPosition(self, rowS, colS, rowF, colF, rowI, colI):
        return ((rowF - rowI) in rowS) and ((colF - colI) in colS)

    def killMan(self, position):
        self.__men[position] = None

    def convert2D(self, position):
        index = self.convert(position)
        row = index // self.__n
        col = index % self.__n
        return row, col

    def convertBack(self, row, col):
        index = row * self.__n + col
        return int(index)

    def colors(self):
        return self.__color1, self.__color2
