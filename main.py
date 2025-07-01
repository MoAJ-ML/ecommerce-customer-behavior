import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Set visualization directory
VIS_DIR = 'visualization'
os.makedirs(VIS_DIR, exist_ok=True)

def load_and_clean_data(filepath):
    """Load data, handle missing values, and ensure correct types."""
    df = pd.read_csv(filepath)
    # Handle missing values
    df = df.dropna(subset=['Customer ID'])
    # Fill or drop other missing values as appropriate
    # Convert columns to correct types
    df['Discount Applied'] = df['Discount Applied'].astype(bool)
    return df

def rfm_analysis(df):
    """Perform RFM segmentation and plot clusters."""
    rfm = df[['Customer ID', 'Days Since Last Purchase', 'Items Purchased', 'Total Spend']].copy()
    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])
    kmeans = KMeans(n_clusters=4, random_state=42)
    rfm['Segment'] = kmeans.fit_predict(rfm_scaled)
    # Plot
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='Recency', y='Monetary', hue='Segment', data=rfm, palette='Set2')
    plt.title('RFM Segments')
    plt.savefig(os.path.join(VIS_DIR, 'rfm_segments.png'), dpi=300, bbox_inches='tight')
    plt.close()
    return rfm

def cohort_analysis(df):
    """Approximate cohorts by Membership Type and plot retention."""
    cohort_pivot = pd.pivot_table(df, index='Membership Type', columns='Satisfaction Level', values='Customer ID', aggfunc='count', fill_value=0)
    cohort_pivot = cohort_pivot.div(cohort_pivot.sum(axis=1), axis=0)
    plt.figure(figsize=(10,6))
    sns.heatmap(cohort_pivot, annot=True, fmt='.2f', cmap='Blues')
    plt.title('Cohort Retention Curve (by Membership Type)')
    plt.savefig(os.path.join(VIS_DIR, 'cohort_retention_curve.png'), dpi=300, bbox_inches='tight')
    plt.close()

def spend_by_membership(df):
    """Plot distribution of Total Spend and Items Purchased by Membership Type."""
    plt.figure(figsize=(8,6))
    sns.boxplot(x='Membership Type', y='Total Spend', data=df)
    plt.title('Total Spend by Membership Type')
    plt.savefig(os.path.join(VIS_DIR, 'spend_by_membership.png'), dpi=300, bbox_inches='tight')
    plt.close()

def discount_vs_rating(df):
    """Show relationship between Discount Applied and Average Rating."""
    plt.figure(figsize=(8,6))
    sns.boxplot(x='Discount Applied', y='Average Rating', data=df)
    plt.title('Discount vs. Rating')
    plt.savefig(os.path.join(VIS_DIR, 'discount_vs_rating.png'), dpi=300, bbox_inches='tight')
    plt.close()

def correlation_heatmap(df):
    """Highlight correlations between numeric features."""
    corr = df[['Total Spend', 'Items Purchased', 'Average Rating', 'Days Since Last Purchase']].corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig(os.path.join(VIS_DIR, 'correlation_heatmap.png'), dpi=300, bbox_inches='tight')
    plt.close()

def main():
    data_path = os.path.join('data', 'E-commerce Customer Behavior - Sheet1.csv')
    df = load_and_clean_data(data_path)
    rfm = rfm_analysis(df)
    cohort_analysis(df)
    spend_by_membership(df)
    discount_vs_rating(df)
    correlation_heatmap(df)
    # After running, write summary manually or automate summary generation

if __name__ == '__main__':
    main()
