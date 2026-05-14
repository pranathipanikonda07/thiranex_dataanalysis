# Quick Start Guide for EDA Project

## 5-Minute Setup

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### Step 2: Open Jupyter Notebook (30 sec)
```bash
jupyter notebook
```

### Step 3: Run the Analysis (3 min)
- Open `notebooks/01_EDA_Analysis.ipynb`
- Click `Kernel → Run All`
- Wait for completion

### Step 4: Review Results (30 sec)
- Check `results/` folder for visualizations
- Read `EDA_Report.md` for findings

## Using Custom Modules

### Import and Use DataExplorer

```python
from eda_utils import DataExplorer
import pandas as pd

# Load your data
df = pd.read_csv('your_data.csv')

# Initialize explorer
explorer = DataExplorer(df)

# Get various analyses
basic_stats = explorer.get_basic_stats()
numerical_stats = explorer.get_numerical_summary()
correlations = explorer.get_correlation_matrix()
outliers = explorer.detect_outliers(method='iqr')

# Create visualizations
explorer.create_distribution_plot(df, ['column1', 'column2'])
explorer.create_correlation_heatmap(explorer.get_correlation_matrix())
```

### Generate Reports

```python
from report_generator import ReportGenerator

# Create report generator
report_gen = ReportGenerator(df, dataset_name="My Dataset")

# Generate reports
report_gen.generate_markdown_report('output_report.md')
report_gen.generate_text_report('output_report.txt')
```

## Common Tasks

### Analyze Your Own Dataset

1. Place CSV file in `data/` folder
2. Modify cell 2 in notebook to load your file:
   ```python
   df = pd.read_csv('../data/your_file.csv')
   ```
3. Run the analysis

### Add New Visualizations

1. Add code after section 8 in the notebook
2. Use matplotlib/seaborn for creating plots
3. Save with: `plt.savefig('../results/your_plot.png', dpi=300, bbox_inches='tight')`

### Modify Report Template

Edit `src/report_generator.py` methods:
- `generate_text_report()` - for text output
- `generate_markdown_report()` - for markdown output

## Troubleshooting

**Missing libraries?**
```bash
pip install --upgrade -r requirements.txt
```

**Data not loading?**
- Check file path in notebook
- Verify CSV format is correct
- Ensure file is in `data/` directory

**Visualizations not showing?**
- Ensure matplotlib backend is active
- Try: `%matplotlib inline` in notebook

## Next Steps

- Customize analysis for your dataset
- Extend with advanced statistical tests
- Add interactive visualizations with Plotly
- Build predictive models using insights
- Create automated reporting pipeline

---

For detailed documentation, see README.md
