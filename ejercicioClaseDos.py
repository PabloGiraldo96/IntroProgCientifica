
cadena = "hola mundo"

print(type(cadena))
# print(cadena[3])
print (cadena[5:-4])

lista = [1, 3,14, True, [1,2,3], 2+1j]

listaDos = lista

listaDos[-1] = False

listaTres = lista.copy()
listaS= lista[:]
listaZ = list(lista)

# print(f'los valores de la lista original son: \n{lista}')
# print(f'los valores de la lista con copy: \n{listaTres}')
# print(f'los valores de la lista con slicing son: \n{listaS}')
# print(f'los valores de la lista con metodo list son: \n{listaZ}')
# print (listaDos)
# print (lista)
# print (listaTres)

personas = {"nombre": ['Ana', 'Juan', 'Jose'], 
            "Apellido": ['Perez', 'Rodriguez', 'Leon']}

personas["Sexo"] = ['M', 'H', 'H']

personas['Apellidos'] = personas.pop("Apellido")

personas['Genero'] = personas.pop("Sexo")

# print(personas)
print(personas)



## CONTROLES DE FLUJO ### 

n = float(input("Ingrese un numero: "))
          
if n >= 5:
    print(f'{n} "Es mayor que 5"')
print(" N es mayor que 5")


n = float(input("Ingrese un numero: "))
          
if n >= 5:
    print(f'{n} "\u2265 5"')
    
else:
    print(f'{n} "< 5"')

temperatura = float(input("Ingrese la temperatura del paciente: "))

if temperatura >= 41:
    print(f'{temperatura} "Tiene fiebre muy alta')
    
elif temperatura < 41 and temperatura >= 39.5:
     print(f'{temperatura} "Tiene fiebre alta')
    
elif temperatura < 39.5 and temperatura >= 37.5:
     print(f'{temperatura} "Tiene fiebre')

elif temperatura <= 37.5 and temperatura >= 36:
     print(f'{temperatura} "Tiene temperatura normal')
     
else:
     print(f'{temperatura} "Tiene hipotermia')
     
     
## BUCLES ### 

for i in range(1,11):
    print(i)

i = 0

while i < 10:
    i += 1
    print(i) 
    
    
    
diccionario = {'America': ["Colombia", "Peru", "Argentina"], 
               'Europa': ["UK", "Alemania", "Italia"],
               'Asia': ["China", "Japon", "India"], 
               'Africa': ["Egipto", "Libia", "Sudan"]
               }


diccionario['Oceania'] = ["Australia", "New Zealand", "Papua Nueva Guinea"]



continentes = list(diccionario.keys())


print(continentes)


for continente in continentes:
    print(f'Algunos paises de {continente} son: ')
    for pais in diccionario[continente]:
        print(f'    {pais}')
    
    
numContinentes = len(continentes)

cont = 0
while cont < numContinentes:
    print(f'Algunos paises de {continentes[cont]} son: ')
    contPais = 0
    while contPais < len(diccionario[continentes[cont]]):
        print(diccionario[continentes[cont]][contPais])
        contPais += 1
    cont +=  1
