import unittest
import os
import pandas as pd
from solution1 import load_data, filter_and_group


class Test1(unittest.TestCase):
        def setUp(self):
            self.csv_file='dataset.csv'
            self.platforms = ['PS4', 'XOne', 'PC', 'WiiU']
        
        def test_load_csv(self):
            try:
                data_csv = load_data(self.csv_file)
            except Exception as e:
                self.fail(f'Loading CSV failed with an error: {e}')
            
            self.assertFalse(data_csv.empty, 'The CSV file is empty.') 

            wanted_columns = ['platform', 'genre']
            for column in wanted_columns:
                self.assertIn(column, data_csv.columns, f'Missing wanted column: {column}.')
            
        def test_filtered_data(self):
            data_csv = load_data(self.csv_file)
            filtered_data = data_csv[data_csv['platform'].isin(self.platforms)]
            self.assertFalse(filtered_data.empty, 'The filtered data is empty.')

        def test_groupby_count(self):
            data_csv = load_data(self.csv_file)
            count_data=filter_and_group(data_csv)
            self.assertIn('platform', count_data.columns, 'Expected column: platform.')
            self.assertIn('genre', count_data.columns, 'Expected column: genre.')
            self.assertIn('count', count_data.columns, 'Expected colunmn: count.')

             

             

        
