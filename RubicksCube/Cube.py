from typing import List
from RubicksCube.Side import Side
from RubicksCube.States import Moves, CubeSides


class Cube:
    init_state: List[Side]
    current_state: List[Side]


    def __init__(self, init_state):
        self.init_state = init_state
        self.current_state = init_state

    def create_str_middle_sides(self):
        l = [i.almost_str() for i in self.current_state[1:-1]]
        b = [[x[i] for x in l] for i in range(5)]
        return "\n".join(["".join(x) for x in b])

    def move_u(self):
        self.current_state[CubeSides.U.value].clockwise_twist()
        tmp = self.current_state[CubeSides.F.value].u_row([7,7,7])
        tmp = self.current_state[CubeSides.L.value].u_row(tmp)
        tmp = self.current_state[CubeSides.B.value].u_row(tmp)
        tmp = self.current_state[CubeSides.R.value].u_row(tmp)
        self.current_state[CubeSides.F.value].u_row(tmp)

    def move_r(self):
        self.current_state[CubeSides.R.value].clockwise_twist()
        tmp = self.current_state[CubeSides.F.value].r_col([7, 7, 7])
        tmp = self.current_state[CubeSides.U.value].r_col(tmp)
        tmp = self.current_state[CubeSides.B.value].l_col(tmp[::-1])
        tmp = self.current_state[CubeSides.D.value].r_col(tmp[::-1])
        self.current_state[CubeSides.F.value].r_col(tmp)

    def move_f(self):
        self.current_state[CubeSides.F.value].clockwise_twist()
        tmp = self.current_state[CubeSides.L.value].r_col([7, 7, 7])
        tmp = self.current_state[CubeSides.U.value].d_row(tmp[::-1])
        tmp = self.current_state[CubeSides.R.value].l_col(tmp)
        tmp = self.current_state[CubeSides.D.value].u_row(tmp[::-1])
        self.current_state[CubeSides.L.value].r_col(tmp)

    def move_d(self):
        self.current_state[CubeSides.D.value].clockwise_twist()
        tmp = self.current_state[CubeSides.F.value].d_row([7,7,7])
        tmp = self.current_state[CubeSides.R.value].d_row(tmp)
        tmp = self.current_state[CubeSides.B.value].d_row(tmp)
        tmp = self.current_state[CubeSides.L.value].d_row(tmp)
        self.current_state[CubeSides.F.value].d_row(tmp)

    def __str__(self):
        whitespaces = " " * 9
        rubiks_cube_str = ""
        self.current_state[0].almost_str()
        rubiks_cube_str += "\n".join(whitespaces+i for i in
                                    self.current_state[0].almost_str()) + "\n"
        rubiks_cube_str+=self.create_str_middle_sides() +"\n"
        rubiks_cube_str += "\n".join(whitespaces+i for i in
                                    self.current_state[-1].almost_str())
        return rubiks_cube_str

