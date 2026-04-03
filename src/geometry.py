
import math
from itertools import combinations
from .models import Light

def distance(a: Light, b: Light) -> float:
    return math.dist(a.coord, b.coord)

def glowing_edges(on_lights: set[Light], threshold: float = 0.75) -> set[tuple[Light, Light]]:
    edges = set()
    for a, b in combinations(sorted(on_lights), 2):
        if distance(a, b) <= threshold + 1e-9:
            edges.add((a, b))

    edge_set = set(edges)
    for a, b, c in combinations(sorted(on_lights), 3):
        tri = {(min(x, y), max(x, y)) for x, y in [(a, b), (a, c), (b, c)]}
        if tri.issubset(edge_set):
            lengths = sorted(
                [((a, b), distance(a, b)), ((a, c), distance(a, c)), ((b, c), distance(b, c))],
                key=lambda x: x[1],
                reverse=True,
            )
            edge_set.discard(tuple(sorted(lengths[0][0])))
    return edge_set
