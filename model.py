from tensorflow.keras import Sequential
from tensorflow.keras.activations import relu, linear
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


class FCNModel:

    def __init__(self):
        self.lr = 0.001
        self.model = self.create_model()

    def create_model(self):
        model = Sequential()
        model.add(Dense(10, input_dim=5, activation=relu))
        model.add(Dense(5, activation=relu))
        model.add(Dense(1, activation=linear))
        model.compile(loss='mse', optimizer=Adam(lr=self.lr))
        return model

    def train(self, data):
        number_of_epochs = 3
        for _ in range(number_of_epochs):
            x = []
            y = []
            for i, line in enumerate(data):
                if i == 0:  # head
                    continue
                preferences = self.calc_preferences_of_soldier(line)
                x += [preferences]
                y += [line.final.value]
            dev_size = 17
            train_data_x = x[:-dev_size]
            train_data_y = y[:-dev_size]
            dev_data_x = x[-dev_size:]
            dev_data_y = y[-dev_size:]
            # np.random.shuffle(train_data_x)
            # np.random.shuffle(train_data_y)
            self.model.fit(train_data_x, train_data_y, validation_data=(dev_data_x, dev_data_y))

    @staticmethod
    def calc_preferences_of_soldier(line):
        preferences = []
        for j, preference in enumerate(line.preferences):
            if j == 0:
                continue
            preferences += [line.preferences[j].value]
        for k in range(j, 5):
            preferences += [-1]
        return preferences
