import re

milista = ["maria", "pepe", "marta", "ntonio"]



# tupla
mitupla = ("juan", 13, 1, 1995)
nombre, dia, mes, año = mitupla  # para poder asignar los valores de una tupla
print(nombre)


# diccionario
midiccionario = {"alemania": "Berlin", "francia": "paris",
                 "ReinoUnido": "Londres", "España": "Madrid"}

midiccionario["Italia"] = "Lisboa"


print(midiccionario)
midiccionario["Italia"] = "Roma"  # para sobreescribir el valor de una clave
del midiccionario["ReinoUnido"]  # para eliminar un elemento
print(midiccionario)

mitupla = ("España", "Francia", "Reino Unido", "Alemania")
midiccionario = {mitupla[0]: "Madrid", mitupla[1]: "Paris", mitupla[2]: "Londres", mitupla[3]: "Berlin"}
print(midiccionario["Francia"])

midiccionario2 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "Anillos": [1991, 1992, 1993, 1996]}
print(midiccionario2["Anillos"])

milista = midiccionario2.keys()
print(milista)


# condicionales
nota = 6
if nota > 5 and nota < 7:
    print("aprobado notable")
else:
    print("suspenso")


# inputs
# cualquier input en python es de tipo String
# para que se transforme el input a tipo entero utilizamos el casting de int()


# bucles
for i in range(10):
    print(i)


# generadores
def generador(limite):
    num = 1
    while num <= limite:
        yield num * 2  # retorna el valor de num * 2 y lo añade a una estructura iterable
        num = num + 1


respuesta = generador(10)
# devuelve el primer valor de la estructura iterable y lo deja en suspensión para la siguiente vez que utilicemos next(), así podríamos ir sacando valores de una lista infinita.
print(next(respuesta))


def ciudades(*ciudades):  # * para indicar que no sabemos cuantos argumentos vamos a recibir
    for elemento in ciudades:
        # for subElem in elemento:
        # para ir iterando por cada elemento y dentro de cada elemento ir iterando en sus letras.
        yield from elemento


ciudades_devueltas = ciudades("Madrid", "Barcelona", "Bilbao")
print(next(ciudades_devueltas))


def reverseBits(x):
    num = str(x)
    num = num[::-1]
    print(num)
    num = int(num, 2)
    print(num)
    # num = int(num, 2)
    # return num


print(reverseBits(10100101000001111010011100))

# pattern recognition
messsage = "hola mi numero es 666-097-120"
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
print(phoneNumRegex.findall(messsage))

# the same with other function
mi = phoneNumRegex.search(messsage)
print(mi.group())


# separate elements within the ocurrences of a pattern
# to search a parentesis intentionally, use \ before the parentesis
phoneNumRegex = re.compile(r'(\d\d\d)-\d\d\d-\d\d\d')
mi = phoneNumRegex.search(messsage)
print(mi.group(1))


# pipes in the pattern
message = "la Autocaravana está averiada"
autoRegex = re.compile(r'Auto(movil|carro|caravana)')
mi = autoRegex.search(message)
print(mi.group())
