# BUCLES

# 1. Escribe el codigo para un bucle tipo for el cual imprime del numero 0 hasta el 7. 
# Utiliza la variable auxiliar llamada n.
for n in range(8):
    print(n)

# 3. Ahora modifica el bucle para que escriba en 3 segundos 99 numeros. 
# Piensa con cuidado los valores iniciales y finales del rango
for n in range(3, 100, 3):
    print(n)

# 4. Programa un bucle que haga una cuenta atras de 10 hasta 1 y por ultimo 
# escriba el mensaje !Despegue¡ 
for cuenta in range(10, 0, -1):
    print(cuenta)
print("!Despegue¡")

# 5. Mediante un bucle, escribe el codigo de la tortuga para que dibuje un cuadro 
# (eligue tu las dimesiones)
from turtle import *
# Cuadro
for n in range(4):
    forward(200)
    right(90)

    
# Circulo
# for n in range(360):
#     forward(1)
#     right(1)

# circle(100)

# Triangulo
# for n in range(3):
#     forward(200)
#     right(-120)