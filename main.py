"""One-star review of something essential: gravity, rated honestly."""
from pathlib import Path

one_star_review = "Gravity works fine all day, then drops my phone screen-first the one time it matters."

Path("/output/entry.txt").parent.mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(one_star_review + "\n", encoding="utf-8")
