
class Reasoner:
    def __init__(self, crisp_x, crisp_y):
        self.crisp_x = crisp_x
        self.crisp_y = crisp_y

        # Dictionary to keep track of the intersection value of the distance graphs and the crisp x
        self.distance = {'verysmall': 0, 'small': 0, 'perfect': 0, 'big': 0, 'verybig': 0}

        # Dictionary to keep track of the intersection value of the delta graphs and crisp y
        self.delta = {'shrinkingfast': 0, 'shrinking': 0, 'stable': 0, 'growing': 0, 'growingfast': 0}

        # Dictionary to keep track of the outputs of each action
        self.actions = {'none': 0, 'slowdown': 0, 'speedup': 0, 'floorit': 0, 'brakehard': 0}

    def __repr__(self):
        return '\n' + "CRISP_X: " + str(self.crisp_x) + \
               '\n' + "CRISP_Y: " + str(self.crisp_y) + \
               '\n'*2 + "DISTANCE: " + str(self.distance) + \
               '\n'*2 + "DELTA: " + str(self.delta) + '\n'*2 \
               + "ACTIONS: " + str(self.actions) + '\n'

    def fuzzification(self):
        self.distance['verysmall'] = self.reverse_grade(self.crisp_x, 0.0, 2.5, 1.0)
        self.distance['small'] = self.triangle(self.crisp_x, 1.5, 3.0, 4.5, 1.0)
        self.distance['perfect'] = self.triangle(self.crisp_x, 3.5, 5.0, 6.5, 1.0)
        self.distance['big'] = self.triangle(self.crisp_x, 5.5, 7.0, 8.5, 1.0)
        self.distance['verybig'] = self.grade(self.crisp_x, 7.5, 10.0, 1.0)

        self.delta['shrinkingfast'] = self.reverse_grade(self.crisp_y, -4.0, -2.5, 1.0)
        self.delta['shrinking'] = self.triangle(self.crisp_y, -3.5, -2, -0.5, 1.0)
        self.delta['stable'] = self.triangle(self.crisp_y, -1.5, 0, 1.5, 1.0)
        self.delta['growing'] = self.triangle(self.crisp_y, 0.5, 2, 3.5, 1.0)
        self.delta['growingfast'] = self.grade(self.crisp_y, 2.5, 4, 1.0)

    def rule_evaluation(self):
        self.actions['none'] = min(self.distance['small'], self.delta['growing'])        # Rule 1
        self.actions['slowdown'] = min(self.distance['small'], self.delta['stable'])     # Rule 2
        self.actions['speedup'] = min(self.distance['perfect'], self.delta['growing'])   # Rule 3
        self.actions['floorit'] = min(self.distance['verybig'],                          # Rule 4
                                      max(1 - self.delta['growing'], 1- self.delta['growingfast']))
        self.actions['brakehard'] = self.distance['verysmall']                           # Rule 5

    def defuzzification(self):
        above = (((-10 - 9 - 8 - 7 - 6 - 5) * self.actions['brakehard'])
                 + ((-7 - 6 - 5 - 4 - 3 - 2 - 1) * self.actions['slowdown'])
                 + ((-3 - 2 - 1 + 0 + 1 + 2 + 3) * self.actions['none'])
                 + ((1 + 2 + 3 + 4 + 5 + 6 + 7) * self.actions['speedup'])
                 + ((5 + 6 + 7 + 8 + 9 + 10) * self.actions['floorit']))
        below = (self.actions['brakehard'] * 6
                 + self.actions['slowdown'] * 7
                 + self.actions['none'] * 7
                 + self.actions['speedup'] * 7
                 + self.actions['floorit'] * 6)




        print("COG: " + '%.2f' % (above / below))

    def triangle(self, pos, x0, x1, x2, clip):
        value = 0.0
        if x0 <= pos <= x1:
            value = (pos - x0) / (x1 - x0)
        elif x1 <= pos <= x2:
            value = (x2 - pos) / (x1 - x0)
        if value > clip:
            value = clip
        return value

    def grade(self, position, x0, x1, clip):
        value = 0.0
        if position >= x1:
            value = 1.0
        elif position <= x0:
            value = 0.0
        else:
            value = (position-x0)/(x1-x0)
        if value > clip:
            value = clip
        return value

    def reverse_grade(self, position, x0, x1, clip):
        value = 0.0
        if position <= x0:
            value = 1.0
        elif position >= x1:
            value = 0.0
        else:
            value = (x1-position)/(x1-x0)
        if value > clip:
            value = clip
        return value

if __name__ == '__main__':

    crisp_x_value = 3.9
    crisp_y_value = 1.4

    reasoner = Reasoner(crisp_x_value, crisp_y_value)

    # Step 1
    reasoner.fuzzification()

    # Step 2
    reasoner.rule_evaluation()

    # Step 4
    reasoner.defuzzification()

    # Printing rest of values in the reasoner
    print(reasoner)









