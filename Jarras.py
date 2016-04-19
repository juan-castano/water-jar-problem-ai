
from random import randint

from aima.search import Problem
from aima.search import breadth_first_search


class Jarras(Problem):

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """
        self.actions = ['verterJ1aJ2', 'verterJ2aJ1', 'vaciarJ1', 'vaciarJ2',
                        'llenarJ1', 'llenarJ2']
        """
        self.actions = ['vaciar', 'llenar']
        return self.actions

    def result(self, state, action):
        print(state)
        print(action)
        if (action is 'vaciar'):
            J1 = 0
            J2 = 0
            state = ('J1', J1, 'J2', J2)
            return state
        elif (action is 'llenar'):
            J1 = 5
            J2 = 3
            state = ('J1', J1, 'J2', J2)
            return state
        '''
        if (action is 'verterJ1aJ2'):

            J1 = state.J1
            J2 = state.J2

            """
            Verifica la cantidad que tiene la JARRA 2 con respecto a su
            capacidad total
            """
            delta = self.size_J2 - J2

            retirar_liquido = J1 - delta  # Retira liquido de la JARRA 1
            new_J2 = retirar_liquido + J2

            state.J1 = 3
            state.J2 = 1
            return state

        elif (action is 'verterJ2aJ1'):
            state.J1 = 3
            state.J2 = 1
            return state

        elif (action is 'vaciarJ1'):
            state.J1 = 3
            state.J2 = 1
            return state

        elif (action is 'vaciarJ2'):
            state.J1 = 3
            state.J2 = 1
            return state

        elif (action is 'llenarJ1'):
            state.J1 = 3
            state.J2 = 1
            return state

        elif (action is 'llenarJ2'):
            state.J1 = 3
            state.J2 = 1
            return state
        else:
            return state

        '''

    def goal_test(self, state):
        return self.goal == state

    def path_cost(self, c, state1, action, state2):
        pass

    def value(self, state):
        pass


def main():
    """
    initial = dict(J1=1, J2=4)
    goal = dict(J1=5, J2=3)
    initial_node = Node(initial)
    goal_node = Node(goal)
    # jarras_problema = Jarras(initial, goal)
    jarras_problema = Jarras(initial_node.state, goal_node.state)
    print(jarras_problema.initial)
    print(jarras_problema.goal)
    result = breadth_first_search(jarras_problema)
    print(type(result))
    """

    initial = ('J1', 1, 'J2', 4)
    goal = ('J1', 5, 'J2', 3)
    jarras_problema = Jarras(initial, goal)
    # print(jarras_problema.initial)
    # print(jarras_problema.goal)
    result = breadth_first_search(jarras_problema)
    print(result.solution())

if __name__ == '__main__':
    main()
