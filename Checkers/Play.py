from Grid import Grid
from os import system

class Play:

    def __init__(self):

        self.playcheckers()

    def playcheckers(self):
        
        g = Grid('red', 'blue')
        error = None
        colors = g.colors()
        turn = 0
        while not(0 in g.countMen()):
            system("clear")
            g.printGrid()
            print('')

            if error: print(error)
            initialp = input('what is the position of the piece you want to move? ')
            if not(initialp in g.labelGrid()):
                initialp = input('not a valid position. what is the position of the piece you want to move? ')
            finalp = input('where would you like to move it? ')
            if not(finalp in g.labelGrid()):
                finalp = input('not a valid position. where would you like to move it? ')
            error = g.moveMan(initialp, finalp, colors[turn])
            if not(error):
                turn = 1 - turn
                
        
        
        
