"""
Standalone EDA Runner Script
Run exploratory data analysis on any CSV dataset
"""

import sys
import os
import pandas as pd
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from eda_utils import DataExplorer
from report_generator import ReportGenerator


def run_eda_analysis(csv_file_path, output_dir='results', dataset_name=None):
    """
    Run complete EDA analysis on a CSV file
    
    Parameters:
    -----------
    csv_file_path : str
        Path to the CSV file to analyze
    output_dir : str
        Directory to save results
    dataset_name : str
        Name of the dataset for reporting
    """
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Load data
    print(f"\n{'='*80}")
    print("EXPLORATORY DATA ANALYSIS - AUTOMATED RUNNER")
    print(f"{'='*80}\n")
    
    print(f"Loading data from: {csv_file_path}")
    try:
        df = pd.read_csv(csv_file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    
    # Set dataset name
    if dataset_name is None:
        dataset_name = os.path.basename(csv_file_path).replace('.csv', '')
    
    print(f"✓ Data loaded successfully")
    print(f"  Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    # Initialize explorer
    explorer = DataExplorer(df)
    
    # Run analysis
    print(f"\n{'='*80}")
    print("BASIC STATISTICS")
    print(f"{'='*80}\n")
    
    basic_stats = explorer.get_basic_stats()
    for key, value in basic_stats.items():
        if isinstance(value, float):
            print(f"{key:20}: {value:.2f}")
        else:
            print(f"{key:20}: {value}")
    
    print(f"\n{'='*80}")
    print("NUMERICAL SUMMARY")
    print(f"{'='*80}\n")
    
    numerical_summary = explorer.get_numerical_summary()
    print(numerical_summary)
    
    print(f"\n{'='*80}")
    print("CATEGORICAL SUMMARY")
    print(f"{'='*80}\n")
    
    categorical_summary = explorer.get_categorical_summary()
    for col, stats in categorical_summary.items():
        print(f"\n{col}:")
        print(f"  Unique Values: {stats['unique_values']}")
        print(f"  Mode: {stats['mode']}")
    
    print(f"\n{'='*80}")
    print("MISSING DATA ANALYSIS")
    print(f"{'='*80}\n")
    
    missing_analysis = explorer.missing_data_analysis()
    if len(missing_analysis) > 0:
        print(missing_analysis.to_string())
    else:
        print("✓ No missing values found")
    
    print(f"\n{'='*80}")
    print("OUTLIER DETECTION")
    print(f"{'='*80}\n")
    
    outliers = explorer.detect_outliers(method='iqr')
    for col, info in outliers.items():
        if info['count'] > 0:
            print(f"{col}: {info['count']} outliers ({info['percentage']:.2f}%)")
    
    print(f"\n{'='*80}")
    print("CORRELATION ANALYSIS")
    print(f"{'='*80}\n")
    
    corr_matrix = explorer.get_correlation_matrix()
    print(corr_matrix)
    
    high_corr = explorer.get_high_correlations(threshold=0.7)
    if high_corr:
        print(f"\nHigh Correlations (> 0.7):")
        for pair, corr in high_corr.items():
            print(f"  {pair}: {corr:.4f}")
    
    # Generate reports
    print(f"\n{'='*80}")
    print("GENERATING REPORTS")
    print(f"{'='*80}\n")
    
    report_gen = ReportGenerator(df, dataset_name=dataset_name)
    
    # Markdown report
    md_path = os.path.join(output_dir, f"{dataset_name}_EDA_Report.md")
    report_gen.generate_markdown_report(md_path)
    print(f"✓ Markdown report: {md_path}")
    
    # Text report
    txt_path = os.path.join(output_dir, f"{dataset_name}_EDA_Report.txt")
    report_gen.generate_text_report(txt_path)
    print(f"✓ Text report: {txt_path}")
    
    print(f"\n{'='*80}")
    print("ANALYSIS COMPLETE")
    print(f"{'='*80}")
    print(f"\nResults saved to: {output_dir}/")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Run exploratory data analysis on CSV files'
    )
    parser.add_argument(
        'csv_file',
        help='Path to CSV file to analyze'
    )
    parser.add_argument(
        '--output-dir',
        default='results',
        help='Output directory for results (default: results)'
    )
    parser.add_argument(
        '--name',
        default=None,
        help='Dataset name for reporting'
    )
    
    args = parser.parse_args()
    
    run_eda_analysis(
        csv_file_path=args.csv_file,
        output_dir=args.output_dir,
        dataset_name=args.name
    )


if __name__ == '__main__':
    main()
