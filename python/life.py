#!/usr/bin/env python


from collections import defaultdict


Cells = lambda: defaultdict(lambda: defaultdict(int))


def neighbors(x, y):
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
            (x - 1, y),                 (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def cell_value(cells, x, y):
    return cells[x][y]

def count_neighbors(cells, x, y):
    nw = cells[x - 1][y - 1]
    n = cells[x][y - 1]
    ne = cells[x + 1][y - 1]
    w = cells[x - 1][y]
    e = cells[x + 1][y]
    sw = cells[x - 1][y + 1]
    s = cells[x][y + 1]
    se = cells[x + 1][y + 1]
    return nw + n + ne + w + e + sw + s + se

def dump(cells, n):
    for x in xrange(n):
        print ' '.join('.#'[cells[x][y]] for y in xrange(n))


def cells_next(cells):
    result = Cells()
    for x, row in cells.items():
        for y, alive in row.items():
            if alive:
                n = count_neighbors(cells, x, y)
                if n == 2 or n == 3:
                    result[x][y] = 1
            for n in neighbors(x, y):
                if cells[x][y] == 0:
                    n = count_neighbors(cells, x, y)
                    if n == 3:
                        result[x][y] = 1
    return result


def blinker():
    c = Cells()
    c[2][1] = 1
    c[2][2] = 1
    c[2][3] = 1
    return c


def glider():
    c = Cells()
    c[0][1] = 1
    c[1][2] = 1
    c[2][0] = 1
    c[2][1] = 1
    c[2][2] = 1
    return c

def r():
    c = Cells()
    for x, y in [(25, 25), (26, 25), (24, 26), (25, 26), (25, 27)]:
        c[x][y] = 1
    return c

def animate(c, n):
    while True:
        dump(c, n)
        print
        c = cells_next(c)
        if raw_input() != '':
            return c


if __name__ == '__main__':
    animate(r(), 50)
