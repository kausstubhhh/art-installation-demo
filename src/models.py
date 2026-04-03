
from dataclasses import dataclass
from typing import Dict

TRACK_X = {1: 0.0, 2: 0.5, 3: 1.0}
HEIGHTS = (0.75, 1.25, 1.75, 2.25, 2.75)

@dataclass(frozen=True, order=True)
class Light:
    track: int
    height: float

    @property
    def coord(self) -> tuple[float, float]:
        return (TRACK_X[self.track], self.height)

@dataclass(frozen=True)
class Instruction:
    timestamp: str
    light: Light
    state: str

class InstallationState:
    def __init__(self) -> None:
        self._states: Dict[Light, bool] = {
            Light(track, h): False
            for track in (1, 2, 3)
            for h in HEIGHTS
        }

    def is_on(self, light: Light) -> bool:
        return self._states[light]

    def apply(self, instruction: Instruction) -> None:
        current = self._states[instruction.light]
        target = instruction.state == "on"
        if current == target:
            raise ValueError(
                f"Redundant instruction for {instruction.light} at {instruction.timestamp}: {instruction.state}"
            )
        self._states[instruction.light] = target

    def set_frame(self, desired: Dict[Light, bool]) -> list[tuple[Light, str]]:
        changes = []
        for light, target in sorted(desired.items()):
            if self._states[light] != target:
                self._states[light] = target
                changes.append((light, "on" if target else "off"))
        return changes

    def on_lights(self) -> set[Light]:
        return {light for light, state in self._states.items() if state}

    def snapshot(self) -> Dict[Light, bool]:
        return dict(self._states)
