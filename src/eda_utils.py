"""
Utility functions for Exploratory Data Analysis
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import StandardScaler


class DataExplorer:
    """Class for comprehensive data exploration"""
    
    def __init__(self, df):
        """Initialize with a DataFrame"""
        self.df = df
        self.numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    def get_basic_stats(self):
        """Get basic statistical summary"""
        stats_dict = {
            'shape': self.df.shape,
            'memory_usage': self.df.memory_usage(deep=True).sum() / 1024**2,
            'null_count': self.df.isnull().sum().sum(),
            'null_percentage': (self.df.isnull().sum().sum() / (self.df.shape[0] * self.df.shape[1])) * 100,
            'duplicate_rows': self.df.duplicated().sum()
        }
        return stats_dict
    
    def get_numerical_summary(self):
        """Get detailed numerical summary"""
        return self.df[self.numeric_cols].describe().T
    
    def get_categorical_summary(self):
        """Get categorical variable summary"""
        summary = {}
        for col in self.categorical_cols:
            summary[col] = {
                'unique_values': self.df[col].nunique(),
                'mode': self.df[col].mode()[0] if not self.df[col].mode().empty else None,
                'value_counts': self.df[col].value_counts().to_dict()
            }
        return summary
    
    def get_correlation_matrix(self):
        """Get correlation matrix for numeric columns"""
        return self.df[self.numeric_cols].corr()
    
    def get_high_correlations(self, threshold=0.7):
        """Get high correlations between numeric columns"""
        corr_matrix = self.get_correlation_matrix()
        high_corr = {}
        
        for i in range(len(corr_matrix.columns)):
            for j in range(i+1, len(corr_matrix.columns)):
                if abs(corr_matrix.iloc[i, j]) > threshold:
                    col1, col2 = corr_matrix.columns[i], corr_matrix.columns[j]
                    high_corr[f"{col1} - {col2}"] = corr_matrix.iloc[i, j]
        
        return high_corr
    
    def detect_outliers(self, columns=None, method='iqr'):
        """Detect outliers using IQR or Z-score method"""
        if columns is None:
            columns = self.numeric_cols
        
        outliers = {}
        
        if method == 'iqr':
            for col in columns:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                outlier_indices = self.df[(self.df[col] < Q1 - 1.5*IQR) | 
                                         (self.df[col] > Q3 + 1.5*IQR)].index.tolist()
                outliers[col] = {
                    'count': len(outlier_indices),
                    'percentage': (len(outlier_indices) / len(self.df)) * 100,
                    'indices': outlier_indices
                }
        
        elif method == 'zscore':
            for col in columns:
                z_scores = np.abs(stats.zscore(self.df[col].dropna()))
                outlier_indices = self.df[np.abs(stats.zscore(self.df[col])) > 3].index.tolist()
                outliers[col] = {
                    'count': len(outlier_indices),
                    'percentage': (len(outlier_indices) / len(self.df)) * 100,
                    'indices': outlier_indices
                }
        
        return outliers
    
    def missing_data_analysis(self):
        """Analyze missing data patterns"""
        missing_data = pd.DataFrame({
            'Column': self.df.columns,
            'Missing_Count': self.df.isnull().sum().values,
            'Missing_Percentage': (self.df.isnull().sum() / len(self.df) * 100).values
        })
        return missing_data[missing_data['Missing_Count'] > 0].sort_values('Missing_Percentage', ascending=False)
    
    @staticmethod
    def create_distribution_plot(df, columns, figsize=(15, 5)):
        """Create distribution plots for numeric columns"""
        numeric_cols = [col for col in columns if pd.api.types.is_numeric_dtype(df[col])]
        n_cols = len(numeric_cols)
        
        fig, axes = plt.subplots(1, n_cols, figsize=figsize)
        if n_cols == 1:
            axes = [axes]
        
        for idx, col in enumerate(numeric_cols):
            axes[idx].hist(df[col].dropna(), bins=30, edgecolor='black', alpha=0.7)
            axes[idx].set_title(f'Distribution of {col}', fontsize=12, fontweight='bold')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Frequency')
            axes[idx].grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def create_correlation_heatmap(correlation_matrix, figsize=(10, 8)):
        """Create a correlation heatmap"""
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                    center=0, square=True, ax=ax, cbar_kws={'label': 'Correlation'})
        ax.set_title('Correlation Matrix Heatmap', fontsize=14, fontweight='bold')
        plt.tight_layout()
        return fig
    
    @staticmethod
    def create_boxplot(df, columns, figsize=(15, 5)):
        """Create boxplots for numeric columns"""
        numeric_cols = [col for col in columns if pd.api.types.is_numeric_dtype(df[col])]
        n_cols = len(numeric_cols)
        
        fig, axes = plt.subplots(1, n_cols, figsize=figsize)
        if n_cols == 1:
            axes = [axes]
        
        for idx, col in enumerate(numeric_cols):
            axes[idx].boxplot(df[col].dropna())
            axes[idx].set_title(f'Boxplot of {col}', fontsize=12, fontweight='bold')
            axes[idx].set_ylabel(col)
            axes[idx].grid(axis='y', alpha=0.3)
        
        plt.tight_layout()
        return fig
