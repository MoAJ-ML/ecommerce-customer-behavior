import tempfile
import unittest
from pathlib import Path

import pandas as pd

import main


class AnalysisTests(unittest.TestCase):
    def test_membership_chart_is_a_distribution(self):
        frame = pd.DataFrame({
            'Customer ID': [1, 2, 3, 4],
            'Membership Type': ['Gold', 'Gold', 'Silver', 'Silver'],
            'Satisfaction Level': ['High', 'Low', 'High', 'High'],
        })
        with tempfile.TemporaryDirectory() as tmp:
            old = main.VIS_DIR
            main.VIS_DIR = tmp
            try:
                result = main.membership_satisfaction_analysis(frame)
                self.assertTrue((Path(tmp) / 'membership_satisfaction.png').exists())
            finally:
                main.VIS_DIR = old
            self.assertTrue((result.sum(axis=1) == 1).all())
            self.assertEqual(result.loc['Gold', 'High'], 0.5)

    def test_tracked_zip_is_a_clean_clone_input(self):
        frame = main.load_and_clean_data('data/E-commerce Customer Behavior - Sheet1.csv')
        self.assertGreater(len(frame), 0)
        self.assertIn('Items Purchased', frame.columns)


if __name__ == '__main__':
    unittest.main()
