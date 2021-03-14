from util import read_data, data_to_db_format

if __name__ == '__main__':
    file_path = "/home/renos/Downloads/archive/aug_train.csv"
    res = read_data(file_name=file_path)
    print(res.head(5))