from functools import reduce
from math import atan2

POINTS = [[1, 1], [0, 1], [0, 0], [1, 0]]

x0, y0 = reduce(
    lambda x, p: (
        i := p[0],
        y := p[1],
        x[0] + (y[0] - x[0]) / i,
        x[1] + (y[1] - x[1]) / i,
    )[-2:],
    enumerate(POINTS, start=1),
    (0, 0),
)

print(sorted(POINTS, key=lambda x: atan2(x[1] - y0, x[0] - x0)))
