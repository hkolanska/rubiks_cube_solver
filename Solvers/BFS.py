from RubicksCube import Cube
from Solvers.Solver import Solver

from typing import List, Tuple
import copy


class BFS(Solver):

    def __init__(self, cube: Cube):
        super().__init__(cube)
        self.steps = [([0], cube)]

    def existed_state(self, cube):
        for _, achieved_state in self.steps:
            if achieved_state == cube:
                return True
        return False

    def run_algorithm(self):
        i = 0
        while True:
            current_cube = copy.deepcopy(self.steps[i][1])
            current_moves = copy.deepcopy(self.steps[i][0])
            if current_cube.solved():
                self.solution = current_moves
                return
            for move in range(1, 28):
                cube = copy.deepcopy(current_cube)
                moves = copy.deepcopy(current_moves)
                cube.make_move(move)
                moves.append(move)
                if cube.solved():
                    self.solution = moves
                    return
                elif not self.existed_state(cube):
                    self.steps.append((moves, cube))
            i += 1
