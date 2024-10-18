import unittest
import os
import pandas as pd


class Test1(unittest.TestCase):
        def setUp(self):
            self.csv_file='../dataset.csv'
            self.platforms = ['PS4', 'XOne', 'PC', 'WiiU']
        
        def test_csv_file_exists(self):
            self.assertTrue(os.path.exists(self.csv_file), 'CSV file not found.')
        
        def test_load_csv(self):
            try:
                data_csv = pd.read_csv(self.csv_file)
            except Exception as e:
                self.fail(f'Loading CSV failed with an error: {e}')
            
            self.assertFalse(data_csv.empty, 'The CSV file is empty.') 

            wanted_columns = ['platform', 'genre']
            for column in wanted_columns:
                self.assertIn(column, data_csv.columns, f'Missing wanted column: {column}')
            
        def test_filtered_data(self):
            data_csv = pd.read_csv(self.csv_file)
            filtered_data = data_csv[data_csv['platform'].isin(self.platforms)]
            self.assertFalse(filtered_data.empty, 'The filtered data is empty.')

        def test_groupby_count(self):
            data_csv = pd.read_csv(self.csv_file)
            filtered_data = data_csv[data_csv['platform'].isin(self.platforms)]
            count_data = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='count')
            self.assertIn('platform', count_data.columns)
            self.assertIn('genre', count_data.columns)
            self.assertIn('count', count_data.columns)

             

        