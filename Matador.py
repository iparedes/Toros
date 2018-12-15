from Cronista import *
import numpy as np
import tools

class Matador:

    pasesdb={} # Diccionario. Clave es dificultad, listas de nombres de pases por dificultad
    pasesdistr={}

    def __init__(self,arte=-1,tecnica=-1):
        if arte<0:
            arte=tools.randIntNormal(1, 100)
        if tecnica<0:
            tecnica=tools.randIntNormal(1, 100)

        self.arte=arte
        self.tecnica=tecnica
        self.nombre="Braulio"

        self.pases={}
        self.frecuencias={}
        for k in self.pasesdb.keys():
            self.pases[k]=[]
            self.frecuencias[k]=[]


        # frecuencias es un diccionario con clave dificultad y valor la probabilidad de que el matador ejecute un pase
        # de esa dificultad
        frecuencias={}
        restante=''
        for k in self.pasesdistr.keys():
            indices=self.pasesdistr[k]['indice']
            valores=self.pasesdistr[k]['valor']
            if indices[0]<0: # Es la ultima distribucion (que se calcula como el restante de las demás)
                restante=k
                frecuencias[k]=0
            else:
                frecuencias[k]=np.interp(self.tecnica,indices,valores)/100
        frecuencias[restante]=1-sum(frecuencias.values())

        for j in self.pasesdb:
            for k in self.pasesdb[j]:
                l=self.pasesdb[j][k]
                vals=np.random.randint(1,100,len(l))
                nl=[x *frecuencias[k]/ sum(vals) for x in vals]

                self.pases[j].extend(l)
                self.frecuencias[j].extend(nl)

        desv=tools.Constants['TecnicaSD']
        self.distrTecnica=tools.get_truncated_normal(mean=self.tecnica, sd=desv, low=1, upp=100)
        desv=tools.Constants['ArteSD']
        self.distrArte=tools.get_truncated_normal(mean=self.arte, sd=desv, low=1, upp=100)

    def cita(self):
        #Cronista.write("%s cita al toro\n" % self.nombre)
        pass

    def pase(self,tipo='capote'):
        pase=np.random.choice(self.pases[tipo],1,p=self.frecuencias[tipo])[0]
        valtecnica=self.distrTecnica.rvs(1)/100
        valarte=self.distrArte.rvs(1)/100


        #Cronista.write("%s\n" % pase)
        return (pase,valtecnica,valarte)

