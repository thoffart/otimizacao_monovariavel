from Packages import Busca_Uniforme
from Packages import Busca_Dicotomica
from Packages.Fibo import Fibo

Bu = Busca_Uniforme.metodo('x**2 + 2*x', 0.5, -3, 5)
Bu.calcula()

bd = Busca_Dicotomica.metodo('x**2 + 2*x', 0.01, -3, 5, 0.1)
bd.calcula()

f = Fibo(-3, 5, 'pow(x, 2) + 2*x', 0.2)
