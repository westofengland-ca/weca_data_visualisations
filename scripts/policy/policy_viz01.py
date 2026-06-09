import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "policy" / "locations.csv"
HTML_PATH = ROOT / "docs" / "visuals" / "policy" / "viz01" / "index.html"

MARKER_START = "    // >>> GENERATED_LOCATIONS"
MARKER_END = "    // <<< GENERATED_LOCATIONS"
MARKER_PATTERN = re.compile(
    re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
    re.DOTALL,
)


def locations_block(df: pd.DataFrame) -> str:
    rows = ",\n".join(
        f"      {json.dumps(record)}"
        for record in df.to_dict(orient="records")
    )
    return (
        f"{MARKER_START}\n"
        f"    const LOCATIONS = [\n{rows}\n"
        f"    ];\n"
        f"{MARKER_END}"
    )


def main() -> None:
    df = pd.read_csv(CSV_PATH)
    html = HTML_PATH.read_text(encoding="utf-8")

    if not MARKER_PATTERN.search(html):
        raise ValueError(f"Location markers not found in {HTML_PATH}")

    updated = MARKER_PATTERN.sub(locations_block(df), html, count=1)
    HTML_PATH.write_text(updated, encoding="utf-8")
    print(f"Updated {len(df)} locations in {HTML_PATH}")


if __name__ == "__main__":
    main()
