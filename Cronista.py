from Limbo import *

class Cronista(Limbo):
    fh=""

    @classmethod
    def basicConfig(cls,filename):
        Cronista.fh=open(filename,"w")

    @classmethod
    def write(cls,message):
        Cronista.fh.write(message)

    @classmethod
    def pase(cls,diestro,manta,pase,tecnica,arte):
        p=Limbo.Pases[manta][pase]
        a="El diestro ejecuta %s %s" % (p['articulo'],pase)
        Cronista.fh.write(a)


    @classmethod
    def termina(cls):
        Cronista.fh.close()


