import numpy as np

class Perceptron:
    def __init__(self, num_inputs, learning_rate=0.01, num_epochs=100):
        self.num_inputs = num_inputs
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = np.random.randn(num_inputs)
        self.bias = np.random.randn()

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights) + self.bias
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels):
        for _ in range(self.num_epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights += self.learning_rate * (label - prediction) * inputs
                self.bias += self.learning_rate * (label - prediction)


# Example usage
training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])

perceptron = Perceptron(num_inputs=2)
perceptron.train(training_inputs, labels)

# Test the trained perceptron
test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for inputs in test_inputs:
    print(f"Input: {inputs} Predicted Output: {perceptron.predict(inputs)}")

