import networkx as nx 
import matplotlib.pyplot as plt 
import scipy as sp

homer = open("a.txt", "r")

def read_nodes(homer):
    """Reads in the nodes of the graph from the input file.
    
    Args:
        homer: A handle for the file containing the graph data, starting at the top.
        
    Returns:
        A generator of the nodes in the graph, yielding a list of the form:
            ['CH', 'AG, 'ME', ...]
    """
    line = homer.readline()
    while line != '\n':
        line = line.replace('\n', '')
        if len(line) != 0:
            if line[0] != '*':
                if line[:2] != '1:':
                    yield line[:2]
                else: break
        line = homer.readline()  

def read_edges(homer):
    """Reads in the edges of the graph from the input file.
    
    Args:
        homer: A handle for the file containing the graph data, starting at the top 
            of the edges section.
            
    Returns:
        A generator of the edges in the graph, yielding a list of pairs of the form:
            [('CH', 'AG'), ('AG', 'ME'), ...]
    """

    for line in homer.readlines():
        line = line.replace('\n', '')
        if len(line) > 1:
            if ':' in line:
                idx = line.index(':')
                line = line[(idx+1):]
                all_related_nodes = line.split(';')
                for related_nodes in all_related_nodes:
                    related_nodes = related_nodes.split(',')
                    for idx_node1 in range(len(related_nodes)-1):
                        for idx_node2 in range(idx_node1+1, len(related_nodes)):
                            pair = (related_nodes[idx_node1], related_nodes[idx_node2])
                            yield pair


G = nx.Graph()
G.add_nodes_from(read_nodes(homer))
G.add_edges_from(read_edges(homer))

nx.draw(G)
