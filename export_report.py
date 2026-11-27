"""Generate a CSV sales report from the bundled sample data."""

import argparse
import csv
import sqlite3
from contextlib import closing
from pathlib import Path

SQL_DIR = Path(__file__).resolve().parent / "sql"


def export_report(output: Path) -> None:
    sample_data = (SQL_DIR / "sample_data.sql").read_text(encoding="utf-8")
    query = (SQL_DIR / "sales_by_region.sql").read_text(encoding="utf-8")

    with closing(sqlite3.connect(":memory:")) as database:
        database.execute("PRAGMA foreign_keys = ON")
        database.executescript(sample_data)
        results = database.execute(query)

        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(column[0] for column in results.description)
            writer.writerows(results)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("reports/sales_by_region.csv"),
        help="Path to the generated CSV file.",
    )
    args = parser.parse_args()
    export_report(args.output)
    print(f"Report saved to {args.output}")


if __name__ == "__main__":
    main()
