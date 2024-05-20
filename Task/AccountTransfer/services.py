import pandas as pd


import pandas as pd


def read_file(file_path):
    """
    Read a file and return its contents as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the file.

    Returns:
    dictionary : of data .
    """
    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'csv':
        df = pd.read_csv(file_path)
    elif file_extension == 'json':
        df = pd.read_json(file_path)
    elif file_extension in ['xls', 'xlsx']:
        df = pd.read_excel(file_path)
    elif file_extension == 'html':
        df = pd.read_html(file_path)[0]
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

    if not df.empty:
        data = df.to_dict(orient='list')
        return data
    


