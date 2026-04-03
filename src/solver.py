
from pathlib import Path
from .generator import emit_demo, frame_from_grid
from .models import InstallationState
from .parser import parse_csv, group_by_timestamp

KNOWN_FRAMES = [
    ("2026-01-01T00:00:00Z", frame_from_grid(["101","101","101","101","010"])),
    ("2026-01-01T00:00:01Z", frame_from_grid(["111","101","101","101","111"])),
    ("2026-01-01T00:00:02Z", frame_from_grid(["100","100","100","100","111"])),
    ("2026-01-01T00:00:03Z", frame_from_grid(["111","100","100","100","111"])),
    ("2026-01-01T00:00:04Z", frame_from_grid(["111","101","101","101","111"])),
    ("2026-01-01T00:00:05Z", frame_from_grid(["110","101","110","101","101"])),
]

def reconstruct_final_state(csv_path: str | Path) -> InstallationState:
    state = InstallationState()
    for ins in parse_csv(csv_path):
        state.apply(ins)
    return state

def infer_next_second_frame() -> dict:
    return frame_from_grid([
        "110",
        "100",
        "110",
        "110",
        "101",
    ])

def build_completed_demo(output_csv: str | Path) -> None:
    frames = KNOWN_FRAMES + [("2026-01-01T00:00:06Z", infer_next_second_frame())]
    emit_demo(frames, output_csv)
