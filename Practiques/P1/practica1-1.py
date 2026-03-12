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

#programar funcio bfs
def components_BFS(graf):
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
                actual=pendents[0]
                graf2.append(actual)
                pendents.pop(0)

                for vei in graf.neighbors(actual):
                    if vei not in llista_recorreguda:
                        llista_recorreguda.add(vei)
                        pendents.append(vei)
            
            llista_final.append(graf2)
    
    temps_final=time.perf_counter()
    temps= temps_final-temps_inici
    
    return llista_final, temps


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
                actual=pendents.pop()
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

def experiment_resiliencia_inversa(graf, num_simulacions=1):
    graf_original = graf.copy()
    
    # Ens quedem només amb la Component Gegant per assegurar que pot ser connex
    nodes_objetiu = max(nx.connected_components(graf_original), key=len)
    arestes_totals = list(graf_original.subgraph(nodes_objetiu).edges())
    num_nodes = len(nodes_objetiu)
    total_arestes_disponibles = len(arestes_totals)
    
    resultats_talls_necessaris = []

    print(f"Nodes en la component: {num_nodes}")
    print(f"Arestes totals: {total_arestes_disponibles}")

    for i in range(num_simulacions):
        # Barrejem les arestes aleatòriament
        random.shuffle(arestes_totals)
        
        # Creem un graf buit només amb els nodes
        g_sim = nx.Graph()
        g_sim.add_nodes_from(nodes_objetiu)
        
        arestes_posades = 0
        for u, v in arestes_totals:
            g_sim.add_edge(u, v)
            arestes_posades += 1
            
            # El graf es torna connex quan té exactament 1 component
            if nx.is_connected(g_sim):
                # Si hem necessitat 'arestes_posades' per connectar-lo,
                # per desconnectar-lo hauríem de tallar:
                talls = total_arestes_disponibles - arestes_posades + 1
                resultats_talls_necessaris.append(talls)
                break
                
    mitjana = sum(resultats_talls_necessaris) / num_simulacions
    print(f"\nResultat mitjà després de {num_simulacions} simulacions:")
    print(f"Hauries de tallar aproximadament {mitjana:.2f} arestes per dividir el graf.")
    
    return mitjana

# Execució









    
resultat=build_graph('lastfm_asia_edges.csv')
print(resultat)

resultat2, temps =components_BFS(resultat)
print(len(resultat2))

print(temps)
print(build_graph('lastfm_asia_edges.csv'))
'''
arestes=arestes_tallar(build_graph('lastfm_asia_edges.csv'),2)
print(arestes)

resultat1, temps =components_BFS(arestes)
print(len(list(resultat1)))
print()
'''
miitj=experiment_resiliencia_inversa(resultat)
print(miitj)


    


#programar funcio dfs