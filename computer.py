
from random import randint

class AI:

    def __init__(self,iterations):

        self.winListPlayer1 = []
        self.winListPlayer2 = []
        self.iterations = iterations

        self.currentGame = []

    def iterate(self,Board):

        Board.move(1,1)
        Board.move(2,2)
        Board.move(3,3)

        pass

    def generateRandom(self):

        return randint(1,3)




