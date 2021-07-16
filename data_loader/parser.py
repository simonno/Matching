from datetime import datetime

from authorities import Authorities
from data_sample import Sample


def parse_preferences(values):
    preferences = [Authorities]
    for value in values:
        authority = Authorities.from_string(value)
        if authority:
            preferences.append(authority)
        else:
            continue
    return preferences


def parse_final(value):
    return Authorities.from_string(value)


def convert_strings_enum(dataset):
    samples = [Sample]
    for row in dataset:
        final = parse_final(row[-1])
        if final:
            samples.append(
                Sample(timestamp=datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S'),
                       preferences=parse_preferences(row[1:-1]),
                       final=final))
    return samples
