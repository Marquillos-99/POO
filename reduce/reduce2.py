from functools import reduce

lista = ["Python", "Java", "Ruby", "Elixir"]

resultado = reduce(lambda acumulador='',elemento='': acumulador + " - " + elemento,lista)
print (resultado)

lista2=['Mexico', 'Colombia', 'Brasil', 'Venezuela', 'Bolivia', 'Argentina', 'Uruguay', 'Peru', 'Paraguay', 'Chile','a']
