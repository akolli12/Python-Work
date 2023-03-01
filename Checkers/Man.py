class Man:

    def __init__(self, color):

        self.__color = color
        self.__queen = False

    def isQueened(self):

        return self.__queen

    def queen(self):

        self.__queen = True

    def getColor(self):

        return self.__color
        
