# SQL Data Querying & Automated CSV Reporting

Generate a regional sales report by querying a sample SQLite database and exporting the results to CSV. The report counts completed orders and sums their revenue by region.

## How it works

1. Create an in-memory SQLite database with sample customers and orders.
2. Join orders to customers, filter for completed orders, and group the results by region.
3. Export the sorted query results to CSV with column headers and UTF-8 encoding with a BOM.

## Run the project

Requires Python 3.8 or later with its standard library.

```bash
git clone https://github.com/trongkia-sys/sql-data-reporting-csv.git
cd sql-data-reporting-csv
python export_report.py
```

The resulting file is `reports/sales_by_region.csv`. Use `--output path/to/report.csv` to choose another location. Running the command again overwrites the chosen output file.

## Example output

```csv
region,completed_orders,revenue_cents
North,2,20000
South,1,9000
```

Revenue is reported in cents to preserve exact integer totals. Cancelled orders are excluded.

## Source files

| File | Purpose |
| --- | --- |
| `sql/sample_data.sql` | Defines the schema and inserts sample records. |
| `sql/sales_by_region.sql` | Filters, aggregates, and sorts the report data. |
| `export_report.py` | Runs the SQL and writes the CSV using Python's `sqlite3` and `csv` modules. |
