class Cronista:
    fh=""

    @classmethod
    def basicConfig(cls,filename):
        Cronista.fh=open(filename,"w")

    @classmethod
    def write(cls,message):
        Cronista.fh.write(message)

    @classmethod
    def termina(cls):
        Cronista.fh.close()


