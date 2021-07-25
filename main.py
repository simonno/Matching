from sys import argv

from data_loader import read_data
from model import FCNModel


def main(file_name):
    data = read_data(file_name)
    model = FCNModel()
    model.train(data)


if __name__ == '__main__':
    main(argv[1])
