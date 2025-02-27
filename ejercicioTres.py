import math


# j = 0

# for i in range (0, 101):
#     j = j + i
#     print(j)
    
# k, i = 0, 0
        
# while i <= 100:
#     k += i
#     i += 1 
#     print(k)
    
    
    
# n = int(input("Ingrese un numero para calculo del factorial "))
# acum = 1


# for i in range(1, n+1):
#     acum = acum * i
# print(f'{n}! = {acum}')
    
    
# n = int(input("Ingrese un numero para calculo del factorial "))
# acum, i = 1, 1


# while i <= n:
#     acum *= i
#     i += 1
# print(f'{n}! = {acum}')


# n = 5
# acum = 1


# for i in range(1, 11):
#     if i == 5:
#         pass
#     print(i)
# print("asdc")


# n = int(input("Ingrese un numero "))
# print(f'10 / {n} es igual a { 10/ n }')


# MANEJO DE ERRORES O EXCEPCIONES 


# try:
#     n = int(input("Ingrese un numero "))
#     print(f'10 / {n} es igual a { 10/ n }')
# except ZeroDivisionError:
#     print("El error es dividir por cero")
# except ValueError:
#     print("EL caracter ingresado no es un mumero")
    
# EVALUEMOS LA FUNCION DE INTERPOLACION sa(x)
# sa(x) = sen(x)/x si x != 0 y 1 si x = 0



# x = list(range(-5, 6))
# sa = []

# for xx in x:
#     try:
#         sa.append(math.sin(xx)/xx)
#     except ZeroDivisionError: 
#         sa.append(1.)  
# print(sa)