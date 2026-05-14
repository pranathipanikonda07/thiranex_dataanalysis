"""
Report generator for EDA findings
"""

import pandas as pd
from datetime import datetime


class ReportGenerator:
    """Generate structured EDA reports"""
    
    def __init__(self, df, dataset_name="Dataset"):
        self.df = df
        self.dataset_name = dataset_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def generate_text_report(self, output_path=None):
        """Generate a text report of EDA findings"""
        
        report = []
        report.append("=" * 80)
        report.append("EXPLORATORY DATA ANALYSIS (EDA) REPORT")
        report.append("=" * 80)
        report.append(f"Dataset: {self.dataset_name}")
        report.append(f"Generated: {self.timestamp}")
        report.append("")
        
        # 1. Data Overview
        report.append("1. DATA OVERVIEW")
        report.append("-" * 80)
        report.append(f"Shape: {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        report.append(f"Memory Usage: {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        report.append("")
        
        # 2. Data Quality
        report.append("2. DATA QUALITY")
        report.append("-" * 80)
        missing_data = self.df.isnull().sum()
        if missing_data.sum() > 0:
            report.append("Missing Values:")
            for col, count in missing_data[missing_data > 0].items():
                pct = (count / len(self.df)) * 100
                report.append(f"  {col}: {count} ({pct:.2f}%)")
        else:
            report.append("No missing values found.")
        
        duplicates = self.df.duplicated().sum()
        report.append(f"Duplicate Rows: {duplicates}")
        report.append("")
        
        # 3. Numerical Features
        report.append("3. NUMERICAL FEATURES SUMMARY")
        report.append("-" * 80)
        numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
        report.append(self.df[numeric_cols].describe().to_string())
        report.append("")
        
        # 4. Categorical Features
        report.append("4. CATEGORICAL FEATURES SUMMARY")
        report.append("-" * 80)
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        for col in categorical_cols:
            report.append(f"\n{col}:")
            report.append(f"  Unique values: {self.df[col].nunique()}")
            report.append(f"  Value counts:")
            for val, count in self.df[col].value_counts().items():
                pct = (count / len(self.df)) * 100
                report.append(f"    {val}: {count} ({pct:.2f}%)")
        report.append("")
        
        # 5. Correlations
        if len(numeric_cols) > 1:
            report.append("5. CORRELATION ANALYSIS")
            report.append("-" * 80)
            corr_matrix = self.df[numeric_cols].corr()
            report.append(corr_matrix.to_string())
            report.append("")
        
        # Footer
        report.append("=" * 80)
        report.append("END OF REPORT")
        report.append("=" * 80)
        
        report_text = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_text)
        
        return report_text
    
    def generate_markdown_report(self, output_path=None):
        """Generate a markdown report of EDA findings"""
        
        report = []
        report.append("# Exploratory Data Analysis (EDA) Report")
        report.append("")
        report.append(f"**Dataset:** {self.dataset_name}  ")
        report.append(f"**Generated:** {self.timestamp}  ")
        report.append("")
        
        # 1. Data Overview
        report.append("## 1. Data Overview")
        report.append("")
        report.append(f"- **Shape:** {self.df.shape[0]} rows × {self.df.shape[1]} columns")
        report.append(f"- **Memory Usage:** {self.df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        report.append("")
        
        # 2. Data Quality
        report.append("## 2. Data Quality")
        report.append("")
        missing_data = self.df.isnull().sum()
        if missing_data.sum() > 0:
            report.append("### Missing Values")
            report.append("")
            for col, count in missing_data[missing_data > 0].items():
                pct = (count / len(self.df)) * 100
                report.append(f"- **{col}:** {count} ({pct:.2f}%)")
        else:
            report.append("✓ No missing values found")
        
        report.append("")
        duplicates = self.df.duplicated().sum()
        report.append(f"- **Duplicate Rows:** {duplicates}")
        report.append("")
        
        # 3. Numerical Features
        report.append("## 3. Numerical Features")
        report.append("")
        numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
        if numeric_cols:
            report.append("```")
            report.append(self.df[numeric_cols].describe().to_string())
            report.append("```")
        report.append("")
        
        # 4. Categorical Features
        report.append("## 4. Categorical Features")
        report.append("")
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        for col in categorical_cols:
            report.append(f"### {col}")
            report.append("")
            report.append(f"- **Unique values:** {self.df[col].nunique()}")
            report.append("- **Value distribution:**")
            for val, count in self.df[col].value_counts().items():
                pct = (count / len(self.df)) * 100
                report.append(f"  - {val}: {count} ({pct:.2f}%)")
            report.append("")
        
        # 5. Correlations
        if len(numeric_cols) > 1:
            report.append("## 5. Correlation Analysis")
            report.append("")
            report.append("| | " + " | ".join(numeric_cols) + " |")
            report.append("|" + "|".join(["---"] * (len(numeric_cols) + 1)) + "|")
            corr_matrix = self.df[numeric_cols].corr()
            for idx, row in corr_matrix.iterrows():
                report.append(f"| **{idx}** | " + " | ".join([f"{val:.3f}" for val in row]) + " |")
            report.append("")
        
        # Key Insights
        report.append("## 6. Key Insights & Recommendations")
        report.append("")
        report.append("- Review data quality metrics above")
        report.append("- Investigate high correlations for multicollinearity")
        report.append("- Consider outlier treatment for numerical features")
        report.append("- Analyze categorical variable distributions")
        report.append("")
        
        report_text = "\n".join(report)
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_text)
        
        return report_text
