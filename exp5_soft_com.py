import numpy as np


# Activation function: Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of Sigmoid (for backpropagation)
def sigmoid_derivative(x):
    return x * (1 - x)


# MLP Class
class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights
        self.weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size))

        # Initialize biases
        self.bias_hidden = np.random.uniform(-1, 1, (1, hidden_size))
        self.bias_output = np.random.uniform(-1, 1, (1, output_size))

    def forward(self, inputs):
        # Forward pass from input layer to hidden layer
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        # Forward pass from hidden layer to output layer
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_layer_input)

        return self.output

    def backward(self, inputs, actual_output, predicted_output, learning_rate):
        # Calculate the error (predicted - actual)
        output_error = actual_output - predicted_output
        output_delta = output_error * sigmoid_derivative(predicted_output)

        # Calculate error for hidden layer
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer_output)

        # Update weights and biases
        self.weights_hidden_output += np.dot(self.hidden_layer_output.T, output_delta) * learning_rate
        self.weights_input_hidden += np.dot(inputs.T, hidden_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

    def train(self, inputs, actual_output, epochs, learning_rate):
        for epoch in range(epochs):
            predicted_output = self.forward(inputs)
            self.backward(inputs, actual_output, predicted_output, learning_rate)

    def predict(self, inputs):
        return self.forward(inputs)


# Example: XOR Problem
if __name__ == "__main__":
    # XOR Input and Output (0/1)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    actual_output = np.array([[0], [1], [1], [0]])

    # Define MLP parameters: 2 input nodes, 4 hidden nodes, 1 output node
    mlp = MLP(input_size=2, hidden_size=4, output_size=1)

    # Train the MLP
    epochs = 10000
    learning_rate = 0.1
    mlp.train(inputs, actual_output, epochs, learning_rate)

    # Test the MLP
    print("Predicted output after training:")
    print(mlp.predict(inputs))


