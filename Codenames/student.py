# CODENAMES WITH CLASSES

class Tennis:

    def __init__(self, name, utr, opponent, result, hours, goal):
        self.__name = name
        self.__utr = utr
        self.__opponent = opponent
        self.__result = result
        self.__hours = hours
        self.__goal = goal

    def changeUTR(self, result):
        if result == "win" and self.__utr < self.__opponent:
            self.__utr += 0.2
        elif result == "loss" and self.__utr > self.__opponent:
            self.__utr = self.__utr - 0.2
        else:
            self.__utr = self.__utr

    def increaseUTR(self, hours):
        self.__utr = self.__utr + (hours * .01)

    def UTR(self):
        return self.__utr

    def setGoal(self, goal):
        hours = (goal - self.__utr) * 100
        print("To get to " + str(goal) + ", you must practice " + str(round(hours)) + " hours.")

                 # four class variables
                 # two getters
                 # two setters

    
