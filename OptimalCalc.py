from OptimalGrid import OptimalGrid
import os

class OptimalCalc:

    def __init__(self):
        pass


    @staticmethod
    def mostPlayedMove(winList, lossList):

        opGrid = OptimalGrid()

        formattedWinList = []

        formattedLossList = []

        for game in winList:

            #Remove comments of the next lines if you want to see the display in action in console!Note:Slows down execution
            #os.system('cls')
            #opGrid.displayOptimalGrid()
            formattedWinList.append(game[0])
            opGrid.addToGridElement(game[0][0],game[0][1],0.001)

        #for game in lossList:

            #Remove comments of the next lines if you want to see the display in action in console!Note:Slows down execution
            # os.system('cls')
            # opGrid.displayOptimalGrid()
            # formattedLossList.append(game[0])
            # opGrid.addToGridElement(game[0][0], game[0][1], -0.0005)


        from collections import Counter

        c = Counter(formattedWinList)
        print (c.most_common(3))

        print(OptimalCalc.most_common(formattedWinList))
        print(formattedWinList.__sizeof__())

        opGrid.displayOptimalGrid()



    @staticmethod
    def most_common(lst):
        return max(set(lst), key=lst.count)