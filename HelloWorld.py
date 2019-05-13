from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'


class HelloProblem(SearchProblem):
    # se tamanho do estado for menor que tamanho do goal
    # retorna lista com alfabeto, senão, retorna lista vazia

    def actions(self, state):
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    # entrada instancia do obj, estado e ação/ retorna como resultado estado + ação
    def result(self, state, action):
        return state + action

    # define meta com entrada para instancia do obj e estado/ retorna se estado é igual à meta
    def is_goal(self, state):
        return state == GOAL

    # define a heuristica do problema, com entrada pra instancia do obj e estado/ retorna o erro e o quanto falta
    def heuristic(self, state):
        # how far are we from the goal?
        # erro = se estado[i] diferente do objetivo[i] então 1, senão 0 e itera com for no range(tamanho do estado do parametro)
        # o quanto falta = tamanho do objetivo menos o tamanho do estado do parametro
        wrong = sum([1 if state[i] != GOAL[i] else 0
                    for i in range(len(state))])
        missing = len(GOAL) - len(state)
        return wrong + missing

# declara var problema igual a classe de helloProblem, com entrada do estado inicial vazio
problem = HelloProblem(initial_state='')

# declara var de resultado e recebe o processamento do problema com o algoritmo de A*
result = astar(problem)

#mostra o estado inicial do resultado e o caminho feito
print(result.state)
print(result.path())