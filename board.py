class Board:

    def __init__(self):
        self.board = ([0,0,0] , [0,0,0] , [0,0,0])
        self.rows = 3
        self.columns = 3
        self.movesPlayed = 0
        self.playerPlaying = 1

#    #Player number is used to assign 1 or 2 as per the player
    def move(self, row, column):

        if self.isEmpty(row-1,column-1):

            self.board[row - 1][column - 1] = self.playerPlaying
            self.movesPlayed = self.movesPlayed + 1

            if self.playerPlaying is 1:
                self.playerPlaying = 2
            else:

                self.playerPlaying = 1
        else:
            print("Move invalid")


    def isEmpty(self, row, column):

        if self.board[row][column] == 0:
            return 1
        else:
            return 0

    def getMovesPlayed(self):

        return self.movesPlayed

    def isWin(self):

        if (((self.board[0][0] == 1 and self.board[0][1] == 1 and self.board[0][2] == 1) or (self.board[1][0] == 1 and self.board[1][1] == 1 and self.board[1][2] == 1) or (self.board[2][0] == 1 and self.board[2][1] == 1 and self.board[2][2] == 1) or (self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1) or (self.board[0][0] == 1 and self.board[1][0] == 1 and self.board[2][0] == 1) or (self.board[0][1] == 1 and self.board[1][1] == 1 and self.board[2][1] == 1) or (self.board[0][2] == 1 and self.board[1][2] == 1 and self.board[2][2] == 1))
		    or ((self.board[0][0] == 2 and self.board[0][1] == 2 and self.board[0][2] == 2) or (self.board[1][0] == 2 and self.board[1][1] == 2 and self.board[1][2] == 2) or (self.board[2][0] == 2 and self.board[2][1] == 2 and self.board[2][2] == 2) or (self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2) or (self.board[0][0] == 2 and self.board[1][0] == 2 and self.board[2][0] == 2) or (self.board[0][1] == 2 and self.board[1][1] == 2 and self.board[2][1] == 2) or (self.board[0][2] == 2 and self.board[1][2] == 2 and self.board[2][2] == 2))):

            return 1

        elif self.movesPlayed is 9 :

            return 2

        else:

            return 0

    def displayBoard(self):

        for x in self.board:
            print(x)

    def clearBoard(self):

        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.movesPlayed = 0