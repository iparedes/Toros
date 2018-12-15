from lxml import etree
import tools
from Limbo import *
import Matador
import Toro
from Cronista import *




class Faena(Limbo):

    a_freqinc=0 # ax+b es la funcion para la frecuencia de incidentes.
    b_freqinc=0 # Técnica maxima da minima frecuencia

    def __init__(self,m,t):
        self.matador=m
        self.toro=t
        self.scoretecnico=0
        self.scoreartistico=0
        #self.pases=pases

        self.varas()
        self.banderillas()
        self.muerte()

    def varas(self):
        # BUCLE PARA PROBAR VALORES
        for i in range(0,100):
            self.matador.cita()
            (pase,tecnica,arte)=self.matador.pase('capote')
            Cronista.pase(self.matador,'capote',pase,tecnica,arte)
            try:
                (oops,v)=self.incidente(tecnica)
            except Exception as e:
                pass
            if oops:
                # todo: procesa incidente
                Cronista.incidente(v)
            max_score=Limbo.Pases['capote'][pase]['maxscore']
            self.scoretecnico+=(max_score*tecnica)
            self.scoreartistico+=arte

    def banderillas(self):
        pass

    def muerte(self):
        pass

    def incidente(self,tecnica):
        threshold=(self.a_freqinc*tecnica)+self.b_freqinc
        # para que suceda el incidente, el valor tiene que ser menor que el threshold
        dice=tools.rand(0,100)
        if dice<threshold:
            # incidente
            # DETERMINAR EL INCIDENTE
            # esta busqueda tan bizarra podria dar varios hits
            for x,i in enumerate(Limbo.Incidentes.values()):
                if dice>=i['min'] and dice<=i['max']:
                    return (True,list(Limbo.Incidentes.keys())[x])
            #a=[x for x,i in enumerate(self.incidentes.values()) if dice>=i['min'] and dice<=i['max']]
        else:
            return (False,-1)



class Mundo(Limbo):
    def __init__(self):
        Cronista.basicConfig('Historia.log')

        #self.Pases={} # Diccionario, la clave es el tipo (capote,muleta), cada uno tiene un diccionario con
        # clave nombre del pase. descripcion y dificultad
        self.NomPases={} # Diccionario, la clave es la dificultad del pase, el valor una lista de nombres
        self.PasesDistr={} # Diccionario, la clave es la dificultad, da puntos para extrapolar las funciones que
        # permiten calcular la distribución de frecuencias por dificultad

        self.NomPases['capote']={}
        self.NomPases['muleta']={}

        self.loadMundo()
        #Faena.pases=self.Pases
        Matador.Matador.pasesdb=self.NomPases
        Matador.Matador.pasesdistr=self.PasesDistr

        self.M=Matador.Matador()
        self.T=Toro.Toro()
        self.faena=Faena(self.M,self.T)

        # import matplotlib.pyplot as plt
        # v=[]
        # w=[]
        # for i in range(0,100):
        #     x=tools.rand(0,100)
        #     v.append(x)
        #     y=self.faena.incidente(x)
        #     w.append(y)
        # plt.plot(v,w)
        # pass

        Cronista.termina()



    def initDB(self):
        pass

    def loadMundo(self):
        parser = etree.XMLParser(remove_blank_text=True)
        XMLconstants = etree.parse('mundo.xml', parser)

        XMLConst = XMLconstants.findall("//const")
        for i in XMLConst:
            c=i.attrib['Name']
            try:
                v=int(i.find('val').text)
            except ValueError:
                v=float(i.find('val').text)
            tools.Constants[c]=v

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

        XMLPases = XMLconstants.findall("//paseCapote")
        Limbo.Pases['capote']={}
        for i in XMLPases:
            na=i.attrib['Name']
            de=i.find('desc').text
            di=i.find('dificultad').text
            ar=i.find('articulo').text
            sc=self.PasesDistr[di]['score']
            Limbo.Pases['capote'][na]={"desc":de,"dificultad":di,"maxscore":sc,"articulo":ar}
            # Eliminar NomPases, utilizar solo Pases
            try:
                self.NomPases['capote'][di].append(na)
            except KeyError:
                self.NomPases['capote'][di]=[]
                self.NomPases['capote'][di].append(na)
        XMLPases = XMLconstants.findall("//paseMuleta")
        Limbo.Pases['muleta']={}
        for i in XMLPases:
            na=i.attrib['Name']
            de=i.find('desc').text
            di=i.find('dificultad').text
            sc=self.PasesDistr[di]['score']
            Limbo.Pases['muleta'][na]={"desc":de,"dificultad":di,"maxscore":sc}
            try:
                self.NomPases['muleta'][di].append(na)
            except KeyError:
                self.NomPases['muleta'][di]=[]
                self.NomPases['muleta'][di].append(na)

        # Funcion para frecuencia de incidentes
        # resuelve a y b en ax+b=N para dos puntos (x,N) (maxima tecnica, minima frecuencia) y (minima tecnica, maxima frecuencia)
        a=(tools.Constants['IncidenteFreqMax']-tools.Constants['IncidenteFreqMin'])/(1-100)
        b=tools.Constants['IncidenteFreqMin']-(100*a)
        Faena.a_freqinc=a
        Faena.b_freqinc=b

        XMLIncidentes=XMLconstants.findall("//incidente")
        for i in XMLIncidentes:
            na=i.attrib['Name']
            de=i.find('desc').text
            v=i.find('minmax').text
            ar=i.find('articulo').text
            elem=list(map(int,v.split(',')))
            Limbo.Incidentes[na]={'desc':de,'min':elem[0],'max':elem[1],'articulo':ar}





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


