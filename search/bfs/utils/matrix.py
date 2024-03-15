from search.bfs.utils.position import Position


class Matrix:
    matrix = []
    visited = []

    @classmethod
    def build(cls, rows, columns, barriers):
        m = Matrix(rows, columns, barriers)
        m._build()
        return m

    def __init__(self, rows, columns, barriers):
        self.rows = rows
        self.columns = columns
        self.barriers = barriers

    def within_bounds(self, node):
        position = node.position
        return 0 <= position.x < self.columns and 0 <= position.y < self.rows

    def is_barrier(self, position):
        return (position.x, position.y) in self.barriers

    def mark_position_visited(self, position: Position):
        self.visited[position.x][position.y] = 1

    def position_was_visited(self, position: Position):
        return self.visited[position.x][position.y] == 1

    def print(self):
        for row in self.matrix:
            print(row)

    def _build(self):
        for i in range(0, self.rows):
            self.matrix.append([0 for j in range(0, self.columns)])
            self.visited.append([0 for j in range(0, self.columns)])
