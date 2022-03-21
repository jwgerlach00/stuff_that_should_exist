import pandas as pd
import warnings
from werkzeug.datastructures import FileStorage
import tempfile
import mimetypes


def read_spreadsheet(file, return_ext=False):  # *

    # Get file MIME
    file_mime = file.content_type

    # Read CSV
    if file_mime == 'text/csv':
        file_ext = 'csv'

        # Read in data
        input_data = pd.read_csv(file)
        
    # Read TSV
    elif file_mime == 'text/tab-separated-values':
        file_ext = 'tsv'

        # Read in data
        input_data = pd.read_csv(file, sep='\t')
        
    # Read Excel
    elif (file_mime == 'application/vnd.ms-excel' or
        file_mime == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
        file_ext = 'xlsx'

        # Read in data
        input_data = pd.read_excel(file)

    # Unsupported filetype
    else:
        warnings.warn(f'"{file_mime}" is not a supported filetype.')


    return (input_data, file_ext) if return_ext else input_data

def store_df(df, ext):
    
    buffer = tempfile.NamedTemporaryFile()
    if ext == 'csv':
        df.to_csv(buffer, index=False)
    elif ext == 'xlsx':
        df.to_excel(buffer, index=False)
    elif ext == 'tsv':
        df.to_csv(buffer, index=False, sep='\t')
    else:
        raise('Only "csv", "xlsx" and "tsv" extensions are accepted')
    
    type = mimetypes.guess_type(f'_.{ext}')[0]
    
    return FileStorage(
            stream=open(buffer.name, 'rb'),
            filename=f'test.{ext}',
            content_type=type,
    )