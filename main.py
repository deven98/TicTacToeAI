from board import Board
import os
from computer import AI

board = Board()

ai = AI(80000)
ai.iterate(board)


