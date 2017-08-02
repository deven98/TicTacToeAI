from OptimalGrid import OptimalGrid

class OptimalCalc:

    def __init__(self):
        pass


    @staticmethod
    def mostPlayedMove(list):

        opGrid = OptimalGrid()

        newList = []

        for game in list:
            newList.append(game[0])
            opGrid.addToGridElement(game[0][0],game[0][1],0.001)

        from collections import Counter

        c = Counter(newList)
        print (c.most_common(3))

        print(OptimalCalc.most_common(newList))
        print(newList.__sizeof__())

        opGrid.displayOptimalGrid()



    @staticmethod
    def most_common(lst):
        return max(set(lst), key=lst.count)