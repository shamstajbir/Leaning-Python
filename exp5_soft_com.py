import numpy as np


# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Mean Squared Error loss function and its derivative
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def mse_derivative(y_true, y_pred):
    return y_pred - y_true


# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.random.rand(hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.random.rand(output_size)

    def forward_propagation(self, X):
        # Hidden layer
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)

        # Output layer
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_input)

        return self.output

    def back_propagation(self, X, y, learning_rate):
        # Calculate output error
        output_error = mse_derivative(y, self.output)
        output_delta = output_error * sigmoid_derivative(self.output)

        # Calculate hidden layer error
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)

        # Update weights and biases for hidden -> output
        self.weights_hidden_output -= self.hidden_output.T.dot(output_delta) * learning_rate
        self.bias_output -= np.sum(output_delta, axis=0) * learning_rate

        # Update weights and biases for input -> hidden
        self.weights_input_hidden -= X.T.dot(hidden_delta) * learning_rate
        self.bias_hidden -= np.sum(hidden_delta, axis=0) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        for _ in range(epochs):
            self.forward_propagation(X)
            self.back_propagation(X, y, learning_rate)


# Example usage
if __name__ == "__main__":
    # Define input and output
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])

    # Create Neural Network
    nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

    # Train the network
    nn.train(X, y, epochs=10000, learning_rate=0.1)

    # Test the network
    output = nn.forward_propagation(X)
    print("Predicted Output:")
    print(output)

