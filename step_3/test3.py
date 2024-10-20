import unittest
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from solution3 import load_data, create_barplot

class Test3(unittest.TestCase):

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

        legend = plot.get_legend()
        self.assertEqual(legend.get_title().get_text(), 'genre',
                          "Expected title should be 'genre'.")

        frame=legend.get_frame()
        self.assertEqual(frame.get_facecolor(), (1.0, 1.0, 1.0, 0.8), 
                         msg="Expected legend frame facecolor to be white.")
        
        self.assertEqual(frame.get_edgecolor(), (1.0, 1.0, 1.0, 0.8), 
                         msg="Expected legend frame edgecolor to be white.")



        self.assertEqual(plot.get_xlabel(), 'platform', 
                        "Expected x axis label to be 'platform'.")

        
        self.assertEqual(plot.get_ylabel(), 'count', 
                        "Expected y axis label to be 'count'.")



        



