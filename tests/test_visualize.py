
from src.models import InstallationState, Instruction, Light
from src.visualize import ascii_frame

def test_ascii_frame():
    s = InstallationState()
    s.apply(Instruction("t", Light(1, 2.75), "on"))
    out = ascii_frame(s)
    assert "2.75" in out
    assert "●" in out
