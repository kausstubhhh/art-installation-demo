
from .models import HEIGHTS, Light, InstallationState
from .geometry import glowing_edges

def ascii_frame(state: InstallationState) -> str:
    lines = []
    for h in reversed(HEIGHTS):
        row = []
        for t in (1, 2, 3):
            row.append("●" if state.is_on(Light(t, h)) else ".")
        lines.append(f"{h:>4.2f}  " + "   ".join(row))
    return "\n".join(lines)

def edge_summary(state: InstallationState) -> str:
    edges = glowing_edges(state.on_lights())
    return "\n".join(
        f"({a.track},{a.height:.2f}) <-> ({b.track},{b.height:.2f})"
        for a, b in sorted(edges)
    )
