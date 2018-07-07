import numpy as np
import math


class Network:
    """ A Multi-Layer Perceptron"""

    def __init__(self, inputs, targets, nhidden, activation_function_provider, momentum=0.9):
        """ Constructor """
        # Set up network size
        self.nin = np.shape(inputs)[1]
        self.nout = np.shape(targets)[1]
        self.ndata = np.shape(inputs)[0]
        self.nhidden = nhidden

        self.momentum = momentum
        self.activation_function_provider = activation_function_provider

        # Initialise network
        self.weights1 = (np.random.rand(self.nin + 1, self.nhidden) - 0.5) * 2 / np.sqrt(self.nin)
        self.weights2 = (np.random.rand(self.nhidden + 1, self.nout) - 0.5) * 2 / np.sqrt(self.nhidden)

    def mlptrain(self, inputs, targets, eta, niterations):
        """ Train the thing """
        # Add the inputs that match the bias node
        inputs = np.concatenate((inputs, -np.ones((self.ndata, 1))), axis=1)

        updatew1 = np.zeros((np.shape(self.weights1)))
        updatew2 = np.zeros((np.shape(self.weights2)))

        for n in range(niterations):
            self.outputs = self.mlpfwd(inputs)
            error = 0.5 * np.sum((self.outputs - targets) ** 2)
            deltao = (self.outputs - targets) / self.ndata

            deltah = self.activation_function_provider.deltah(self.hidden,deltao,self.weights2)

            updatew1 = eta * (np.dot(np.transpose(inputs), deltah[:, :-1])) + self.momentum * updatew1
            updatew2 = eta * (np.dot(np.transpose(self.hidden), deltao)) + self.momentum * updatew2
            self.weights1 -= updatew1
            self.weights2 -= updatew2

    def mlpfwd(self, inputs):
        """ Run the network forward """

        self.hidden = np.dot(inputs, self.weights1)
        self.hidden = self.activation_function_provider.forward(self.hidden)
        self.hidden = np.concatenate((self.hidden, -np.ones((np.shape(inputs)[0], 1))), axis=1)

        outputs = np.dot(self.hidden, self.weights2)
        return outputs

    def accuracy(self, inputs, targets, epsilon, verbose=True):
        """Confusion matrix"""

        # Add the inputs that match the bias node
        inputs = np.concatenate((inputs, -np.ones((np.shape(inputs)[0], 1))), axis=1)
        outputs = self.mlpfwd(inputs)

        temp_outputs = outputs
        nrows = np.shape(targets)[0]

        difference = np.abs(outputs - targets)
        outputs = np.where( difference <= epsilon, 1, 0)
        correct_num = np.sum(np.where(outputs==1,1,0))

        accuracy = correct_num / nrows * 100

        if verbose:
            length = np.shape(targets)[0]

            print("inputs / output / target / difference")
            for i in range(length):
                print(inputs[i], " / %.5f / %.5f / %.5f" % (temp_outputs[i], targets[i], difference[i] ))

            print("accuracy: %.2f%%" % accuracy)

        return accuracy
