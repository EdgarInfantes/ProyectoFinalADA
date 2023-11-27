#grafo={(1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (2, 6): 1, (5, 6): 1}

class Operaciones:
    def getVecinos(grafo,nodo):
        vecinos = []
        for arista, peso in grafo.items():
            #print(arista)
            if(arista[0]==nodo):
                vecinos.append(arista[1])
            if(arista[1]==nodo):
                vecinos.append(arista[0])
        return vecinos
        