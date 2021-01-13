from typing import List


class Side:
    current_state: List[List[int]]

    def __init__(self, state):
        self.current_state = state

    def same(self):
        first = self.current_state[0][0]
        for row in self.current_state:
            for element in row:
                if first != element:
                    return False
        return True

    def clockwise_twist(self):
        new_u = [self.current_state[2][0], self.current_state[1][0],
                 self.current_state[0][0]]
        new_m = [self.current_state[2][1], self.current_state[1][1],
                 self.current_state[0][1]]
        new_d = [self.current_state[2][2], self.current_state[1][2],
                 self.current_state[0][2]]
        self.current_state = [new_u, new_m, new_d]
        return

    def anticlockwise_twist(self):
        new_u = [self.current_state[0][2], self.current_state[1][2],
                 self.current_state[2][2]]
        new_m = [self.current_state[0][1], self.current_state[1][1],
                 self.current_state[2][1]]
        new_d = [self.current_state[0][0], self.current_state[1][0],
                 self.current_state[2][0]]

        self.current_state = [new_u, new_m, new_d]
        return

    def u_row(self, new_tiles):
        removed_tiles = self.current_state[0]
        self.current_state[0] = new_tiles
        return removed_tiles

    def m_row(self, new_tiles):
        removed_tiles = self.current_state[1]
        self.current_state[1] = new_tiles
        return removed_tiles

    def d_row(self, new_tiles):
        removed_tiles = self.current_state[2]
        self.current_state[2] = new_tiles
        return removed_tiles

    def l_col(self, new_tiles):
        removed_tiles = [i[0] for i in self.current_state]
        for i, _ in enumerate(new_tiles):
            self.current_state[i][0] = new_tiles[i]
        return removed_tiles

    def m_col(self, new_tiles):
        removed_tiles = [i[1] for i in self.current_state]
        for i, _ in enumerate(new_tiles):
            self.current_state[i][1] = new_tiles[i]
        return removed_tiles

    def r_col(self, new_tiles):
        removed_tiles = [i[2] for i in self.current_state]
        for i, _ in enumerate(new_tiles):
            self.current_state[i][2] = new_tiles[i]
        return removed_tiles

    def almost_str(self):
        return [f"+-------+",
                f"+ {' '.join(str(v) for v in self.current_state[0])} +",
                f"+ {' '.join(str(v) for v in self.current_state[1])} +",
                f"+ {' '.join(str(v) for v in self.current_state[2])} +",
                f"+-------+"]
