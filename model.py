import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.activations import relu
from tensorflow.keras.layers import Dense
from tensorflow.python.keras.activations import softmax
from tensorflow.python.keras.losses import SparseCategoricalCrossentropy


class FCNModel:

    def __init__(self):
        self.model = self.create_model()

    def create_model(self):
        model = Sequential()
        model.add(Dense(40, input_dim=5, activation=relu))
        model.add(Dense(20, activation=relu))
        model.add(Dense(19, activation=softmax))
        model.compile(loss=SparseCategoricalCrossentropy(from_logits=True), optimizer='adam', metrics=['accuracy'])
        return model

    def train(self, train_data_x, train_data_y):
        self.model.fit(train_data_x, train_data_y, epochs=100)

    def test(self, dev_data_x, dev_data_y):
        number_of_correct_answers = 0
        for (sample, tag) in zip(dev_data_x, dev_data_y):
            arr = np.array(sample)
            probabilites = self.model.predict_proba(arr.reshape((1, 5)), verbose=2)[0]
            max_index = None
            max_proba = 0
            for i, proba in enumerate(probabilites):
                if proba > max_proba:
                    max_index = i + 1
                    max_proba = proba
            if max_index == tag:
                number_of_correct_answers += 1
        print("Accuracy : " + str(number_of_correct_answers / len(dev_data_y)))
