import networkx as nx

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

        for linia in fitxer:
            llista_q_conte=linia.strip().split(',')
            
            graf.add_edge(llista_q_conte[0],llista_q_conte[1])
    
    return graf

#programar funcio bfs
def components_BFS(graf):
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
    
    return llista_final


def components_DFS(graf):
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
                pendents.pop()

                for vei in graf.neighbors(actual):
                    if vei not in llista_recorreguda:
                        llista_recorreguda.add(vei)
                        pendents.append(vei)
            
            llista_final.append(graf2)
    
    return llista_final


print(build_graph('lastfm_asia_edges.csv'))





    


#programar funcio dfs