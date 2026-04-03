
from pathlib import Path
from src.generator import frame_from_grid, emit_demo
from src.models import Light

def test_frame_from_grid():
    frame = frame_from_grid(["111","000","000","000","111"])
    assert frame[Light(1, 2.75)] is True
    assert frame[Light(2, 1.75)] is False
    assert frame[Light(3, 0.75)] is True

def test_emit_demo_only_changes(tmp_path: Path):
    out = tmp_path / "demo.csv"
    f1 = frame_from_grid(["100","000","000","000","000"])
    f2 = frame_from_grid(["100","000","000","000","000"])
    emit_demo([("t0", f1), ("t1", f2)], out)
    text = out.read_text()
    assert text.count("\n") == 2  # header + one row
