from Personnage import Personnage

#     ____                      _           
#    / ___|_   _  ___ _ __ _ __(_) ___ _ __ 
#   | |  _| | | |/ _ \ '__| '__| |/ _ \ '__|
#   | |_| | |_| |  __/ |  | |  | |  __/ |   
#    \____|\__,_|\___|_|  |_|  |_|\___|_|   



class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        super().__init__(pseudo, niveau)
        self.pv = niveau * 8 + 4
        self.initiative = niveau * 4 + 6

    def __str__(self) -> str:
        return super().__str__() + " (Guerrier)"

    def degats(self) -> int:
        return self.niveau * 2

    def soin(self) -> None:
        self.pv = self.niveau * 8 + 4
