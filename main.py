from sys import argv

from data_loader import read_data


def main(file_name):
    read_data(file_name)


if __name__ == '__main__':
    main(argv[1])
