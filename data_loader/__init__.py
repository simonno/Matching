from pandas import read_csv

from data_loader.parser import convert_strings_enum


def read_data(file_name):
    dataset = read_csv(file_name)
    return convert_strings_enum(dataset.values)
