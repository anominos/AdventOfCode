# flake8: noqa
from copy import deepcopy

class GridFunc:
    @staticmethod
    def rotate_grid(grid:list[list]):
        return list(zip(*grid[::-1]))

    @staticmethod
    def iter_horiz(grid: list[list]):
        for y in grid:
            yield y

    @staticmethod
    def iter_vert(grid: list[list]):
        grid = GridFunc.rotate_grid(grid)
        yield from GridFunc.iter_horiz(grid)

    @staticmethod
    def iter_maindiag(grid: list[list]):
        """
        a b c       c
        d e f  ->  b f
        g h i     a e i
                   d h
                    g
        """
        for start in range(len(grid[0])-1, 0, -1):
            cx, cy = start, 0
            l = []
            while 0<=cy<len(grid) and 0<=cx<len(grid[cy]):
                l.append(grid[cy][cx])
                cx+=1
                cy+=1
            yield l

        for start in range(len(grid)):
            cx, cy = 0, start
            l = []
            while 0<=cy<len(grid) and 0<=cx<len(grid[cy]):
                l.append(grid[cy][cx])
                cx+=1
                cy+=1
            yield l

    @staticmethod
    def iter_antidiag(grid: list[list]):
        """
        a b c       a
        d e f  ->  d b
        g h i     g e c
                   h f
                    i
        """
        grid = GridFunc.rotate_grid(grid)
        yield from GridFunc.iter_maindiag(grid)

    @staticmethod
    def iter_cardinal(grid):
        yield from GridFunc.iter_horiz(grid)
        yield from GridFunc.iter_vert(grid)

    @staticmethod
    def iter_diag(grid):
        yield from GridFunc.iter_maindiag(grid)
        yield from GridFunc.iter_antidiag(grid)

    @staticmethod
    def iter_adj(grid):
        yield from GridFunc.iter_cardinal(grid)
        yield from GridFunc.iter_diag(grid)
