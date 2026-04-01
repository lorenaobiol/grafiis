#Tasca 1. El problema de les cliques. (50%)

'''
Un problema freqüent que podem modelar amb grafs és el de buscar subgrafs molt
connectats. En particular, ens agradaria ser capaços de trobar, en una xarxa qualsevol (com
ara les xarxes de last.fm i de Twitch que vam treballar al primer laboratori), trobar la mida
de la clique més gran... i enumerar totes les cliques d’aquesta mida.
Aquest problema no és difícil... és NP-complet. Ara bé, això no vol dir que, per problemes
petits, es puguin fer algoritmes que funcionin. I hi ha grafs en els quals el problema no és
pas tan difícil. Sou capaços de fer un algoritme que funcioni per al graf de last.fm? I per al de
Twitch?

Creeu el vostre propi algoritme (heu de poder explicar al professor com funciona, tant en
global com línia a línia).

Heu de crear un programa ben documentat que prengui un graf simple com argument i
retorni una llista amb les cliques de mida màxima del graf (30%).
'''

import networkx as nx
import time

def build_graph(nomarxiu):
    graf=nx.Graph()
    with open (nomarxiu,'r') as fitxer:
        next(fitxer) 
        for linia in fitxer:
            llista_q_conte=linia.strip().split(',')
            
            graf.add_edge(llista_q_conte[0],llista_q_conte[1])
    
    return graf

def cliques(graf):
    grafet=graf.copy()

    temps_inici=time.perf_counter()

    nodes=list(graf.nodes())

    for n in range(len(nodes)): # aquest nombre s'anira fent gran i passara de 0 a la allargada del graf, per si el graf complet es k-clique. representa la k de clique.



def components_DFS(graf):
    temps_inici=time.perf_counter()

    llista_recorreguda=set()
    llista_final=[]

    nodes=list(graf.nodes())

    for node in nodes:
        if node not in llista_recorreguda:
            
            pendents=[]
            pendents.append(node)
            llista_recorreguda.add(node)

            graf2=[]

            while pendents:
                actual=pendents.pop()     #guardarem el valor del ULTIM ELEMENT de la llista de pendents i alhora l'eliminarem de la llista
                graf2.append(actual)

                for vei in graf.neighbors(actual):
                    if vei not in llista_recorreguda:
                        llista_recorreguda.add(vei)
                        pendents.append(vei)
            
            llista_final.append(graf2)
    
    temps_final=time.perf_counter()
    temps= temps_final-temps_inici
    
    return llista_final, temps
