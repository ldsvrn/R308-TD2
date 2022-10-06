from Personnage import Personnage

#    __  __                  
#   |  \/  | __ _  __ _  ___ 
#   | |\/| |/ _` |/ _` |/ _ \
#   | |  | | (_| | (_| |  __/
#   |_|  |_|\__,_|\__, |\___|
#                 |___/      

class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        super().__init__(pseudo, niveau)
        self.pv = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.__mana = niveau * 5
    
    def __str__(self) -> str:
        return super().__str__() + f", {self.__mana} mana (Mage)"

    def degats(self) -> int:
        if self.__mana >= 4:
            self.__mana -= 4
            return self.niveau + 3
        else:
            return self.niveau

    def soin(self) -> None:
        self.pv = self.niveau * 5 + 10
        self.__mana = self.niveau * 5
