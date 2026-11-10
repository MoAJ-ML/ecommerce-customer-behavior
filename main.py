import os
import zipfile
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
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
    elif os.path.exists('archive (2).zip'):
        with zipfile.ZipFile('archive (2).zip') as archive:
            with archive.open(os.path.basename(filepath)) as source:
                df = pd.read_csv(source)
    else:
        raise FileNotFoundError(f"Provide {filepath} or archive (2).zip")
    # Handle missing values
    df = df.dropna(subset=['Customer ID'])
    # Fill or drop other missing values as appropriate
    # Convert columns to correct types
    df['Discount Applied'] = df['Discount Applied'].astype(str).str.lower().eq('true')
    return df

def segment_customers(df):
    """Segment customers using recency, item count, and spend proxies."""
    rfm = df[['Customer ID', 'Days Since Last Purchase', 'Items Purchased', 'Total Spend']].copy()
    rfm.columns = ['CustomerID', 'Recency', 'ItemsPurchased', 'Monetary']
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[['Recency', 'ItemsPurchased', 'Monetary']])
    kmeans = KMeans(n_clusters=min(4, len(rfm)), random_state=42, n_init=10)
    rfm['Segment'] = kmeans.fit_predict(rfm_scaled)
    # Plot
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='Recency', y='Monetary', hue='Segment', data=rfm, palette='Set2')
    plt.title('Customer Groups: Recency, Item Count, and Spend')
    plt.savefig(os.path.join(VIS_DIR, 'customer_segments.png'), dpi=300, bbox_inches='tight')
    plt.close()
    return rfm

def membership_satisfaction_analysis(df):
    """Plot the satisfaction mix within each membership type."""
    satisfaction_pivot = pd.pivot_table(df, index='Membership Type', columns='Satisfaction Level', values='Customer ID', aggfunc='count', fill_value=0)
    satisfaction_pivot = satisfaction_pivot.div(satisfaction_pivot.sum(axis=1), axis=0)
    plt.figure(figsize=(10,6))
    sns.heatmap(satisfaction_pivot, annot=True, fmt='.2f', cmap='Blues')
    plt.title('Satisfaction Distribution by Membership Type')
    plt.savefig(os.path.join(VIS_DIR, 'membership_satisfaction.png'), dpi=300, bbox_inches='tight')
    plt.close()
    return satisfaction_pivot

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
    segment_customers(df)
    membership_satisfaction_analysis(df)
    spend_by_membership(df)
    discount_vs_rating(df)
    correlation_heatmap(df)
    # After running, write summary manually or automate summary generation

if __name__ == '__main__':
    main()
