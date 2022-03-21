import unittest
from werkzeug.datastructures import FileStorage
import io
import json
import pandas as pd
import json
import tempfile
from pandas import testing

from stse import web

# input_json = json.dumps(my_dict, indent=4).encode("utf-8")

# mock_file = FileStorage(
#     stream=open(buffer.name, 'rb'),
#     filename='ape.csv',
#     content_type='text/csv',
# )

# print(web.read_spreadsheet(mock_file))

class TestWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.DataFrame({
            'a': [1, 2, 3, 4],
            'b': ['a', 'b', 'c', 'd']
        })
        return super().setUpClass()
    
    def test_read_shreadsheet(self):
        # Test csv
        mock_file = web.store_df(self.df, 'csv')
        testing.assert_frame_equal(web.read_spreadsheet(mock_file), self.df)
        
        # Test excel
        mock_file = web.store_df(self.df, 'xlsx')
        testing.assert_frame_equal(web.read_spreadsheet(mock_file), self.df)
        
        # Test csv
        mock_file = web.store_df(self.df, 'tsv')
        testing.assert_frame_equal(web.read_spreadsheet(mock_file), self.df)
        
    # def test_store_df(self):
        