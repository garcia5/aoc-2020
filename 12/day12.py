class Ship:

    direction = "E"
    x = 0
    y = 0
    dx = 10
    dy = 1

    def move(self, direction):
        d = direction[0]
        value = int(direction[1:])
        if d in ["N", "S", "E", "W"]:
            self._move_waypoint(d, value)

        else:
            self._move_relative(d, value)

    def _move_waypoint(self, d, value):
        print(f"moving {d} by {value}")
        if d == "N":
            self.dy += value

        if d == "S":
            self.dy -= value

        if d == "E":
            self.dx += value

        if d == "W":
            self.dx -= value

    def _move_relative(self, d, value):

        if value == 180 and d != "F":
            self.dx *= -1
            self.dy *= -1

        if (value == 270 and d == "L") or (value == 90 and d == "R"):
            (self.dy, self.dx) = (self.dx, self.dy)
            self.dy *= -1

        if (value == 270 and d == "R") or (value == 90 and d == "L"):
            (self.dy, self.dx) = (self.dx, self.dy)
            self.dx *= -1

        if d != "F":
            print(f"new waypoint is {self.dx}, {self.dy}")

        if d == "F":
            self.x += value * self.dx
            self.y += value * self.dy


if __name__ == "__main__":

    directions = [line.strip() for line in open("input", "r")]

    ship = Ship()

    for d in directions:
        # breakpoint()
        print(d)
        ship.move(d)
        print(f"new position is ({ship.x}, {ship.y})")
        print()

    print(ship.x, ship.y)
    print(abs(ship.x) + abs(ship.y))
