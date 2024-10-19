import unittest
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from solution2 import load_data, create_barplot

class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_csv = load_data('dataset.csv')

    def test_create_bar_plot(self):
        platforms = ['PS4', 'XOne', 'PC', 'WiiU']
        genre_order = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 
                       'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 
                       'Simulation', 'Sports', 'Strategy']

        plot = create_barplot(self.data_csv, platforms, genre_order)

        self.assertIsNotNone(plot, "The plot should not be None.")

        with self.subTest('Check x axis label'):
            self.assertEqual(plot.get_xlabel(), 'platform', 
                             "Expected x axis label to be 'platform'.")

        with self.subTest('Check y axis label'):
            self.assertEqual(plot.get_ylabel(), 'count', 
                             "Expected y axis label to be 'count'.")

        


