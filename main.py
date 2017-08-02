from board import Board
import os
from computer import AI

board = Board()

numberOfIterations = int(input("Enter the number of iterations you want for the system : "))

ai = AI(numberOfIterations)
ai.iterate(board)
