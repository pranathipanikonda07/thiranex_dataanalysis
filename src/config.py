"""
Configuration and constants for EDA project
"""

# Data Paths
DATA_DIR = '../data'
RESULTS_DIR = '../results'
NOTEBOOKS_DIR = '../notebooks'

# Analysis Parameters
OUTLIER_IQR_MULTIPLIER = 1.5
OUTLIER_ZSCORE_THRESHOLD = 3
CORRELATION_THRESHOLD = 0.7

# Visualization Parameters
VISUALIZATION_DPI = 300
FIGURE_SIZE_DEFAULT = (14, 6)
FIGURE_SIZE_LARGE = (16, 10)
FIGURE_SIZE_HEATMAP = (10, 8)

# Plotting Styles
PLOT_STYLE = "whitegrid"
COLOR_PALETTE = "Set2"

# Data Quality Thresholds
MISSING_VALUE_THRESHOLD = 0.5  # 50% of data must be present
DUPLICATE_THRESHOLD = 0.1      # Allow max 10% duplicates

# Statistical Parameters
CONFIDENCE_LEVEL = 0.95
SIGNIFICANCE_LEVEL = 0.05

# Report Configuration
REPORT_FORMAT_MARKDOWN = 'markdown'
REPORT_FORMAT_TEXT = 'text'
REPORT_TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

# Column Type Classification
NUMERIC_TYPES = ['int64', 'float64', 'int32', 'float32']
CATEGORICAL_TYPES = ['object', 'category']

# Features for Different Analyses
DEFAULT_NUMERIC_COLS = ['age', 'purchase_amount', 'quantity', 'customer_tenure_days', 'satisfaction_score']
DEFAULT_CATEGORICAL_COLS = ['gender', 'product_category', 'payment_method', 'location']
