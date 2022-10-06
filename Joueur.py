from Personnage import Personnage
from Guerrier import Guerrier
from Mage import Mage

#        _                             
#       | | ___  _   _  ___ _   _ _ __ 
#    _  | |/ _ \| | | |/ _ \ | | | '__|
#   | |_| | (_) | |_| |  __/ |_| | |   
#    \___/ \___/ \__,_|\___|\__,_|_|   
                                 

class Joueur:
    def __init__(self, nom, persos: list = [], nb_persos_max: int = 3) -> None:
        self.__nom = nom
        self.__persos = persos
        self.__nb_perso_max = nb_persos_max

    def __str__(self) -> str:
        return f"Joueur: {self.__nom}, perso: {[i.__str__() for i in self.__persos]}, {self.__nb_perso_max} personnages max"

    def append_perso(self, perso):
        if len(self.__persos) < self.__nb_perso_max:
            self.__persos.append(perso)
        else:
            raise Exception("Nombre max de personnages atteint")

    def get_perso_index(self, index: int):
        if len(self.__persos) >= index:
            return self.__persos[index]
        else:
            raise Exception("Le personnage n'existe pas!")

    def get_perso_pseudo(self, pseudo):
        for perso in self.__persos:
            if perso.pseudo == pseudo:
                return perso
        return None

    def del_perso_index(self, index: int) -> None:
        if len(self.__persos) >= index:
            self.__persos.pop(index)
        else:
            raise Exception("Le personnage n'existe pas!")

    def del_perso_pseudo(self, pseudo) -> None:
        for index, perso in enumerate(self.__persos):
            if perso.pseudo == pseudo:
                self.__persos.pop(index)

    def del_perso(self, perso) -> None:
        if perso in self.__persos:
            self.__persos.remove(perso)
        else:
            raise Exception(f"Le perso n'appartient pas au joueur {self.__nom}")

    # Faire un test avec __eq__ ?
    def has_perso(self, perso) -> bool:
        return perso in self.__persos

    @property
    def persos(self):
        return self.__persos