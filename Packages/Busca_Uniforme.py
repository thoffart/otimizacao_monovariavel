class metodo():

    def __init__(self, fx, delta, a, b):
        self.fx = fx
        self.delta = delta
        self.a = a
        self.b = b

    def calculaux(self, x, aux, result1, result2, deltaux):
        while(result2 < result1 and aux < self.b):
            result1 = result2
            self.a = aux
            if(aux + self.delta < self.b):
                aux = aux + self.delta
            else:
                aux = self.b
            x = aux
            result2 = eval(self.fx)
        if result2 > result1:
            print('p(', self.a, ') = ', result1)
        else:
            print('p(', x, ') = ', result2)

    def calcula(self):
        x = self.a
        deltaux = self.delta
        aux = self.a + self.delta
        result1 = eval(self.fx)
        x = aux
        result2 = eval(self.fx)
        self.calculaux(x, aux, result1, result2, deltaux)
