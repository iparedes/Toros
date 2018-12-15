from Limbo import *
import sys

class Cronista(Limbo):
    fh=""

    @classmethod
    def basicConfig(cls,filename):
        #Cronista.fh=open(filename,"w")
        Cronista.fh=sys.stdout

    @classmethod
    def write(cls,message):
        Cronista.fh.write(message)

    @classmethod
    def pase(cls,diestro,manta,pase,tecnica,arte):
        p=Limbo.Pases[manta][pase]
        a="El diestro ejecuta %s %s\n" % (p['articulo'],pase)
        Cronista.fh.write(a)

    @classmethod
    def incidente(cls,i):
        f=Limbo.Incidentes[i]
        a="El diestro ha sufrido %s %s. Es %s\n" % (f['articulo'],i,f['desc'])
        Cronista.fh.write(a)


    @classmethod
    def termina(cls):
        Cronista.fh.close()


