import unittest
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


sample_data = {
    'platform': ['PC', 'PC', 'PS4', 'PS4', 'WiiU', 'WiiU', 'XOne', 'XOne'],
    'genre': ['Action', 'Adventure', 'Platform', 'Puzzle', 'Shooter', 'Sports',
               'Fighting', 'Misc'],
    'count': [39, 8, 9, 1, 3, 2, 5, 17]
}
count_data = pd.DataFrame(sample_data)


def create_bar_plot(count_data, platforms, genre_order):
    plot = sb.barplot(x='platform', y='count', hue='genre', data=count_data, 
                      order=platforms, hue_order=genre_order)
    plt.show()
    return plot

class Test2(unittest.TestCase):

    def test_create_bar_plot(self):
        platforms = ['PS4', 'XOne', 'PC', 'WiiU']
        genre_order = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 
                       'Puzzle', 'Racing', 'Role-Playing', 'Shooter', 
                       'Simulation', 'Sports', 'Strategy']

       
        plot = create_bar_plot(count_data, platforms, genre_order)

        self.assertIsNotNone(plot, "This shouln't be None.")

        with self.subTest('Check x axis label'):
            self.assertEqual(plot.get_xlabel(), 'platform', 
                             "Expected x axis label to be 'platform'")
        
        with self.subTest('Check y axis label'):
            self.assertEqual(plot.get_ylabel(), 'count', 
                             "Expected y axis label to be 'count'")
        

        


