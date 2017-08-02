
from random import randint
from OptimalCalc import OptimalCalc
import sys

class AI:

    def __init__(self,iterations):

        self.winListPlayer1 = []
        self.winListPlayer2 = []
        self.iterations = iterations
        self.gamesPlayed = 0
        self.currentGame = []

#   Iterates the game the number of times the user specifies
    def iterate(self,Board):

        while(self.gamesPlayed < self.iterations):

            self.playGame(Board)
            Board.clearBoard()
            self.gamesPlayed = self.gamesPlayed + 1

        #f = open("games",'w')

        #for game in self.winListPlayer1:
          #  f.write(str(game))

        OptimalCalc.mostPlayedMove(self.winListPlayer1,self.winListPlayer2)

#   Generates random for board move
    def generateRandom(self):

        return randint(1,3)

#   Plays a single game and writes to the win list
    def playGame(self,board):

        gameState = 0
        self.currentGame = []

        while gameState is 0:

            i = self.generateRandom()
            j = self.generateRandom()

            if board.isEmpty(i-1,j-1) is 1:
                board.move(i,j)
                self.currentGame.append((i,j))

            gameState = board.isWin()

        if gameState is 1:
            #print("Win!")

            if board.playerPlaying is 2:
                self.winListPlayer1.append(self.currentGame)

            if board.playerPlaying is 1:
                self.winListPlayer2.append(self.currentGame)

        if gameState is 2:
            #print("Draw!")
            pass
