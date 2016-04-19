
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
        actions = ['vaciar', 'llenar']
        return actions

    def result(self, state, action):
        if action is 'vaciar':

            if state[1] != 0 or state[3] != 0:
                j1 = 0
                j2 = 0
                state = ('J1', j1, 'J2', j2)
                return state

            return state

        elif action is 'llenar':

            if state[1] == 0 and state[3] == 0:
                j1 = 5
                j2 = 3
                state = ('J1', j1, 'J2', j2)
                return state

            return state

    def goal_test(self, state):
        return self.goal == state

    def path_cost(self, c, state1, action, state2):
        pass

    def value(self, state):
        pass


def main():

    initial = ('J1', 1, 'J2', 4)
    goal = ('J1', 5, 'J2', 3)
    jarras_problema = Jarras(initial, goal)
    result = breadth_first_search(jarras_problema)
    print("### Resultado ###")
    print(result)
    print("### Solucion ###")
    print(result.solution())

    print("### Recorrido ###")
    for node in result.path():
        print(node)

if __name__ == '__main__':
    main()
