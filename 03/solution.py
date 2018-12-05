import re

#118 @ 65,516: 10x17

prog = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$')

class Rectangle:
    def __init__(self, string):
        match = prog.match(string)

        self._id = int(match.group(1))
        self._x = int(match.group(2))
        self._y = int(match.group(3))
        self._w = int(match.group(4))
        self._h = int(match.group(5))

    def get_overlapping_area(self, other_rectangle)


    def __str__(self):
        return '{} {},{} {}x{}'.format(self._id, self._x, self._y, self._w, self._h)

    def __repr__(self):
        return str(self)
        
with open('input.txt', 'r') as fil:
    rectangles = [Rectangle(x) for x in fil.readlines()]

