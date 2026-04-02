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
from networkx.algorithms.approximation import large_clique_size

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

    maxim=large_clique_size(grafet)
    llistafinal=[clique for clique in nx.enumerate_all_cliques(grafet) if len(clique)==maxim ]

    temps_final=time.perf_counter()
    
    return llistafinal , temps_final-temps_inici , maxim


#Proves

#el nostre graf
g = nx.Graph()
g.add_nodes_from(['charles','gina','amy','jake','raymond'])
g.add_edges_from([('charles','gina'), ('charles','jake'), ('jake','gina'),('jake','raymond'),('amy','gina'),('gina','raymond')])

#graf de lastfm
graf=build_graph('large_twitch_edges.csv')


llista,temps,maxim=cliques(graf)

print(len(llista),temps,maxim)


