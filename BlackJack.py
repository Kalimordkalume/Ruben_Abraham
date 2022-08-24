"""
#En este programa se va a realizar un programa del juego de mesa blackjack, utilizando el curso de youtube ofrecido por freecode.org.

#Se nos pide crear dos variables. Una llamada suite que tendrá el valor de "hearts"; otra llamada rank que tenga de valor "K" de "King" y
#otra llamada value que tenga de valor "10".

#suit="hearts"
#rank="K"
#value=10
#Ahora nos pide colocar una línea de código en el que printemos un mensaje utilizando las variables. "your card is:"
#print("Your card is: ")
#Añadimos una nueva línea con un print de la variable rank.
#print(rank)

#Ahora se nos pide que retoquemos el código para que quede la parte del print, en una única línea.

#print("Your card is: "+ rank)#Aquí utilizo el operador de suma, ya que con esto se me permite concatenar cadenas de texto y variables.

#Ahora se nos pide que actualizemos nuestro código para que el programa nos muestre en pantalla cual es la carta; su rango, su palo.

#print("Your card is:"+ rank + " of " + suit)


#Se nos informa que en python también se puede trabajar con listas que lleven consigo todos los datos. Se nos dice que establezcamos 
#ahora una nueva variable, que contenga todos los palos del póker en una lista.


#suites=["hearts","diamonds","clubs","spades"]
#suit="hearts"
#rank="K"
#value=10

#print("Your card is: "+suit+"of"+rank)

#ahora se nos pide, que utilizando las propiedades de las listas, en este caso del uso de los [], actualicemos la variable suit, 
# con el contenido de la vairable suites haciendo uso del índice de la lista.

#suites=["hearts","diamonds","clubs","spades"]
#suit=suites[0]
#rank="K"
#value=10

#print("Your card is: " + rank + " of " + suit)

# Ahora quiere que practiquemos un for loop.
# Nos pide que escribamos un loop con for, que printe cada uno de los palos.

#suits=["hearts","diamonds","clubs","spades"]
#suit=suits[0]
#rank="K"
#value=10

#for suit in suits:
    #print(suit)
# ---- Aunque la variable "suit" existe en la línea 48, para un bucle for, la variable suit, aún no ha sido usada
# eso es por que se trata de una variable de uso local, o en mis palabras, que no sale del bucle y solo es usada en el bucle
# para que la pudiera usar, debería rescatarla de alguna manera de la lína 48 y que esa variable ya no fuera algo local sino algo mundial (?)
#entonces comenzaría a tener problemas con el bucle, por que usaría los datos almacenados más atrás.

# Ahora se nos pide que junto antes del loop que hemos creado, intentemos añadir un nuevo item a la lista que sea el str "snakes"
# Para este ejercicio, sé que se puede usar el operador suma:
#suits=["hearts","diamonds","clubs","spades"]
#suit=suits+["snakes"]
#rank="K"
#value=10
#for suit in suit:
#    print(suit)

#Esta es una forma utilizando el operador suma. Ahora bien, sé que debe de haber un método que permite hacerlo.
#El método es append.

#suits=["hearts","diamonds","clubs","spades"]
#suits.append("snakes")
#rank="K"
#value=10
#for suit in suits:
#    print(suits)

#Esta parte del código funciona correctamente.

#Ahora vamos a empezar a implementar la representación de un deck entero de cartas.
#El codigo anterior ya no vale.
#Ahora vamos a crear una nueva lista que contenga los valores del rango.


#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#value=10
#for suit in suits:
#    print(suits)

#Ahora se nos pide que asignemos una lista vacía a una variable llamada card.
#Por otro lado, dentro de la lista de cards, debería existir un item por cada una de las 52 cartas.
#Por lo tanto, debemos actualizar el print para que imprima una lista de dos items, el primero debe ser 
# uno de los palos, con el primer item de la lista ranks. Tras eso, podemos inferir que necesitaremos que se 
# imprima cada palo con cada uno de los rangos.
#Una lista, puede contener más listas.
#Por lo tanto, se puede inducir que podemos cargar en la variable cards que es una lista vacía, y podemos utilizar el método append
#para cargar los datos de la lista dentro de otra lista.
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#
#for suit in suits:
#    for rank in ranks:
#       cards.append([suit,rank])
#print(cards)
#
#Ahora los elementos de la lista están ordenados, pero para nuestro juego, lo ideal es que estén desordenados.
#Para ello vamos a llamar a la librería random y vamos a utilizar el método shuffle para este menester
#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#
#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])
#random.shuffle(cards)
#print(cards)

#Ahora se nos pide que quitemos un elemento de la lista, utilizando el método pop el 
#cual es un método que está dentro de las listas de python.

#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])
#random.shuffle(cards)
#card=cards.pop()
#print(card)

#Con todo esto el siguiente paso es crear una función llamada shuffle,
#  que se encargue de desordenar las cartas cuando se ejecute.
#Además, reordenamos el código para que se printe lo mismo con la función llamada.
#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#
#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])
#
#def shuffle():
#    random.shuffle(cards)
#
#shuffle()
#print(cards.pop())

#Ahora vamos a crear una nueva función, que hará las funciones de dealer.
#Esta se llamará deal y se encargará de entregarnos una carta.

#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#
#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])
#
#def shuffle():
#    random.shuffle(cards)
#
#def deal():
#    card=cards.pop()
#    return card
#shuffle()
#print(cards.pop())

#Ahora, llamaremos a la función deal, y printaremos una única carta.
#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])
#
#def shuffle():
#    random.shuffle(cards)

#def deal():
#    card=cards.pop()
#    return card
#shuffle()
#card=deal()
#print(card)
#Qué pasaría si ahora queremos que la función deal, nos entregue más de una carta? Refactoricemos la función deal
#para que ahora acepte un argumento.
#Tras esto, hagamos que el parámetro que hemos creado en la función sea usado por ella, haciendo que en vez de entregar una carta, entregue una lista.
#Para ello vamos a colocar una nueva lista vacía.
#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])

#def shuffle():
#    random.shuffle(cards)

#def deal(number):
#    cards_dealt=[]
#    
#    return cards_dealt
#shuffle()
#cards_dealt=deal(2)
#print(cards_dealt)

#Ahora necesitamos crear un loop que almacene los datos necesarios utilizando el método range. Este método, nos da una lista de números que empieza en el 0.

#import random
#cards=[]
#suits=["hearts","diamonds","clubs","spades"]
#ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#
#for suit in suits:
#    for rank in ranks:
#        cards.append([suit,rank])
#
#def shuffle():
#    random.shuffle(cards)
#
#def deal(number):
#    cards_dealt=[]
#    for x in range(number):
#        card=cards.pop()
#        cards_dealt.append(card)
#    return cards_dealt
#shuffle()
#cards_dealt=deal(2)
#print(cards_dealt)

#Ahora se nos pide que separemos abajo del todo la primera carte de las que se han dado y la coloquemos en una nueva variable card.
import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt=deal(2)
card=cards_dealt[0]
print(card)

#Ahora vamos a separar el rango de una carta. Creemos una variable nueva llamada rank y asignémosles el valor del rango de esa carta.

import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt=deal(2)
card=cards_dealt[0]
rank=card[1]
print(card)

#Ahora necesitamos checkear cual es el valor del rango de esa carta y colocarle el valor correcto según las normas del BJ.
#Para ellos usaremos algunos condicionales y tras esto imprimiremos por pantalla el rango y el valor de la carta.
import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt=deal(2)
card=cards_dealt[0]
rank=card[1]
if rank=="A":
    value=11
elif rank=="J" or rank=="Q" or rank=="K":
    value=10
else:
    value=rank
print(rank,value)



#Ahora vamos a introducir los diccionarios. Se trata de un conjunto de datos que nos permite categorizar una serie de items con una palabra clave en ellos.
#Creemos un dictonario para los rangos de las cartas.
import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt=deal(2)
card=cards_dealt[0]
rank=card[1]
if rank=="A":
    value=11
elif rank=="J" or rank=="Q" or rank=="K":
    value=10
else:
    value=rank

rank_dict={"rank": rank, "value":value}
print(rank,value)

#Ahora se nos pide que actualicemos nuestro código para que printe utilizando los valores del diccionario.

import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
cards_dealt=deal(2)
card=cards_dealt[0]
rank=card[1]
if rank=="A":
    value=11
elif rank=="J" or rank=="Q" or rank=="K":
    value=10
else:
    value=rank

rank_dict={"rank": rank, "value":value}
print(rank_dict["rank"],rank_dict["value"])
"""
#Ahora se nos pide que refactoricemos el código para que tengamos el valor de cada uno de los rangos sin necesidad de utilizar una línea condicional de tipo if.
#Para ello, guardaremos los valores en la lista de ranks usando dicts. Por ello necesitaremos borrar gran parte del código.
#Ahora vamos a asignar una nueva variable card desde la función deal, de tal manera que nos aseguremos de que esa variable no es una lista.
#Ahra acualitzaremos ranks, para que sea una lista de diccionarios con cada uno de los rangos y el valor que tienen.
#Ahora la variable ranks, contiene una lista, en la que cada item es un diccionario.
"""
import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=[
    {"rank":"A","value":11},
    {"rank":"2","value":2},
    {"rank":"3","value":3},
    {"rank":"4","value":4},
    {"rank":"5","value":5},
    {"rank":"6","value":6},
    {"rank":"7","value":7},
    {"rank":"8","value":8},
    {"rank":"9","value":9},
    {"rank":"10","value":10},
    {"rank":"J","value":10},
    {"rank":"Q","value":10},
    {"rank":"K","value":10}
]

for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
card=deal(1)[0]
"""
#Ahora se nos pide que printemos una carta.
#Cuando lo hagamos, se nos pide que en vez de que printe una carta printe el valor de la carta.
import random
cards=[]
suits=["hearts","diamonds","clubs","spades"]
ranks=[
    {"rank":"A","value":11},
    {"rank":"2","value":2},
    {"rank":"3","value":3},
    {"rank":"4","value":4},
    {"rank":"5","value":5},
    {"rank":"6","value":6},
    {"rank":"7","value":7},
    {"rank":"8","value":8},
    {"rank":"9","value":9},
    {"rank":"10","value":10},
    {"rank":"J","value":10},
    {"rank":"Q","value":10},
    {"rank":"K","value":10}
]
#El siguiente loop, pasa cada uno de los items que hay en la variable suits, con cada uno de los items que hay en la lista ranks.
#El primer item de suits y de ranks será almacenado en forma de lista y luego inyectado con el comando append al final de la lista vacía cards. Así hasta que termine el loop.
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])
#En este punto, la lista cards contiene 52 listas cada una con 2 elementos que corresponden al palo de la carta y su rango.
def shuffle():
    random.shuffle(cards)

#Esta función se encargará de repartir tantas cartas como se le pida en su parámetro.
def deal(number):
    cards_dealt=[]
    for x in range(number):
        card=cards.pop()
        cards_dealt.append(card)
    return cards_dealt
shuffle()
card=deal(1)[0]
print("Su carta es: "+ card[1]["rank"]+ " de " + card[0])

lista=["pene","vagina"]
superlista=[lista]
print("Lo que contiene la variable lista es: "+ str(lista) + " el número de items que hay es: " + str(len(lista)) + " y el tipo de dato que es la variables es: " + str(type(lista)))
print("Lo que contiene la variable superlista es: "+ str(superlista) + " el número de items que hay es: " + str(len(superlista)) + " y el tipo de dato que es la variables es: " + str(type(superlista)))