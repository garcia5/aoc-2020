TREE = '#'
class Toboggan():

    def __init__(self, _pos=(0,0)):
        self.x = _pos[0]
        self.y = _pos[1]

    def move(self, num=3, denom=1):
        self.x += num
        self.y += denom

    def coord(self):
        return (self.x, self.y)


class Grid():

    def __init__(self, _grid):
        self.data = _grid
        self.period = len(_grid[0])

    def is_tree(self, coord):
        x = coord[0] % self.period
        y = coord[1]
        return self.get_char(x, y) == TREE

    def get_char(self, x, y):
        return self.data[y][x]


if __name__ == '__main__':
    input_grid = open('input', 'r').read().splitlines()
    g = Grid(input_grid)
    print(f'grid height is {len(input_grid)}')

    tree_count = 1
    slopes = [
                {'num': 1, 'denom': 1},
                {'num': 3, 'denom': 1},
                {'num': 5, 'denom': 1},
                {'num': 7, 'denom': 1},
                {'num': 1, 'denom': 2},
            ]

    for s in slopes:
        t = Toboggan()
        iter_count = 0
        while t.y < len(input_grid):
            if g.is_tree(t.coord()):
                iter_count = iter_count + 1

            t.move(**s)

        print(f'iter_count: {iter_count}')
        tree_count = tree_count * iter_count


    print(f'tree count is: {tree_count}')
