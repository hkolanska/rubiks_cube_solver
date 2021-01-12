import json

from RubicksCube.Side import Side
from RubicksCube.Cube import Cube

s = Cube([
    Side([[1, 1, 1], [1, 1, 1], [1, 1, 1]]),
    Side([[2, 2, 2], [2, 2, 2], [2, 2, 2]]),
    Side([[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
    Side([[4, 4, 4], [4, 4, 4], [4, 4, 4]]),
    Side([[5, 5, 5], [5, 5, 5], [5, 5, 5]]),
    Side([[6, 6, 6], [6, 6, 6], [6, 6, 6]])
])
with open("./Input/2.json") as file:
    states = json.load(file)

cube = Cube([Side(states["U"]),Side(states["L"]),Side(states["F"]),
            Side(states["R"]),Side(states["B"]),Side(states["D"])])
cube.move_u()
print(cube)
#
cube.move_r()
print(cube)
