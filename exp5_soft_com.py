import numpy as np

X = np.array([[1, 0, 1, 0],
              [1, 0, 1, 1],
              [0, 1, 0, 1]
              ])

print('\ninput:')
print(X)

y = np.array([[1], [1], [0]])

print('\nActual Output:')
print(y)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derivatives_sigmoid(x):
    return x * (1 - x)


epoch = 5000
lr = 0.1
inputlayer_nerourns = X.shape[1]
hiddenlayer_nerourns = 3
output_neurons = 1

wh = np.random.uniform(size=(inputlayer_nerourns, hiddenlayer_nerourns))
bh = np.random.uniform(size=(1, hiddenlayer_nerourns))
wout = np.random.uniform(size=(hiddenlayer_nerourns, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for i in range(epoch):
    hidden_layer_input1 = np.dot(X, wh)
    hidden_layer_input = hidden_layer_input1 + bh
    hidden_layer_activations = sigmoid(hidden_layer_input)

    output_layer_input1 = np.dot(hidden_layer_activations, wout)
    output_layer_input = output_layer_input1 + bout
    output = sigmoid(output_layer_input)

    E = y - output
    slope_output_layer = derivatives_sigmoid(output)
    slope_hidden_layer = derivatives_sigmoid(hidden_layer_activations)
    d_output = E * slope_output_layer

    Error_at_hidden_layer = d_output.dot(wout.T)
    d_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer

    wout += hidden_layer_activations.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

print('\nOutput form the model:')
print(output)