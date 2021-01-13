from enum import Enum


class CubeSides(Enum):
    U = 0
    L = 1
    F = 2
    R = 3
    B = 4
    D = 5


class Moves(Enum):
    start = 0
    u = 1
    r = 2
    f = 3
    d = 4
    l = 5
    b = 6
    m = 7
    e = 8
    s = 9
    ui = 10
    ri = 11
    fi = 12
    di = 13
    li = 14
    bi = 15
    u2 = 16
    r2 = 17
    f2 = 18
    d2 = 19
    l2 = 20
    b2 = 21
