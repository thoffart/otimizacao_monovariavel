class metodo():

    def __init__(self, fx, delta, a, b, epsilon):
        self.fx = fx
        self.delta = delta
        self.a = a
        self.b = b
        self.epsilon = epsilon

    def calcula(self):
        while(abs(self.b - self.a) > self.epsilon):
            xaux = (self.a + self.b)/2
            x = xaux - self.delta
            result1 = eval(self.fx)
            x = xaux + (self.delta)
            result2 = eval(self.fx)
            if(result1 > result2):
                self.a = xaux - (self.delta)
            else:
                self.b = xaux + (self.delta)
        if(result2 > result1):
            print('f(', xaux - self.delta, ') = ', result1)
        else:
            print('f(', x, ') = ', result2)
