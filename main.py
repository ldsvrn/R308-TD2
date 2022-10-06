#!/usr/bin/env python3
from Personnage import Personnage
from Guerrier import Guerrier
from Mage import Mage
from Joueur import Joueur
import pickle

p1 = Personnage("test", 10)
p2 = Personnage("test2", 11)

print(p1)
print(p2)

p1.attaque(p2)

print(p1)
print(p2)

p3 = Mage('mage_noir-xx', 999)

j1 = Joueur("XxxD4rK_S4suk3xxX")
j1.append_perso(p1)
j1.append_perso(p2)
j1.append_perso(p3)

print(j1)

j1.del_perso_pseudo("test2")

print(j1)
j1.append_perso(p2)

j1.del_perso_index(0)

print(j1)

print(j1.get_perso_index(0))
print(j1.get_perso_pseudo("test2"))

p4 = Guerrier('Francky Vicent', 999999)
j1.append_perso(p4)
#j1.append_perso(p1)
print(j1)

with open("joueur.bin", "wb") as file:
    pickle.dump(j1, file)

with open("joueur.bin", "rb") as file:
    jp = pickle.load(file)
    print("fichier pickle:")
    print(jp)
