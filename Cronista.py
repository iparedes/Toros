class Cronista:
    fh=""

    @classmethod
    def basicConfig(cls,filename):
        Cronista.fh=open(filename,"w")

    @classmethod
    def write(cls,message):
        Cronista.fh.write(message)

    @classmethod
    def pase(cls,diestro,pase):
        a="El diestro ejecuta %s %s" % (pase['articulo'],pase.key())
        Cronista.fh.write(a)


    @classmethod
    def termina(cls):
        Cronista.fh.close()


