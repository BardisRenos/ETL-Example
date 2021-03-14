from util import read_data

if __name__ == '__main__':
    file_path = "/home/renos/Downloads/archive/aug_train.csv"
    res = read_data(file_name=file_path)
    print(res.head(5))

