"""
Escobar Rodrigo
Primer parcial laboratorio
"""
from funciones import *

lista_personajes = parse_json("data.json")

def star_wars_app(lista: list):
    
    lista_ordenada = []
    while True:
        opcion = menu_star_wars()
        match opcion:
            case 1: lista_ordenada = listar_personajes_ordenados_por_altura(lista)
            case 2: mostrar_personajes_mas_altos_por_genero(lista)
            case 3: lista_ordenada = ordenar_lista_peso(lista)
            case 4: buscar_personaje(lista)
            case 5: generar_csv_ordenado(lista_ordenada, "lista_ordenada.csv")
            case 6: print(lista_ordenada)
            case 7: break
            
star_wars_app(lista_personajes)
