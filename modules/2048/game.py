import enum
import random
import numpy as np
from vector import Vector
import enum

class GameStatus(enum.Enum):
    WIN = 'win'
    LOSE = 'lose'
    PLAY = 'play'

class Game:
    def __init__(self, size):
        self.__size = size
        self.__matrix = [[0]*size for _ in range(size)]
        self.completion()
        self.__points = 0
        self.status = GameStatus.PLAY

    @property
    def size(self):
        return self.__size

    @property
    def matrix(self):
        return self.__matrix

    @property
    def points(self):
        return self.__points


    def completion(self):
        r1 = random.randint(0, self.__size-1)
        c1 = random.randint(0, self.__size-1)
        r2 = random.randint(0, self.__size-1)
        c2 = random.randint(0, self.__size-1)
        while True:
            if (r1 != r2) and (c1 != c2):
                self.__matrix[r1][c1] = 2
                self.__matrix[r2][c2] = 2
                break
            else:
                r2 = random.randint(0, self.__size-1)
                c2 = random.randint(0, self.__size-1)

    def check_index(self, index):
        if index < 0 or index > len(self.__matrix)-1:
            return True

    def shift(self, v):
        self.remove_zeros(v)
        self.merge_clons(v)
        self.remove_zeros(v)
        self.random_two()

    def remove_zeros(self, v):
        for row in range(0, len(self.__matrix), 1):
            for col in range(0, len(self.__matrix[0]), 1):
                new_index = self.get_new_index(Vector(row, col), v)
                if self.__matrix[new_index.row][new_index.col] == 0:
                    continue
                x = self.__matrix[new_index.row][new_index.col]
                i = v.row
                j = v.col
                while (not(self.check_index(new_index.row + i)) and not(self.check_index(new_index.col + j))
                       and self.__matrix[new_index.row + i][new_index.col + j] == 0):
                    self.__matrix[new_index.row + i][new_index.col + j] = x
                    self.__matrix[new_index.row + i - v.row][new_index.col + j - v.col] = 0
                    i += np.sign(i)
                    j += np.sign(j)
                    if self.check_index(new_index.row + i) or self.check_index(new_index.col + j):
                        break

    def get_new_index(self, index, orientation):
        if orientation.row == 1:
            return Vector(len(self.__matrix) - 1 - index.row, index.col)
        if orientation.row == -1:
            return index
        if orientation.col == 1:
            return Vector(index.row, len(self.__matrix[0]) - 1 - index.col)
        if orientation.col == -1:
            return index

    def merge_clons(self, v):
        for row in range(len(self.__matrix)):
            for col in range(len(self.__matrix[0])):
                new_index = self.get_new_index(Vector(row, col), v)
                if self.check_index(new_index.row - v.row) or self.check_index(new_index.col - v.col):
                    break
                if self.__matrix[new_index.row][new_index.col] == self.__matrix[new_index.row - v.row][new_index.col - v.col]:
                    self.__matrix[new_index.row][new_index.col] *= 2
                    if self.__matrix[new_index.row][new_index.col] == 2048:
                        self.status = GameStatus.WIN
                    self.__points += self.__matrix[new_index.row][new_index.col]
                    self.__matrix[new_index.row - v.row][new_index.col - v.col] = 0

    def random_two(self):
        free_indexes = []
        for row in range(len(self.__matrix)):
            for col in range(len(self.__matrix[0])):
                if self.__matrix[row][col] == 0:
                    free_indexes.append(Vector(row,col))
        if len(free_indexes) == 0:
            self.status = GameStatus.LOSE
        else:
            index = random.choice(free_indexes)
            self.__matrix[index.row][index.col] = 2


def print_m(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end = ' ')
        print()
