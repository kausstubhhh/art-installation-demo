
from src.parser import parse_csv, group_by_timestamp

def test_parse_csv_reads_rows():
    rows = parse_csv("sample_input.csv")
    assert len(rows) == 26
    assert rows[0].timestamp == "2026-01-01T00:00:00Z"
    assert rows[0].light.track == 1

def test_group_by_timestamp():
    rows = parse_csv("sample_input.csv")
    grouped = group_by_timestamp(rows)
    assert "2026-01-01T00:00:05Z" in grouped
    assert len(grouped["2026-01-01T00:00:05Z"]) == 4
