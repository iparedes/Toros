from tools import *


class Toro:
    def __init__(self,n=-1,b=-1,s=-1):
        """
        :param n: Nobleza. Un toro noble embiste cuando se le cita y da embestidas limpias
        :param s: Stamina. Energia del animal. Decrece a lo largo de la faena
        :param b: Bravura. Agresividad, afecta a las cogidas cuando el pase sale mal
        """
        if n<0:
            n=randIntNormal(1, 100)
        if s<0:
            s=randInt(50, 100)
        if b<0:
            n=randIntNormal(1, 100)
        self.nobleza=n
        self.stamina=s
        self.bravura=b

        # Agresividad? Se puede ser noble y agresivo?
        # Diría que sí, pero cómo usar los valores durante la faena

