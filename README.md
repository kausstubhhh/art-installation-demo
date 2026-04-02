
# Art Installation Demo Solver


## Core idea

The provided CSV is an **event log**, not a frame dump.

That means:
- lights retain their state until changed
- each row is a transition instruction
- redundant transitions are invalid

The software reconstructs the state over time and can emit **minimal CSV event logs** for arbitrary demo sequences.

---

## Geometry model

Each light is embedded in 2D:

- Track 1: x = 0.0
- Track 2: x = 0.5
- Track 3: x = 1.0

Heights:
- 0.75, 1.25, 1.75, 2.25, 2.75

Two ON lights glow-connect if their Euclidean distance is <= 0.75m.

This allows:
- vertical neighbors
- horizontal same-height neighbors
- immediate diagonals between adjacent tracks

If three lights form a complete glowing triangle, the **longest edge is removed**.

---

## Inference for the next second

The first six timestamps strongly resemble a deliberate geometric animation, not random toggling.

My chosen continuation for `00:00:06Z` is:

```csv
2026-01-01T00:00:06Z,2,1.25,on
2026-01-01T00:00:06Z,3,2.25,off
2026-01-01T00:00:06Z,3,1.25,off
```

Why:
- it continues the transition from right-side emphasis toward center-left structure
- it uses the minimum number of valid changes
- it respects the "no redundant instruction" rule
- it produces a visually coherent continuation

This is intentionally presented as a **reasoned artistic inference**, not a mathematically unique truth.

---

## Run

### Install
```
pip install -r requirements.txt
```

### Test
```
pytest -q
```

### Generate completed CSV
```
python -m src.main --output completed_output.csv
```

### Inspect final state of provided input
```
python -m src.main --input sample_input.csv --show
```

---

