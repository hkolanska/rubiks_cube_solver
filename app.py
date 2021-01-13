import json
from typing import List

from RubicksCube.Side import Side
from RubicksCube.Cube import Cube
from RubicksCube.States import CubeSides
from  Solvers.BFS import BFS


def make_moves_from_list(cube: Cube, list_of_moves: List[int]):
    for move in list_of_moves:
        cube.make_move(move)

def cube_to_json(cube: Cube, filepath: str):
    d = {}
    for index, side in enumerate(cube.current_state):
        d[str(CubeSides(index).name)] = side.current_state
    with open(filepath, "w") as outfile:
        json.dump(d,outfile)

    return


if __name__=="__main__":

    with open("./Input/3.json") as file:
        states = json.load(file)

    cube = Cube([Side(states["U"]),Side(states["L"]),Side(states["F"]),
                Side(states["R"]),Side(states["B"]),Side(states["D"])])
    bfs = BFS(cube)
    bfs.run_algorithm()
    print(bfs.solution)
    make_moves_from_list(cube, bfs.solution)
