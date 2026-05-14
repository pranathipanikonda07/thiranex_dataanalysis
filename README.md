# Exploratory Data Analysis (EDA) Project

A comprehensive data analysis project demonstrating exploratory data analysis techniques to uncover patterns, trends, and key insights from sales transaction data.

## 📋 Project Overview

This project provides a complete framework for performing exploratory data analysis, including:

- **Statistical Analysis**: Descriptive statistics, distributions, and correlation analysis
- **Data Visualization**: Multiple visualization techniques to uncover patterns
- **Outlier Detection**: Identifying and analyzing anomalies in the data
- **Structured Reporting**: Automated report generation in multiple formats
- **Reusable Utilities**: Custom Python modules for EDA workflows

## 🗂️ Project Structure

```
thiranex_dataanalysis/
├── data/                           # Raw and processed data
│   └── sales_data.csv             # Sample dataset (40 customer transactions)
├── notebooks/
│   └── 01_EDA_Analysis.ipynb      # Main EDA analysis notebook
├── src/
│   ├── eda_utils.py               # Utility classes for data exploration
│   └── report_generator.py        # Report generation utilities
├── results/                        # Output visualizations and reports
│   ├── *.png                       # Generated visualizations
│   ├── EDA_Report.md               # Markdown format report
│   └── EDA_Report.txt              # Text format report
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   cd thiranex_dataanalysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Analysis

1. **Launch Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open the main notebook**
   - Navigate to `notebooks/01_EDA_Analysis.ipynb`

3. **Run the analysis**
   - Execute cells sequentially from top to bottom
   - Or use `Kernel → Run All` to execute the entire notebook

## 📊 Key Analysis Sections

### 1. **Data Loading & Inspection**
   - Load dataset and inspect structure
   - Examine data types and basic information
   - Display sample records

### 2. **Data Quality Assessment**
   - Check for missing values
   - Identify duplicate records
   - Validate data integrity

### 3. **Descriptive Statistics**
   - Summary statistics (mean, median, std, etc.)
   - Quartile analysis
   - Distribution metrics (skewness, kurtosis)

### 4. **Univariate Analysis**
   - Histogram distributions
   - Box plots for outlier identification
   - Distribution shapes and patterns

### 5. **Bivariate Analysis**
   - Scatter plots for relationships
   - Cross-tabulations
   - Categorical comparisons

### 6. **Correlation Analysis**
   - Correlation matrix calculation
   - Heatmap visualization
   - Identification of key influencing factors

### 7. **Distribution by Groups**
   - Violin plots by category
   - Segmented analysis
   - Age group profiling

### 8. **Outlier Detection**
   - IQR-based outlier detection
   - Z-score analysis
   - Visual outlier identification

### 9. **Key Insights Report**
   - Comprehensive findings summary
   - Business implications
   - Recommendations

## 📈 Generated Outputs

The analysis produces:

- **8 Visualization PNG files**:
  - `01_distributions.png` - Histogram distributions of all numeric variables
  - `02_boxplots.png` - Box plots for outlier identification
  - `03_scatter_plots.png` - Relationship scatter plots
  - `04_bar_charts.png` - Category and payment method analysis
  - `05_correlation_heatmap.png` - Correlation matrix visualization
  - `06_violin_plots.png` - Distribution by category/gender
  - `07_age_analysis.png` - Age group profiling
  - `08_outlier_analysis.png` - Outlier highlighting

- **2 Report Files**:
  - `EDA_Report.md` - Markdown formatted comprehensive report
  - `EDA_Report.txt` - Plain text formatted report

## 🔧 Key Modules

### `eda_utils.py`

Contains the `DataExplorer` class with methods:

- `get_basic_stats()` - Dataset overview metrics
- `get_numerical_summary()` - Descriptive statistics
- `get_categorical_summary()` - Category analysis
- `get_correlation_matrix()` - Correlation calculations
- `detect_outliers()` - Outlier identification (IQR/Z-score)
- `missing_data_analysis()` - Missing value assessment
- `create_distribution_plot()` - Distribution visualizations
- `create_correlation_heatmap()` - Heatmap generation
- `create_boxplot()` - Box plot creation

### `report_generator.py`

Contains the `ReportGenerator` class with methods:

- `generate_text_report()` - Generate text format reports
- `generate_markdown_report()` - Generate markdown format reports

## 📊 Sample Dataset

The project includes a sample sales dataset (`sales_data.csv`) with 40 customer transactions containing:

- **Customer Demographics**: age, gender, location
- **Transaction Details**: product_category, purchase_amount, quantity, payment_method
- **Temporal Data**: purchase_date, customer_tenure_days
- **Satisfaction**: satisfaction_score (1-10)

## 🎓 Learning Outcomes

By working through this project, you'll develop skills in:

- Data exploration and discovery techniques
- Statistical analysis and interpretation
- Data visualization best practices
- Pattern and trend identification
- Outlier detection and treatment
- Report generation and communication
- Python data analysis workflow
- Jupyter notebook usage

## 💡 Use Cases

This framework can be adapted for:

- Customer behavior analysis
- Sales performance review
- Market research analysis
- Product performance evaluation
- Quality assurance testing
- Fraud detection exploration
- Any exploratory data analysis task

## 🔍 Analysis Insights Examples

The analysis reveals insights such as:

- Revenue distribution across product categories
- Customer satisfaction patterns
- Age group purchasing behavior
- Payment method preferences
- Customer loyalty indicators
- High-value customer identification
- Seasonal trends and patterns

## 📝 Notes

- All visualizations are saved at 300 DPI for publication quality
- Reports automatically include data quality metrics
- The analysis is reproducible and can be run on new datasets
- Time needed: ~5-10 minutes for full notebook execution

## 🤝 Contributing

Feel free to extend this project with:

- Additional analysis techniques
- Advanced visualizations
- Statistical hypothesis testing
- Machine learning integration
- Interactive dashboards

## 📄 License

This project is provided as-is for educational purposes.

---

**Last Updated**: May 2026