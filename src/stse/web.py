import pandas as pd


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
        raise(f'"{file_mime}" is not a supported filetype.')


    return (input_data, file_ext) if return_ext else input_data
