import pandas as pd
import csv_to_sqlite
import sqlite3


# Read the csv file
def read_data(file_name):
    with open(file=file_name) as csv_file:
        csv_reader = pd.read_csv(csv_file)

    return csv_reader


# Convert the a csv file into database format
def data_to_db_format(file_name):
    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250")
    input_files = [file_name]

    return csv_to_sqlite.write_csv(input_files, "output.db", options)

