# Interpretation notes for the customer snapshot

The supplied CSV has one row per customer and no transaction timestamps. `customer_segments.png` groups customers by days since last purchase, **item count**, and total spend. Item count is not purchase frequency, and cluster numbers are arbitrary labels rather than validated customer types.

`membership_satisfaction.png` shows the share of each satisfaction category within a membership type. It is not a retention cohort. The other plots describe spend, ratings, discounts and simple correlations within this snapshot. They do not establish that membership or discounts cause satisfaction, that a customer will churn, or that a proposed campaign would work.

The publisher and license for this CSV are still unverified. Reproduce the plots with `python main.py` and check the input before sharing any quantitative finding.
