# E-commerce Customer Behavior Analysis

## Overview
This project analyzes customer behavior for an e-commerce business using Python. It includes RFM (Recency, Frequency, Monetary) analysis, cohort analysis, and visualizations to uncover actionable insights about customer purchase patterns and satisfaction.

## Features
- **RFM Analysis**: Segments customers based on recency, frequency, and monetary value.
- **Cohort Analysis**: Tracks customer retention and behavior over time.
- **Visualizations**: Includes boxplots, heatmaps, and scatterplots to illustrate key findings.
- **Actionable Insights**: Provides data-driven recommendations for business strategy.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ecommerce-customer-behavior.git
   cd ecommerce-customer-behavior
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place your dataset in the `data/` directory.
2. Run the analysis:
   ```bash
   python main.py
   ```
3. View the generated visualizations in the `visualization/` directory.

## Project Structure
```
.
├── data/                    # Dataset directory
│   └── E-commerce Customer Behavior - Sheet1.csv
├── visualization/           # Generated visualizations
│   ├── rfm_segments.png
│   ├── cohort_retention_curve.png
│   ├── spend_by_membership.png
│   ├── discount_vs_rating.png
│   ├── correlation_heatmap.png
│   └── summary_insights.md
├── main.py                  # Main analysis script
├── requirements.txt         # Dependencies
└── README.md                # This file
```

## Dependencies
- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

## Contributing
Feel free to submit issues or pull requests for improvements.

## License
This project is open-source and available under the [MIT License](LICENSE).
