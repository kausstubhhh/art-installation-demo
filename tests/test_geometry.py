
from src.geometry import distance, glowing_edges
from src.models import Light

def test_adjacent_diagonal_connects():
    a = Light(1, 1.25)
    b = Light(2, 1.75)
    assert round(distance(a, b), 3) == 0.707

def test_triangle_longest_edge_removed():
    a = Light(1, 1.25)
    b = Light(1, 1.75)
    c = Light(2, 1.25)
    edges = glowing_edges({a, b, c})
    assert (min(a,c), max(a,c)) in edges
    assert (min(a,b), max(a,b)) in edges
    assert (min(b,c), max(b,c)) not in edges
