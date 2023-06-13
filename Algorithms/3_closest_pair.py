"""
Closest pair problem - The closest pair of points problem or closest pair problem
is a problem of computational geometry: given n points in metric space, find a pair
of points with the smallest distance between them.

https://github.com/karan/Projects
"""

import random

def closest_pair(points: list[tuple[int, int]]) -> tuple[int, tuple[int, int]]:
    minimum_distance = 200
    point = (-1, -1)
    for x, y in points:
        distance = abs(x - y)
        if distance < minimum_distance:
            minimum_distance = distance
            point = (x, y)
    return minimum_distance, point

points = [ (random.randint(0, 50), random.randint(50, 100)) for _ in range(100) ]

print(closest_pair(points))