from board import Board
import os
from computer import AI

board = Board()

ai = AI(500000)
ai.iterate(board)


