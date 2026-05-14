# EDA Analysis Template for New Datasets

This directory contains a template for performing exploratory data analysis on any dataset.

## Steps to Analyze a New Dataset

### 1. Prepare Your Data
- Export or convert your data to CSV format
- Place the file in the `data/` directory
- Example: `data/my_dataset.csv`

### 2. Option A: Using Jupyter Notebook (Recommended)

```python
# In the notebook, modify the data loading cell:
df = pd.read_csv('../data/my_dataset.csv')

# Then run all cells to generate analysis
```

### 3. Option B: Using Command Line

```bash
# Run automated analysis
python run_eda.py data/my_dataset.csv --output-dir results --name "My Dataset"
```

### 4. Review Results

Generated files will be saved in `results/`:
- `my_dataset_EDA_Report.md` - Markdown format report
- `my_dataset_EDA_Report.txt` - Text format report
- Various PNG visualizations (if using notebook)

## Customization Tips

### For Time-Series Data
- Add time-based analysis in the notebook
- Use `pd.to_datetime()` for date columns
- Create time-based aggregations and trends

### For Large Datasets
- Consider sampling for faster analysis
- Use chunked processing for memory efficiency
- Adjust visualization size for readability

### For Categorical Heavy Data
- Increase number of categorical analysis sections
- Add more cross-tabulation analysis
- Use more category-based visualizations

### For Numerical Heavy Data
- Add correlation clustering
- Include PCA or dimensionality reduction
- Add more distribution analysis

## Example: Analyzing Different Data Types

### Example 1: Customer Data
```python
df = pd.read_csv('../data/customers.csv')
# Analysis will include: demographics, purchase patterns, lifetime value
```

### Example 2: Financial Data
```python
df = pd.read_csv('../data/transactions.csv')
# Analysis will include: trends, patterns, anomalies
```

### Example 3: Sensor Data
```python
df = pd.read_csv('../data/sensor_readings.csv')
# Analysis will include: distributions, time patterns, calibration check
```

## Modifying Analysis Parameters

Edit `src/config.py` to customize:
- Outlier detection thresholds
- Correlation thresholds
- Visualization sizes
- Report formatting

## Troubleshooting

| Issue | Solution |
|-------|----------|
| File not found | Ensure CSV is in `data/` directory |
| Memory error | Sample data: `df = df.sample(10000)` |
| Missing values issue | Use `df.fillna()` or `df.dropna()` |
| Encoding error | Specify encoding: `pd.read_csv('file.csv', encoding='utf-8')` |

## Next Steps After Analysis

1. **Share Findings**
   - Use generated markdown report
   - Include visualizations in presentations

2. **Deep Dive**
   - Investigate specific patterns
   - Run hypothesis tests
   - Create predictive models

3. **Automate**
   - Schedule regular analyses
   - Build dashboards
   - Create alerts for anomalies

---

For more information, see the main README.md
