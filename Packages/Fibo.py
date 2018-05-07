class Fibo:

    def calcfibo(self, fib, n):
      fib.append(1)
      fib.append(1)
      for i in range(2, n, 1):
        fib.append(fib[i-1]+fib[i-2])

    
    def __init__(self, a, b, func, ep):
      fib = []
      h = (b-a)/ep
      p = 0
      q = 0
      fp = 0
      fq = 0
      n = 3
      k = 1
      self.calcfibo(fib, n)
      while (fib[len(fib)-1] <= h):
        fib = []
        self.calcfibo(fib, n)
        n += 1
      while(b-a >= ep):
        p = (float(fib[len(fib)-1-k-2])/float(fib[len(fib)-1-k]))*(b-a) + a
        q = (float(fib[len(fib)-1-k-1])/float(fib[len(fib)-1-k]))*(b-a) + a
        x = p
        fp = eval(func)
        x = q
        fq = eval(func)
        if (fq > fp ):
          b = q
        elif (fq < fp):
          a = p
      print(a)
      print(b)
      