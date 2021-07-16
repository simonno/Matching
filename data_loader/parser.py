from datetime import datetime

from authorities import Authorities
from data_sample import Sample


def convert_strings_enum(dataset):
    samples = [Sample]
    for row in dataset:
        samples.append(
            Sample(timestamp=datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S'),
                   preferences=[Authorities.from_string(value) for value in row[1:-1]],
                   final=Authorities.from_string(row[-1])))
    return samples
