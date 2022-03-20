from werkzeug.datastructures import FileStorage
import io
import json
import pandas as pd
import json

from stse import web

# Here we are mocking a JSON file called Input.json
my_dict = 'testing'
df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': ['a', 'b', 'c', 'd']
})

print(df)

buffer = io.BytesIO()
# df.to_json('data/web_test.json')
df.to_csv(buffer)

print(buffer)

# input_json = json.dumps(my_dict, indent=4).encode("utf-8")

mock_file = FileStorage(
    stream=buffer,
    filename='ape.csv',
    content_type='text/csv',
)
# print(mock_file)
print(pd.read_json('data/web_test.json'))
# print(web.read_spreadsheet(mock_file))
print(mock_file)
print(mock_file.read())
