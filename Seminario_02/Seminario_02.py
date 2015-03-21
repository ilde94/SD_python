'''
Grupo 1
David Blanco Fuentes
Ildefonso de la Cruz romero

Vamos a desarrollar el programa de Python que nos permita, a partir de una lista de

palabras, encontrar la lista mas larga posible de palabras de manera que la ultima letra de

una palabra coincida con la primera de la siguiente palabra. Para probar el programa la lista

de palabras con las que vamos a trabajar son la que encontramos en el fichero pokemon.txt

'''

#Abrimos el fichero y lo convertimos en una lista de palabras:
Pokemon = open('Pokemon.txt', 'r')
Lista_Pokemon = Pokemon.read().split()

#Creamos una lista vacia para mantener la cuenta de las palabras utilizadas y la cadena en ese momento
Lista_Recorrido = []
#Lista vacia que contendra
Lista_Final = []

#Se define una funcion para buscar una palabra dentro de la Lista_recorrido
def buscar(palabra,Lista):
	return (palabra in Lista)

#Recorremos la lista_pokemon que contendra el contenido del fichero
for Palabra_Pokemon in Lista_Pokemon:
	#Usamos la ultima letra de la siguiente palabra que se encuentre en la lista_pokemon
    letra = Palabra_Pokemon[-1]
    #Vamos anadiendo a lista_recorrido las palabras que vamos recorriendo
    #esta lista estara vacia al comenzar el bucle y contendra las cadenas que se vayan formando.
    Lista_Recorrido.append(Palabra_Pokemon)
    #Volvemos a recorrer el contenido del fichero en busca de las palabras;
    #que comience por la ultima letra de la palabra actual y no se encuentre ya en la lista_recorrido
    for Palabra_actual in Lista_Pokemon:
        if letra == Palabra_actual[0] and buscar(Palabra_actual,Lista_Recorrido) == False:
            Lista_Recorrido.append(Palabra_actual)
            #Le asignamos a letra el nuevo valor correspondiente a la ultima letra de la palabra anadida a lista_recorrido
            letra = Palabra_actual[-1]
    #Comprobamos que la lista_recorrido es la mayor lista encadenada
    if len(Lista_Recorrido) > len(Lista_Final):
        Lista_Final = Lista_Recorrido
    #vaciamos la lista_recorrido para volver a realizar el problema
    Lista_Recorrido = []
print Lista_Final


