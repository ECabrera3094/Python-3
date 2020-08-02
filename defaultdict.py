from collections import defaultdict

default_demo = defaultdict(list)

print("Default_Demo: ", default_demo[3])

for i in range(10):
    default_demo[i] = i + 10

default_demo['Emiliano'] = 'Buzz' # Se Agrega un Valor DIFERENTE.

print("Default_Demo: ", default_demo)

# -----------------------------------------------------------

ice_cream = defaultdict(lambda: 'Vanilla') # Asignamos un Valor por DEFAULT en el Diccionario.

ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'

print("Ice Cream: ", ice_cream) # Llama al Valor por DEFAULT.
print("Ice Cream: ", ice_cream['Emiliano'])

# -----------------------------------------------------------

food_list = 'spam spam spam spam spam spam eggs spam'.split()

food_count = defaultdict(int) # El Valor por Default es 0. 
                              # Por lo que no Requiere el Ingreso de la Primer Key.

for food in food_list:
    food_count[food] += 1

print("Food Count: ", food_count)

# -----------------------------------------------------------

ss = [('NC', 'Raleigh'), ('VA', 'Richmond'), ('WA', 'Seattle'), ('NC', 'Asheville')] # Lista de Tuplas.

cities = defaultdict(list)

for key, city in ss:
    cities[key].append(city)

print("Cities: ", cities)

mi_lista = ['Ibias', 'Pesoz', 'Tineo', 'Boal']
for c, valor in enumerate(mi_lista, 1):
    print(c, valor)








# hp pavilion 14 notebook tc

# https://es.wikipedia.org/wiki/Sunohara-sou_no_Kanrinin-san
# https://es.wikipedia.org/wiki/Tsurezure_Children
# https://es.wikipedia.org/wiki/Kanojo,_Okarishimasu
# https://es.wikipedia.org/wiki/Ore_wo_Suki_Nano_wa_Omae_Dake_ka_yo