import pandas as pd


def read_data(file_name):
    with open(file=file_name) as csv_file:
        csv_reader = pd.read_csv(csv_file)

    return csv_reader