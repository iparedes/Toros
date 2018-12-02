from Cronista import *
import numpy as np
import tools

class Matador:

    def __init__(self,pases,pasesdistr,arte=-1,tecnica=-1):
        if arte<0:
            arte=tools.randNormal(1,100)
        if tecnica<0:
            tecnica=tools.randNormal(1,100)

        self.arte=arte
        self.tecnica=tecnica
        self.nombre="Braulio"

        self.pases=[]
        self.frecuencias=[]

        frecuencias={}
        restante=''
        for k in pasesdistr.keys():
            indices=pasesdistr[k]['indice']
            valores=pasesdistr[k]['valor']
            if indices[0]<0: # Es la ultima distribucion (que se calcula como el restante de las demás)
                restante=k
                frecuencias[k]=0
            else:
                frecuencias[k]=np.interp(self.tecnica,indices,valores)/100
        frecuencias[restante]=1-sum(frecuencias.values())

        for k in pases:
            l=pases[k]
            vals=np.random.randint(1,100,len(l))
            nl=[x *frecuencias[k]/ sum(vals) for x in vals]

            self.pases.extend(l)
            self.frecuencias.extend(nl)
            pass

        desv=tools.Constants['TecnicaSD']
        self.distrTecnica=tools.get_truncated_normal(mean=self.tecnica, sd=desv, low=1, upp=100)
        desv=tools.Constants['ArteSD']
        self.distrArte=tools.get_truncated_normal(mean=self.arte, sd=desv, low=1, upp=100)

    def cita(self):
        Cronista.write("%s cita al toro\n" % self.nombre)
        pass

    def pase(self):
        pase=np.random.choice(self.pases,1,p=self.frecuencias)[0]
        valtecnica=self.distrTecnica.rvs(1)
        valarte=self.distrArte.rvs(1)
        Cronista.write("%s\n" % pase)
        return (pase,valtecnica,valarte)

