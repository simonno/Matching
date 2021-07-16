import csv


def svc_reader(file_name):
    with open(file_name, 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)  # skip the first row - the headers
        return reader
