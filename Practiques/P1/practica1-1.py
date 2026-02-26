import networkx as nx

#primer funcio bulid graf del arxiu .csv

def build_graph(nomarxiu):
    graf=nx.Graph()
    with open (nomarxiu,'r') as fitxer:

        for linia in fitxer:
            llista_q_conte=linia.strip().split(',')
            
            graf.add_edge(llista_q_conte[0],llista_q_conte[1])
    
    return graf

#programar funcio bfs
def components_BFS(graf):
    llista_veins=[]

    llista_recorreguda=[]

    


#programar funcio dfs