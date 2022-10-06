

class Personnage:
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__initiative = niveau

    def __str__(self) -> str:
        return f"Personnage: {self.__pseudo}, niv. {self.__niveau}, {self.__pv}pv, {self.__initiative} d'initiative"

    def __eq__(self, __o: object) -> bool:
        return self.pseudo == __o.pseudo and self.niveau == __o.niveau and type(self) == type(__o)

    def degats(self) -> int:
        return self.__niveau

    def attaque(self, opposant) -> None:
        if self.__initiative < opposant.__initiative:
            self.__pv -= opposant.degats()
            if self.__pv > 0:
                opposant.__pv -= self.__niveau
        elif self.__initiative > opposant.__initiative:
            opposant.__pv -= self.degats()
            if opposant.__pv > 0:
                self.__pv -= opposant.__niveau
        else:
            self.__pv -= opposant.degats()
            opposant.__pv -= self.degats()

    def combat(self, opposant) -> None:
        while self.__pv > 0 and opposant.__pv > 0:
            self.attaque(opposant)

    def soin(self) -> None:
        self.__pv = self.__niveau

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @pseudo.setter
    def set_pseudo(self, pseudo: str) -> None:
        if type(pseudo) == str:
            self.__pseudo = pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @property
    def pv(self) -> int:
        return self.__pv

    @pv.setter
    def pv(self, pv: int) -> None:
        if type(pv) == int:
            self.__pv = pv

    @property
    def initiative(self) -> int:
        return self.__initiative
    
    @initiative.setter
    def initiative(self, initiative: int):
        if type(initiative) == int:
            self.__initiative = initiative


