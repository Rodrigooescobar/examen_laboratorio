"""Primer Parcial Laboratorio de Computación I
1. Listar los personajes ordenados por altura. Preguntar al usuario si lo quiere 
ordenar de manera ascendente ('asc') o descendente ('desc')
2. Mostrar el personaje más alto de cada genero
3. Ordenar y listar los personajes por peso. Preguntar al usuario si lo quiere 
ordenar de manera ascendente ('asc') o descendente ('desc')
4. Armar un buscador de personajes
5. Exportar a CSV la lista de personajes ordenada según opción elegida 
anteriormente [1]
6. Salir
Aclaraciones:
● Los puntos deben ser accedidos mediante un menú. Para todas las opciones, 
validar lo ingresado por consola con RegEx
● El set de datos proviene de un json
● Realizar las validaciones que crea pertinentes
● En todos los casos se deberá trabajar con una copia de la lista origina
Escobar Rodrigo
Primer parcial laboratorio
"""
import json
import re

def parse_json(nombre_archivo: str)->list:
    """
    Parea un archivo json a la memoria del programa en un diccionario
    """
    with open(nombre_archivo, "r") as archivo:
        personajes_json = json.load(archivo)  #parsea a dict
    return personajes_json["results"]

def starwars_normalizar_datos(lista: list):
    if type(lista) == type(list()) and len(lista) > 0:
        for e_lista in lista:
            if type(e_lista["height"]) != type(int(e_lista["height"])):
                e_lista["height"] = int(e_lista["height"])
            if type(e_lista["mass"]) != type(int(e_lista["mass"])):
                e_lista["mass"] = int(e_lista["mass"])

def copiar_lista(lista:list):
    """
    Recibe una lista y la retorna duplicada por el metodo shalow copy
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista_duplicada = lista[:]
        starwars_normalizar_datos(lista_duplicada)
        return lista_duplicada

def listar_personajes_ordenados_por_altura(lista: list):
    """
    Recibe una lista y pregunta al usuario como ordenaela, de maneda ascendente o desendente
    se valida el string que ingresa el dato e imprime el orden seleccionado
    Pregunta al usuario si quiere exprotar el orden de la lista a un arhivo CSV
    """
    if type(lista) == type(list()) and len(lista) > 0:
        lista_personajes_duplicada = copiar_lista(lista)
        lista_ordenada_altura = ordenar_lista(lista_personajes_duplicada, "height")
        mostrar_nombre_clave_interadno(lista_ordenada_altura, "height")
        imprimir = input("Desea parsear a CSV lista ordenada? [si/no] ")
        imprimir = validar_string(imprimir)
        if imprimir == "si":
            generar_csv(lista_ordenada_altura, "lista_ordenada.csv")
        return lista_ordenada_altura

def calcular_max_clave(lista: list, clave: str, genero:str):
    """
    Calcula y retorna el valor maximo de cualquier clave
    Se pasa por parametros la lista, clave y el genero
    """
    if type(lista) == type(list()) and len(lista) > 0 and type(clave) == type(str()) and type(genero) == str:
        maxmin = None
        for e_lista in lista:
            if (genero == e_lista["gender"]) and (maxmin is None or e_lista[clave] > maxmin[clave]):
                maxmin = e_lista
        retorno = maxmin
    return retorno

def mostrar_nombre_y_clave(diccionario:dict, clave:str):
    """Muestra el nombre, una clave y su valor de un diccionario"""
    print("Nombre: {0[name]} | {1} {2}".format(
        diccionario, clave, diccionario[clave]))
    
def mostrar_nombre(diccionario:dict):
    """muestra el nombre de un diccionario"""
    print("Nombre: {0[name]}".format(diccionario))

def mostrar_nombre_clave_interadno(lista:list, clave:str):
    """Muestra el nombre, una clave y su valor iterando una lista"""
    for e_lista in lista:
        print("Nomber: {0[name]} | {1}: {2} ".format(e_lista, clave, e_lista[clave]))

def mostrar_nombre_y_2claves(dic:dict, clave1:str, clave2:str):
    """Muestra el nombre, dos clave y el valor de una sola de un diccionario"""
    print ("Nomber: {0[name]} | {1} {2} | {3}".format(dic, clave1, dic[clave1], dic[clave2]))  

def mostrar_personajes_mas_altos_por_genero (lista:list):
    """Muestra el nombre, la altura con su valor y el genero"""
    if type(lista) == list and len(lista) > 0:
        lista_personajes_duplicada = copiar_lista(lista)
        mas_alto_masculino = calcular_max_clave(lista_personajes_duplicada, "height", "male")
        mas_alto_femenino = calcular_max_clave(lista_personajes_duplicada, "height", "female")
        mas_alto_n_a = calcular_max_clave(lista_personajes_duplicada, "height", "n/a")
        mostrar_nombre_y_2claves(mas_alto_masculino, "height", "gender")
        mostrar_nombre_y_2claves(mas_alto_femenino, "height", "gender")
        mostrar_nombre_y_2claves(mas_alto_n_a, "height", "gender")

def ordenar_lista (lista:list, clave:str):
    """
    Ordena una lista preguntando al usuario de manera asendente o descedente
    retorna la lista ordenada segun la opcion elegida
    """
    if type(lista) == list and len(lista) > 0 and type(clave) == str:
        bandera_swap = True
        orden = input(
            "Ingrese la forma de ordear [asc/desc] o por cualquier tecla volver al menu: ")
        orden=validar_string(orden)
        if orden == "asc" or orden == "desc":
            while bandera_swap == True:
                bandera_swap = False
                for i in range(len(lista)-1):
                    if (orden == "asc" and lista[i][clave] > lista[i+1][clave]) or (
                        orden == "desc" and lista[i][clave] < lista[i+1][clave]):
                        auxiliar = lista[i]
                        lista[i] = lista[i+1]
                        lista[i+1] = auxiliar
                        bandera_swap = True
            retorno = lista
        else: 
            retorno = lista
            print ("Lista sin orndear")
        return retorno

def ordenar_lista_peso (lista:list):
    """Ordena una lista segun el peso, de manera ascendente o descendente"""
    if type(lista) == list and len(lista) > 0:
        lista_personajes_duplicada = copiar_lista(lista)
        lista_ordenada_por_peso = ordenar_lista(lista_personajes_duplicada, "mass")
        mostrar_nombre_clave_interadno(lista_ordenada_por_peso, "mass")
        imprimir = input("Desea parsear a CSV lista ordenada? [si/no] ")
        imprimir = validar_string(imprimir)
        if imprimir == "si":
            generar_csv(lista_ordenada_por_peso, "lista_ordenada.csv")
        return lista_ordenada_por_peso


def buscar_personaje(lista: list):         
    if type(lista) == list and len(lista) > 0:
        personajes_encontrados = []
        while True:
            nombre = input("Ingrese el nombre del personaje a buscar: ")
            nombre = validar_number_string(nombre)
            for e_lista in lista:
                if nombre in e_lista["name"].lower():
                    personajes_encontrados.append(e_lista)
            if len(personajes_encontrados) > 0:
                for personaje in personajes_encontrados:
                    mostrar_nombre(personaje)
                return personajes_encontrados
            print("Personaje no encontrado, ingrese otro nombre: ")
    
def imprimir_menu():
    print("\n1-Listar personaes ordenado por altura\n"
        "2-Personajes mas altos de cada genero\n"
        "3-Ordenar la lista de personajes por peso\n"
        "4-Buscador de perosnajes\n"
        "5-Generar CSV\n"
        "6-Uiltima lista ordenada\n"
        "7-Salir\n")

def validar_number_string(value: str):
    patron = r"[a-zA-Z0-9]+"
    if re.search(patron, value):
        value = value.lower()
        return value

def validar_string(string:str):
    patron = "[a-zA-Z]+"
    if re.search(patron, string) != None:
        string = string.lower()
        retorno = string
    else: retorno = None
    return retorno

def validar_numero(numero):
    patron = "^[0-9]+$"
    if re.search(patron,numero) != None:
        numero = int(numero)
        retorno = numero
    else: retorno = -1
    return retorno

# def validar_numero(numero):
#     while not numero.isdigit():  # Mientras la cadena no contenga solo dígitos
#         print("Por favor, ingresa un número válido.")
#         numero = input("Introduce un número: ")

#     return int(numero)

def menu_star_wars():
    while True:
        imprimir_menu()
        menu = input("Ingrese una opcion: ")
        menu = validar_numero(menu)
        return menu
    
def generar_csv(lista, nombre_archivo):
    if type(lista) == list and len(lista) > 0 and type(nombre_archivo) == str:
        with open(nombre_archivo, "w") as archivo:
            for personajes in lista:
                mensaje = "{0},{1},{2},{3}\n".format(
                personajes["name"],
                personajes["height"],
                personajes["mass"],
                personajes["gender"],
                )
                archivo.write(mensaje)
        print("Archivo generado con exito")

def generar_csv_ordenado (lista, nombre_archivo):
    if type(lista) == list and len(lista) > 0 and type(nombre_archivo) == str:
        generar_csv(lista, nombre_archivo)
        return lista
    else: 
        print("Primero debe ordenar la lista")
    