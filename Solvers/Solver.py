import abc
from typing import List, Tuple
from RubicksCube.Cube import Cube


class Solver:
    init_cube: Cube
    solution: List[int]
    steps: List[Tuple[List[int], Cube]]

    def __init__(self, cube: Cube):
        self.init_cube = cube
        self.steps = [([0], cube)]

    @abc.abstractmethod
    def run_algorithm(self):
        return
