milista = ["maria", "pepe", "marta", "Antonio"]

# funciones


def mensaje():
    print(milista[2])
    print(milista[:5])
    milista.append("Carlos")
    print(milista[:5])
    print(milista.index("pepe"))
    print("pepe" in milista)  # contains
    milista.extend(["jaimito", "lucia"])
    milista.pop()
    print(milista)


mensaje()

# funciones2


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(12))

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
midiccionario = {mitupla[0]: "Madrid", mitupla[1]                 : "Paris", mitupla[2]: "Londres", mitupla[3]: "Berlin"}
print(midiccionario["Francia"])

midiccionario2 = {23: "Jordan", "Nombre": "Michael",
                  "Equipo": "Chicago", "Anillos": [1991, 1992, 1993, 1996]}
print(midiccionario2["Anillos"])

milista = midiccionario2.keys()
print(milista)
