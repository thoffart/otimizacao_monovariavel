
# coding: utf-8

# In[84]:


import numpy as np
import parser

def fx(x):
    code = parser.expr(formula).compile()
    return eval(code)

def iteracao(a,b,p,q):
    fp = fx(p)
    fq = fx(q)
    
    if(fp>fq):
        return [p,b]
    else:
        return [a,q]
    
def aurea(a, b):
    p = a + (1-0.618)*(b - a)
    q = a + 0.618*(b - a)
    
    fp = fx(p) 
    fq = fx(q)
    
    parada = b - a
    
    print("a: {0}\nb: {1}\np: {2}\nf(p): {3}\nq: {4}\nf(q): {5}\nb - a: {6}".format(a,b,p,fp,q,fq,parada))
    
    [a,b] = iteracao(a,b,p,q)
    
    return [a,b,parada]
    


# In[105]:


a = input("Intervalo: [a,b].\na: ")
b = input("b: ")
delta = input("Critério de parada Delta: ")
formula = input("f(x): ")


# In[106]:


a = float(a)
b = float(b)
parada = 1000
delta = float(delta)
i=1

while(parada>delta):
    print("Iteracao {0}".format(i))
    i+=1
    [a,b,parada] = aurea(a,b)
    print("\n")
    
print("x* = {0}".format((a+b)/2))


# In[88]:


parada

