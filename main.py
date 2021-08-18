import random
from sys import argv

from model import FCNModel
from data_loader import read_data

random.seed(1)
def calc_preferences_of_soldier(line):
    preferences = []
    for j, preference in enumerate(line.preferences):
        if j == 0:
            continue
        preferences += [line.preferences[j].value]
    for k in range(j, 5):
        preferences += [-1]
    return preferences


def calc_probability_per_force(x):
    probabilities = [[], [], [], [], []]
    for line in x:
        for i in range(5):
            if line[i] != -1:
                probabilities[i] += [line[i]]

    return probabilities


def replace_nones_with_data(x, probabilities_per_force):
    for line in x:
        for i in range(5):
            if line[i] == -1:
                line[i] = random.sample(probabilities_per_force[i], 1)[0]


if __name__ == '__main__':
    data = read_data(argv[1])
    fcn = FCNModel()
    x = []
    y = []
    counter = 0
    for i, line in enumerate(data):
        if i == 0:  # head
            continue
        # if len(line.preferences) < 5: # skip lines with none values
        #     continue
        preferences = calc_preferences_of_soldier(line)
        x += [preferences]
        y += [line.final.value]
    probabilities_per_force = calc_probability_per_force(x)
    replace_nones_with_data(x, probabilities_per_force)
    dev_size = 15
    temp = list(zip(x, y))
    # random.shuffle(temp)
    x, y = zip(*temp)
    train_data_x = x[:-dev_size]
    train_data_y = y[:-dev_size]
    dev_data_x = x[-dev_size:]
    dev_data_y = y[-dev_size:]
    fcn.model.fit(train_data_x, train_data_y, epochs=50)
    test_loss, test_acc = fcn.model.evaluate(dev_data_x, dev_data_y, verbose=2)
    # fcn.test(dev_data_x,dev_data_y)

    print('\nTest accuracy:', test_acc)
