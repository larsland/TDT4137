import random
from pybrain.datasets.supervised import SupervisedDataSet
from pybrain.structure import TanhLayer
from pybrain.supervised.trainers.backprop import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork


def train(input, hidden, output, dataset):
    """
    Method to build and train a neural network with backpropagation until it converges
    :param input: input nodes for network (1)
    :param hidden: hidden nodes for network
    :param output: output nodes for network (1)
    :param dataset: SupervisedDataSet, maps input->output: 1->1, 2->2 ... 8->8
    :return: the trained neural network
    """
    net = buildNetwork(input, hidden, output, hiddenclass=TanhLayer)
    trainer = BackpropTrainer(net, dataset, learningrate=0.01)
    trainer.trainUntilConvergence(verbose=False, validationProportion=0.15, maxEpochs=1000, continueEpochs=10)

    return net


def activate_various():
    """
    Method to activate the neural network with random generated
    integers between -10, 10, which is outside the training set and print output
    """
    net = train(1, 4, 1, dataset)
    print("---------------------------------------")
    print("Network with random float inputs between -10,10")
    print("---------------------------------------")
    for i in values:
        print("Input: %.5f, Output: %.5f" % (i, net.activate([i])[0]))


def decreasing_hidden_nodes():
    """
    Method to activate the neural network with decreasing number
    of hidden nodes, from 8 to 1
    """
    for hidden in reversed(range(1, 9)):
        net = train(1, hidden, 1, dataset)
        print("-----------------------------")
        print("Network with %i hidden nodes" % hidden)
        print("-----------------------------")
        for i in range(1, 9):
            print("Input: %i, Output: %.5f" % (i, net.activate([i])[0]))


if __name__ == "__main__":

    dataset = SupervisedDataSet(1, 1)
    for i in range(1, 9):
        dataset.addSample(i, i)

    values = [random.uniform(-15, 15) for _ in range(0, 9)]

    activate_various()
    decreasing_hidden_nodes()













