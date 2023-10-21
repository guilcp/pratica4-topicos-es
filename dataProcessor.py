import json
import pandas as pd

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
def avg_age_country(filePath, format = 'years'):
    data = read_json_file(filePath)

    df = pd.DataFrame(data)

    if format == 'months':
        df['age'] *= 12
    elif format == 'days':
        df['age'] *= 365

    avg_age = df.groupby('country').mean()

    print(avg_age)

    return avg_age.to_dict()

def max_age_country(filePath):
    data = read_json_file(filePath)
    
    df = pd.DataFrame(data)
    
    max_age = df.groupby('country')['age'].max()
    
    print(max_age)
    
    return max_age.to_dict()