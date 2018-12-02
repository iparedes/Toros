from lxml import etree
import tools
import Matador
import Toro
from Cronista import *


class Faena:
    def __init__(self,m,t):
        self.matador=m
        self.toro=t
        self.scoretecnico=0
        self.scoreartistico=0

        self.varas()
        self.banderillas()
        self.muerte()

    def varas(self):
        self.matador.cita()
        (pase,tecnica,arte)=self.matador.pase()

        dif=self.Pases[p]['dificultad']
        max_score=self.PasesDistr[dif]['score']

        self.scoretecnico+=(max_score*tecnica)
        self.scoreartistico+=arte
        pass

    def banderillas(self):
        pass

    def muerte(self):
        pass


class Mundo:
    def __init__(self):
        Cronista.basicConfig('Historia.log')

        self.Pases={} # Diccionario, la clave es el nombre del pase. descripcion y dificultad
        self.NomPases={} # Diccionario, la clave es la dificultad del pase, el valor una lista de nombres
        self.PasesDistr={} # Diccionario, la clave es la dificultad, da puntos para extrapolar las funciones que
                           # permiten calcular la distribución de frecuencias por dificultad


        self.loadPases()

        M=Matador.Matador(self.NomPases,self.PasesDistr)
        T=Toro.Toro()
        faena=Faena(M,T)



        Cronista.termina()
        pass


    def initDB(self):
        pass

    def loadPases(self):
        parser = etree.XMLParser(remove_blank_text=True)
        XMLconstants = etree.parse('mundo.xml', parser)

        XMLConst = XMLconstants.findall("//const")
        for i in XMLConst:
            c=i.attrib['Name']
            v=int(i.find('val').text)
            tools.Constants[c]=v

        XMLPases = XMLconstants.findall("//paseCapote")
        for i in XMLPases:
            na=i.attrib['Name']
            de=i.find('desc').text
            di=i.find('dificultad').text
            self.Pases[na]={"desc":de,"dificultad":di}
            try:
                self.NomPases[di].append(na)
            except KeyError:
                self.NomPases[di]=[]
                self.NomPases[di].append(na)


        XMLPasesDistr=XMLconstants.findall("//distrPase")
        for i in XMLPasesDistr:
            l=[]
            vals=i.findall('val')
            for v in vals:
                elem=list(map(int, v.text.split(',')))
                l.append((elem[0],elem[1]))


            def getKey(item):
                return (item[0])
            l=sorted(l,key=getKey)
            l=list(map(list,zip(*l)))
            # Comprueba si es la ultima categoria (vacia en el XML)
            if l:
                x=l[0]
                y=l[1]
            else:
                x=[-1]
                y=[-1]
            score=int(i.find('score').text)
            self.PasesDistr[i.attrib['Name']]={"indice":x,"valor":y,"score":score}


    def faena(self,M):
        pass
        # M.cita()
        # (pase,tecnica,arte)=M.pase()
        #
        # dif=self.Pases[p]['dificultad']
        # max_score=self.PasesDistr[dif]['score']
        #
        # self.scoretecnico+=(max_score*tecnica)
        # self.scoreartistico+=arte


