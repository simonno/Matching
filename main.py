from pandas import read_csv


def read_data(file_name):
    data = read_csv(file_name)
    return data


def main():
    print(read_data('data.csv'))


if __name__ == '__main__':
    main()