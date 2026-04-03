
import csv
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from .models import Instruction, Light

def parse_csv(path: str | Path) -> list[Instruction]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                Instruction(
                    timestamp=row["timestamp"].strip(),
                    light=Light(int(row["track_number"]), float(row["height_above_ground_meters"])),
                    state=row["state"].strip().lower(),
                )
            )
    return rows

def group_by_timestamp(instructions: list[Instruction]) -> Dict[str, List[Instruction]]:
    grouped: Dict[str, List[Instruction]] = defaultdict(list)
    for ins in instructions:
        grouped[ins.timestamp].append(ins)
    return dict(grouped)
