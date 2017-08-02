

class OptimalCalc:

    def __init__(self):
        pass


    @staticmethod
    def mostPlayedMove(list):

        newList = []

        for game in list:
            newList.append(game[0])

        print(OptimalCalc.most_common(newList))


    @staticmethod
    def most_common(lst):
        return max(set(lst), key=lst.count)