
# # def sumatoria(a,b):
# #     return a + b
    
# # x = sumatoria(5,9)

# # print(x)


# # def operaciones(a,b):
# #     return a + b, a-b, a*b, a/b, a**b

# # s, r, m, d, p = operaciones(2,3)

# # print(s,r,m,d,p)


# #VALOR POR DEFECTO 

# # def operaciones(a, b = 1):
# #     return a + b, a-b, a*b, a/b, a**b

# # s, r, m, d, p = operaciones(2,3)

# # print(operaciones(2, 6))




def suma(x, y = 0):
    return x+y

def resta(x, y = 0):
    return x-y

def mult(x, y = 1):
    return x*y

def division(x, y = 1):
    return x/y

# def ordenSuperior(a, b = True):
#     if b == True:
#         return suma(a), resta(a), mult(a), division(a)
#     else:
#         return suma(a,b), resta(a,b), mult(a,b), division(a,b)
    
# print(ordenSuperior(2))
# print(ordenSuperior(2, 7))

def opSuperior(funcion, val1, val2):
    return funcion(val1,  val2)

lista_funciones = [suma, resta, mult, division]
for func in lista_funciones:
    print(opSuperior(func, 5,8))