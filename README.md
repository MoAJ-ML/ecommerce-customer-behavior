# E-commerce Customer Behavior Analysis

## Overview
This project explores customer-level e-commerce data using recency, item count, spend, and satisfaction. The supplied dataset has no transaction dates or repeat purchase records, so it cannot support a time-based retention cohort or a true transaction-frequency RFM analysis.

## Features
- **Customer segmentation**: Groups customers by days since last purchase, items purchased, and total spend. Item count is a proxy, not transaction frequency.
- **Membership satisfaction**: Shows the satisfaction distribution within each membership type; it does not measure retention.
- **Visualizations**: Includes boxplots, heatmaps, and scatterplots to illustrate key findings.
- **Actionable Insights**: Provides data-driven recommendations for business strategy.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MoAJ-ML/ecommerce-customer-behavior.git
   cd ecommerce-customer-behavior
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. The script reads the tracked `archive (2).zip` directly. You can instead place `E-commerce Customer Behavior - Sheet1.csv` in `data/`.
2. Run the analysis:
   ```bash
   python main.py
   ```
3. View the generated visualizations in the `visualization/` directory.

## Project Structure
```
.
├── data/                    # Dataset directory
│   └── E-commerce Customer Behavior - Sheet1.csv  # optional extracted input
├── visualization/           # Generated visualizations
│   ├── rfm_segments.png
│   ├── membership_satisfaction.png
│   ├── spend_by_membership.png
│   ├── discount_vs_rating.png
│   ├── correlation_heatmap.png
│   └── summary_insights.md
├── main.py                  # Main analysis script
├── requirements.txt         # Dependencies
└── README.md                # This file
```

## Dependencies
- A Python version supported by the versions resolved from `requirements.txt`
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Contributing
Feel free to submit issues or pull requests for improvements.

## License
No software license file is currently included. Obtain permission from the data owner before redistributing or reusing the dataset.

## Reproducibility and limits

The tracked ZIP contains a single customer-level CSV with no timestamps. Run `python main.py` from the repository root after installing `requirements.txt`. The analysis produces descriptive plots and unsupervised clusters; it does not validate a predictive model or measure customer retention. The dataset source and redistribution terms still need to be identified before any external reuse.

Run the focused synthetic checks with `python -m unittest discover -s tests`.

**Repository description recommendation:** “Descriptive customer segmentation and satisfaction analysis on a single e-commerce snapshot.”
