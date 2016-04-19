from aima.search import Problem
from aima.search import breadth_first_search


class Jarras(Problem):

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.size_J1 = 5
        self.size_J2 = 3

    def actions(self, state):
        print(state)
        return ['verterJ1aJ2', 'verterJ2aJ1', 'vaciarJ1', 'vaciarJ2',
                'llenarJ1', 'llenarJ2']

    def result(self, state, action):
        print(action)
        if (action is 'verter'):
            J1 = state.J1
            J2 = state.J2

            """
            Verifica la cantidad que tiene la JARRA 2 con respecto a su
            capacidad total
            """
            delta = self.size_J2 - J2

            retirar_liquido = J1 - delta  # Retira liquido de la JARRA 1
            new_J2 = retirar_liquido + J2


            pass
        elif (action is 'vaciar'):
            pass
        elif (action is 'llenar'):
            pass


    def goal_test(self, state):
        return self.goal == state

    def path_cost(self, c, state1, action, state2):
        pass

    def value(self, state):
        pass


def main():
    initial = dict(J1=0, J2=4)
    goal = dict(J1=0, J2=4)
    jarras_problema = Jarras(initial, goal)
    result = breadth_first_search(jarras_problema)
    print(result)


if __name__ == '__main__':
    main()
