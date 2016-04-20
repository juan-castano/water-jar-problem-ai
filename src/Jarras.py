
from aima.search import Problem
from aima.search import breadth_first_search


class Jarras(Problem):

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.capacidadJ1 = 5
        self.capacidadJ2 = 3

    def actions(self, state):

        actions = ['verterJ1aJ2', 'verterJ2aJ1', 'vaciarJ1', 'vaciarJ2', 'llenarJ1', 'llenarJ2']

        # actions = ['vaciar', 'llenar']
        return actions

    def result(self, state, action):

        if action is 'verterJ1aJ2':
            cantidadJ1 = state[1]
            cantidadJ2 = state[3]
            j1 = 0
            j2 = 0
            deltaJ2 = self.capacidadJ2 - cantidadJ2

            if deltaJ2 > 0:

                if cantidadJ1 >= deltaJ2:
                    quedaEnJ1 = cantidadJ1 - deltaJ2
                    cantidadADepositar = cantidadJ1 - quedaEnJ1
                    j2 = cantidadJ2 + cantidadADepositar
                    j1 = quedaEnJ1
                else:
                    j2 = cantidadJ1 + cantidadJ2
                    j1 = 0

                state = ('J1', j1, 'J2', j2)
                return state
            return state

        elif action is 'verterJ2aJ1':
            cantidadJ1 = state[1]
            cantidadJ2 = state[3]
            j1 = 0
            j2 = 0

            deltaJ1 = self.capacidadJ1 - cantidadJ1

            if deltaJ1 > 0:

                if cantidadJ2 > deltaJ1:
                    quedaEnJ2 = cantidadJ2 - deltaJ1
                    cantidadADepositar = cantidadJ2 - quedaEnJ2
                    j1 = cantidadJ1 + cantidadADepositar
                    j2 = quedaEnJ2
                else:
                    j1 = cantidadJ2 + cantidadJ1
                    j2 = 0

                state = ('J1', j1, 'J2', j2)
                return state

            return state

        elif action is 'vaciarJ1':
            j1 = 0
            state = ('J1', j1, 'J2', state[3])
            return state

        elif action is 'vaciarJ2':
            j2 = 0
            state = ('J1', state[1], 'J2', j2)
            return state

        elif action is 'llenarJ1':
            j1 = self.capacidadJ1
            state = ('J1', j1, 'J2', state[3])
            return state

        elif action is 'llenarJ2':
            j2 = self.capacidadJ2
            state = ('J1', state[1], 'J2', j2)
            return state

    def goal_test(self, state):
        return self.goal == state

    def path_cost(self, c, state1, action, state2):
        pass

    def value(self, state):
        pass


def main():
    print("### Ejemplo 1 ###")
    initial = ('J1', 1, 'J2', 4)
    goal = ('J1', 4, 'J2', 0)
    jarras_problema = Jarras(initial, goal)
    result = breadth_first_search(jarras_problema)
    print("### Resultado ###")
    print(result)
    print("### Solucion ###")
    print(result.solution())

    print("### Recorrido ###")
    for node in result.path():
        print(node)

    print("### Ejemplo 2 ###")
    initial = ('J1', 0, 'J2', 0)
    goal = ('J1', 4, 'J2', 0)
    jarras_problema = Jarras(initial, goal)
    result = breadth_first_search(jarras_problema)
    print("### Resultado ###")
    print(result)
    print("### Solucion ###")
    print(result.solution())

    print("### Recorrido ###")
    for node in result.path():
        print(node)

    print("### Ejemplo 2 ###")
    initial = ('J1', 5, 'J2', 0)
    goal = ('J1', 4, 'J2', 0)
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
