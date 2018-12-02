from tools import *


class Toro:
    def __init__(self,n=-1,s=-1):
        """
        :param n: Nobleza. Un toro noble embiste cuando se le cita y da embestidas limpias
        :param s: Stamina. Energia del animal. Decrece a lo largo de la faena
        """
        if n<0:
            n=randNormal(1,1000)
        if s<0:
            s=rand(50,100)
        self.nobleza=n
        self.stamina=s

        # Agresividad? Se puede ser noble y agresivo?
        # Diría que sí, pero cómo usar los valores durante la faena

