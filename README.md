# Data Analysis on CSV Files

## Internship Task 5 – Sales Data Analysis using Pandas

### Objective
Analyze a sales dataset stored in a CSV file using Python and Pandas, then present useful insights with charts.

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Project Structure

```text
data-analysis-on-csv/
├── sales_data.csv
├── sales_analysis.ipynb
├── sales_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Analysis Performed

The project demonstrates:

- Loading CSV data with `pandas.read_csv()`
- Inspecting rows, columns, data types, and missing values
- Converting dates with `pd.to_datetime()`
- Calculating total sales and total quantity
- Calculating average order value
- Grouping sales by category using `groupby()` and `sum()`
- Comparing sales across regions
- Ranking product performance
- Filtering high-value orders
- Analyzing monthly sales trends
- Creating bar charts and a line chart with Matplotlib

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/rayhan-ahmed-web/data-analysis-on-csv.git
cd data-analysis-on-csv
```

### 2. Create a virtual environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Python Analysis

```bash
python sales_analysis.py
```

The script prints the main findings and displays three charts.

## Run the Jupyter Notebook

```bash
jupyter notebook sales_analysis.ipynb
```

Run all cells from top to bottom to reproduce the analysis and visualizations.

## Dataset

The included `sales_data.csv` contains sample sales records with order ID, date, product, category, region, quantity, unit price, and total sales.

## Example Insights

The analysis identifies:

- The highest-revenue category
- The highest-performing region
- The best-performing product by revenue
- Monthly sales patterns
- High-value orders
- Overall revenue and quantity sold

## Key Pandas Concepts Demonstrated

- `DataFrame`
- `read_csv()`
- `head()`
- `shape`
- `info()`
- `isnull()`
- `groupby()`
- `sum()`
- `mean()`
- Boolean filtering
- Date/time grouping

## Internship Deliverable

This repository contains the CSV dataset, completed Jupyter Notebook, Python analysis script, charts/visualization code, dependencies, and documentation required for the sales-data analysis task.

## License

This project is intended for educational and internship submission purposes.
