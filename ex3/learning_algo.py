import random


class PerceptronLearning:
    def __init__(self, d, dt, i, t):
        self.data = d
        self.data_type = dt
        self.iterations = i
        self.threshold = t
        self.weights = [random.uniform(-self.threshold, self.threshold) for _ in range(len(self.data)-1)]
        self.learn()

    def __repr__(self):
        return "Data: %s Data type: %s Iterations: %i Threshold: %f  Weights: %s" % \
               (self.data, self.data_type, self.iterations, self.threshold, self.weights)

    def learn(self):
        unit_step = lambda x: 0 if x < 0 else 1

        print("Learning: %s" % self.data_type)
        for count in range(self.iterations):
            errors = 0
            for input, desired_output in self.data:
                result = sum([i*j for i, j in zip(input, self.weights)])
                error = desired_output - unit_step(result)

                print('Weights: %s' % self.weights)

                if error:
                    errors += 1
                    for index, value in enumerate(input):
                        self.weights[index] += 0.1 * error * value

            # Break loop if not getting errors
            if errors == 0:
                break

        print('\n' + 'Final weights: ')
        print('Weights: %s' % self.weights)
        return self.weights

if __name__ == "__main__":
    i = 100
    t = 0.5

    learning_data = {'AND': [((1, 0, 0), 0), ((1, 0, 1), 0), ((1, 1, 0), 0), ((1, 1, 1), 1)],
                     'OR': [((1, 0, 0), 0), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 1)],
                     'NAND': [((1, 0, 0), 1), ((1, 0, 1), 1), ((1, 1, 0), 1), ((1, 1, 1), 0)]}

    a = PerceptronLearning(learning_data['AND'], "AND", i, t)
    #b = PerceptronLearning(learning_data['OR'], "OR", i, t)










