import networkx as nx
import time
import random

'''
BASICS PER A NTWX

graf no dirigit -> g=nx.Graph()
g dirigit -> g=nx.DiGraph()
g en pesos -> G.add_edge(1,2,wieght=x)

g.add_node() // g.add_nodes_from((llista))
g.add_edge() // g.add_edges_from((llista))


'''


#primer funcio bulid graf del arxiu .csv

def build_graph(nomarxiu):
    graf=nx.Graph()
    with open (nomarxiu,'r') as fitxer:
        next(fitxer) 
        for linia in fitxer:
            llista_q_conte=linia.strip().split(',')
            
            graf.add_edge(llista_q_conte[0],llista_q_conte[1])
    
    return graf

#BFS -> primer element de la llista de pendents
def components_BFS(graf):
    temps_inici=time.perf_counter()
    llista_recorreguda=set()            #per evitar repetir nodes Aqui guardem els nodes queja coneixiem i NO HEM DE TORNAR A VEURE. || La llista recorreguda ens assegura que cap node es visitara dues vegades
    llista_final=[]                     #aqui guardarem els subgrafs que s'aniran creant. Si no és connex, hi haurà més de una subllista

    nodes=list(graf.nodes())            #Ho passem a llista per a recorrer els vèrtex del graf.

    for node in nodes:
        if node not in llista_recorreguda:#Si no hem mirat els veins de aquell node, es a dir, no l'hem explorat. Només si no hem mirat els seus veins.
            
            pendents=[]                 #Aqui guardarem els nodes veins del node que estem recorrent  || NECESITA SER UNA LLISTA PERÒ NO ADMET REPETICIONS
            pendents.append(node)       #Incloem el que estem recorrent a aquesta llista
            llista_recorreguda.add(node)#I el guardem a la llista dels que ja hem visitat i no hem de tornar a tocar.

            graf2=[]                    #Aquesta veriable es com una mena de "llista final" on guardarem els que ja hem mirat els seus veins

            while pendents:             #Si pendents no esta buida, ja que anirem eliminant elements de dins de la llista
                actual=pendents[0]      #guardarem el valor del PRIMER ELEMENT de la llista de pendents i alhora l'eliminarem de la llista
                graf2.append(actual)    #tambe el guardem al graf resultant ja que aixo significa que l'estem recorrent
                pendents.pop(0)

                for vei in graf.neighbors(actual):      #Mirem els veins d'aquell node
                    if vei not in llista_recorreguda:   #Si el vei no l'hem recorregut en cap moment
                        llista_recorreguda.add(vei)     #l'afegim a esta llista i a la de pendents.
                        pendents.append(vei)            
            
            llista_final.append(graf2)  #Finalment afegim el graf resultant de l'algorisme a la llista final dels vertex
    
    temps_final=time.perf_counter()     #guarda el temps final de l'algorisme
    temps= temps_final-temps_inici      #calcula el temps que ha trigat l'algorisme en executar-se, restant el temps final al temps inicial
    
    return llista_final, temps

#DFS -> ultim element de la llista de pendents
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

'''
def arestes_tallar(graf,n):
    graf2=graf.copy()
    arestes=list(graf2.edges())
    for i in range(n):
        graf.remove_edge(arestes[i][0],arestes[i][1])
    
    return graf'''



def experiment_resiliencia(G_original):
    G = G_original.copy()
    
    arestes = list(G.edges())
    random.shuffle(arestes)
    
    comptador_talls = 0
    
    for u, v in arestes:
        G.remove_edge(u, v)
        comptador_talls += 1
        
        # Comprovem si el graf continua sent connex
        # nx.is_connected(G) utilitza un BFS o DFS per sota
        if not nx.is_connected(G):
            return comptador_talls

    return comptador_talls









    '''
resultat=build_graph('lastfm_asia_edges.csv')
print(resultat)

resultat2, temps =components_BFS(resultat)
print(len(resultat2))

print(temps)
print(build_graph('lastfm_asia_edges.csv'))

arestes=arestes_tallar(build_graph('lastfm_asia_edges.csv'),2)
print(arestes)

resultat1, temps =components_BFS(arestes)
print(len(list(resultat1)))
print()

n_talls = experiment_resiliencia(build_graph('lastfm_asia_edges.csv'))
print(f"Arestes tallades: {n_talls} ")
'''

    


#programar funcio dfs