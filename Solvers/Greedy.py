from RubicksCube import Cube
from Solvers.Solver import Solver
from typing import List

import copy


class Greedy(Solver):

    def __init__(self, cube: Cube):
        super().__init__(cube)
        self.openlist = [([0], cube, self.fitness_function(cube))]
        self.closelist = []
        self.it_num = 0

    def existed_closelist(self, cube: Cube) -> int:
        for _, achieved_state, _ in self.closelist:
            if achieved_state == cube:
                return True
        return False

    def existed_openlist(self, cube: Cube) -> int:
        for _, achieved_state, _ in self.openlist:
            if achieved_state == cube:
                return True
        return False

    def fitness_function(self, cube: Cube) -> int:
        fitness = 0
        for index, side in enumerate(cube.current_state, start=1):
            for row in side.current_state:
                for col in row:
                    if index != col:
                        fitness += 1
        return fitness

    def cube_with_best_fitness(self, list: List):
        lowest = list[0]
        best_fitness = lowest[2]
        for step_data in list:
            if step_data[2] < best_fitness:
                lowest = step_data
                best_fitness = lowest[2]
        return lowest

    def run_algorithm(self):
        while self.openlist:
            current_obj = self.cube_with_best_fitness(self.openlist)
            current_cube = copy.deepcopy(current_obj[1])
            current_moves = copy.deepcopy(current_obj[0])
            if current_cube.solved():
                self.solution = current_moves
                return
            self.openlist.remove(current_obj)
            self.closelist.append(current_obj)

            for move in range(1, 28):
                cube = copy.deepcopy(current_cube)
                moves = copy.deepcopy(current_moves)
                cube.make_move(move)
                moves.append(move)
                if current_cube.solved():
                    self.solution = moves
                    return
                if not self.existed_closelist(cube) and \
                        not self.existed_openlist(cube) and len(moves) < 7:
                    self.openlist.append(
                        (moves, cube, self.fitness_function(cube)))
