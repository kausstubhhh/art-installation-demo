
from src.solver import reconstruct_final_state, build_completed_demo
from src.models import Light

def test_reconstruct_final_state():
    state = reconstruct_final_state("sample_input.csv")
    assert state.is_on(Light(1, 2.75)) is True
    assert state.is_on(Light(2, 0.75)) is False
    assert state.is_on(Light(3, 2.75)) is False
    assert state.is_on(Light(2, 1.75)) is True

def test_build_completed_demo(tmp_path):
    out = tmp_path / "completed.csv"
    build_completed_demo(out)
    text = out.read_text()
    assert "2026-01-01T00:00:06Z,2,1.25,on" in text
    assert "2026-01-01T00:00:06Z,3,2.25,off" in text
    assert "2026-01-01T00:00:06Z,3,1.25,off" in text
