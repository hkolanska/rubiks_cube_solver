import abc
from typing import List, Tuple
from RubicksCube.Cube import Cube


class Solver:
    init_cube: Cube
    solution: List[int]

    def __init__(self, cube: Cube):
        self.init_cube = cube

    @abc.abstractmethod
    def run_algorithm(self):
        return
