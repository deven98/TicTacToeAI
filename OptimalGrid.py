
class OptimalGrid:

    def __init__(self):

        self.grid = [[0,0,0],[0,0,0],[0,0,0]]

    def addToGridElement(self,row,column,value):

        self.grid[row-1][column-1] = self.grid[row-1][column-1] + value

    def displayOptimalGrid(self):

        print("Optimal grid is")

        for rows in self.grid:
            myFormattedList = ['%.2f' % elem for elem in rows]

            print(myFormattedList)

