import json
from typing import List
import random
import time
import copy

from RubicksCube.Side import Side
from RubicksCube.Cube import Cube
from RubicksCube.States import CubeSides, Moves
from Solvers.BFS import BFS
from Solvers.Greedy import Greedy


def make_moves_from_list(cube: Cube, list_of_moves: List[int]):
    for move in list_of_moves:
        cube.make_move(move)


def cube_to_json_file(cube: Cube, filepath: str):
    d = {}
    for index, side in enumerate(cube.current_state):
        d[str(CubeSides(index).name)] = side.current_state
    with open(filepath, "w") as outfile:
        json.dump(d, outfile)
    return


def random_moves_generator() -> List[int]:
    random.seed()
    l = random.randint(0, 3)
    moves = []
    for i in range(l):
        moves.append(random.randint(1, 9))
    return moves


def random_cube(filepath: str):
    with open("./Input/1.json") as file:
        states = json.load(file)

    cube = Cube([Side(states["U"]), Side(states["L"]), Side(states["F"]),
                  Side(states["R"]), Side(states["B"]), Side(states["D"])])
    moves = random_moves_generator()
    make_moves_from_list(cube,moves)
    cube_to_json_file(cube,filepath)


def test_bfs(cube: Cube):
    bfs = BFS(cube)
    start = time.time()
    bfs.run_algorithm()
    print(f"BFS time: {time.time() - start}")
    return list(map(lambda x: Moves(x).name, bfs.solution))[1:]


def test_greedy(cube: Cube):
    greedy = Greedy(cube)
    start = time.time()
    greedy.run_algorithm()
    print(f"Greedy time: {time.time() - start}")
    return list(map(lambda x: Moves(x).name, greedy.solution))[1:]


def run_both_solvers(filepath: str):
    with open(filepath) as file:
        states = json.load(file)

    cube1 = Cube([Side(states["U"]), Side(states["L"]), Side(states["F"]),
                  Side(states["R"]), Side(states["B"]), Side(states["D"])])
    cube2 = copy.deepcopy(cube1)
    print(cube1)
    print(test_greedy(cube1))
    print(test_bfs(cube2))


if __name__ == "__main__":
    filepath = "./Input/2.json"
    run_both_solvers(filepath)
    #random_cube(filepath)
