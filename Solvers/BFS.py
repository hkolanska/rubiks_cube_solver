from RubicksCube import Cube
from Solvers.Solver import Solver
import copy


class BFS(Solver):

    def __init__(self, cube: Cube):
        super().__init__(cube)

    def run_algorithm(self):
        i = 0
        while True:
            current_cube = copy.copy(self.steps[i][1])
            current_moves = copy.copy(self.steps[i][0])
            if current_cube.solved():
                self.solution = current_moves
                return
            for move in range(1,10):
                cube = copy.copy(current_cube)
                moves = copy.copy(current_moves)
                cube.make_move(move)
                moves.append(move)
                if cube.solved():
                    print(moves)
                    self.solution = moves
                    return
                else:
                    self.steps.append((moves, cube))
            i+=1





