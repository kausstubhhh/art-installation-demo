
import csv
from pathlib import Path
from .models import HEIGHTS, InstallationState, Light

def frame_from_grid(grid: list[str]) -> dict[Light, bool]:
    if len(grid) != 5 or any(len(row) != 3 for row in grid):
        raise ValueError("Grid must be 5 rows x 3 cols")
    desired = {}
    heights_top_to_bottom = list(reversed(HEIGHTS))
    for r, height in enumerate(heights_top_to_bottom):
        for c, ch in enumerate(grid[r], start=1):
            desired[Light(c, height)] = (ch == "1")
    return desired

def emit_demo(frames: list[tuple[str, dict[Light, bool]]], out_path: str | Path) -> None:
    state = InstallationState()
    rows = []
    for timestamp, desired in frames:
        changes = state.set_frame(desired)
        for light, new_state in changes:
            rows.append([timestamp, light.track, f"{light.height:.2f}", new_state])
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "track_number", "height_above_ground_meters", "state"])
        writer.writerows(rows)
