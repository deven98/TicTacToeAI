

class OptimalCalc:

    def __init__(self):
        pass


    @staticmethod
    def mostPlayedMove(list):

        newList = []

        for game in list:
            newList.append(game[0])

        from collections import Counter

        c = Counter(newList)
        print (c.most_common(3))

        print(OptimalCalc.most_common(newList))
        print(newList.__sizeof__())


    @staticmethod
    def most_common(lst):
        return max(set(lst), key=lst.count)