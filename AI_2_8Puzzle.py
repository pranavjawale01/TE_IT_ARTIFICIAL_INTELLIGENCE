from collections import deque

class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([str(row) for row in self.board])

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def move_up(self):
        i, j = self.find_blank()
        if i == 0:
            return None
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        return PuzzleState(new_board, self, "Up")

    def move_down(self):
        i, j = self.find_blank()
        if i == 2:
            return None
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        return PuzzleState(new_board, self, "Down")

    def move_left(self):
        i, j = self.find_blank()
        if j == 0:
            return None
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        return PuzzleState(new_board, self, "Left")

    def move_right(self):
        i, j = self.find_blank()
        if j == 2:
            return None
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
        return PuzzleState(new_board, self, "Right")

    def expand(self):
        children = []
        up_child = self.move_up()
        if up_child:
            children.append(up_child)
        down_child = self.move_down()
        if down_child:
            children.append(down_child)
        left_child = self.move_left()
        if left_child:
            children.append(left_child)
        right_child = self.move_right()
        if right_child:
            children.append(right_child)
        return children

def breadth_first_search(initial_state, goal_state):
    visited = set()
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            path = []
            while current_state.parent:
                path.append(current_state.move)
                current_state = current_state.parent
            path.reverse()
            return path

        for child in current_state.expand():
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return None

if __name__ == "__main__":
    initial_state = PuzzleState([[2, 8, 3],
                                 [1, 6, 4],
                                 [7, 0, 5]])

    goal_state = PuzzleState([[1, 2, 3],
                              [8, 0, 4],
                              [7, 6, 5]])

    solution = breadth_first_search(initial_state, goal_state)
    if solution:
        print("Solution found!")
        print("Moves to reach the goal state:")
        print(solution)
    else:
        print("No solution found.")
