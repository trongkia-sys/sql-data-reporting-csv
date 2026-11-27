# SQL Data Querying & Automated CSV Reporting

Generate a regional sales report from bundled sample data using SQLite and Python. The report counts completed orders and sums their revenue for each region.

## Quick start

Use Python 3.8 or later. The script uses only the standard library and creates an in-memory SQLite database.

Clone the repository and run these commands from a terminal. If you downloaded a ZIP from GitHub, extract it and open a terminal in the extracted folder, then run the last command.

```bash
git clone https://github.com/trongkia-sys/sql-data-reporting-csv.git
cd sql-data-reporting-csv
python export_report.py
```

On Windows, use `py -3` in place of `python` if needed. On macOS or Linux, use `python3` if your installation uses that command.

Open the generated `reports/sales_by_region.csv` in a spreadsheet app or text editor. To choose a different destination, use `--output`:

```bash
python export_report.py --output "reports/demo/regional_sales.csv"
```

Relative output paths start from the terminal's current directory. The script creates missing output directories and overwrites an existing file at the selected path.

## Repository layout

| Path | Purpose |
| --- | --- |
| [`export_report.py`](export_report.py) | Loads the SQL files, runs the query, and writes the CSV. |
| [`sql/sample_data.sql`](sql/sample_data.sql) | Creates the customer and order tables and inserts sample records. |
| [`sql/sales_by_region.sql`](sql/sales_by_region.sql) | Joins customers to orders and aggregates completed sales by region. |
| `reports/sales_by_region.csv` | Default output, generated when you run the script. |

The script locates `sql/` next to `export_report.py`, even when you start it from another directory. Keep both SQL files in that folder.

## Example output

```csv
region,completed_orders,revenue_cents
North,2,20000
South,1,9000
```

The CSV includes a header row and uses UTF-8 with a byte order mark (BOM). The query includes only regions with completed orders and sorts by revenue descending, then region name for ties. It reports revenue in integer cents to preserve exact totals.
