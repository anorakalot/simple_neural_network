from numpy import exp,array,random,dot

class NeuralNetwork(object):
    def __init__(self):

        random.seed()

        self.random_weights = 2 * random.random((3,1)) -1



    def __sigmoid(self,x):
        return 1/(1+exp(-x))

    def __sigmoid_derivative(self,x):
        return x * (1-x)

    def train(self,training_set_inputs,training_set_outputs,number_of_training_iterations):
        for step in xrange(number_of_training_iterations):

            output = self.think(training_set_inputs)

            error = training_set_outputs - output

            adjustment = dot(training_set_inputs.T,error * self.__sigmoid_derivative(output))

            self.random_weights += adjustment




    def think(self,inputs):
        return self.__sigmoid(dot(inputs,self.random_weights))






if __name__ == "__main__":
    neural_network = NeuralNetwork()

    print "Random starting weights"

    print neural_network.random_weights

    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    neural_network.train(training_set_inputs,training_set_outputs,10000)

    print "New weights after training: "

    print neural_network.random_weights

    print "Testing with new input! [1,0,0]"

    print neural_network.think(array([1,0,0]))
