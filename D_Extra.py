#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Graph:

    def __init__(self, vertices=[], edges={}):
        self.vertices = vertices
        self.edges = edges

    def get_vertices(self):
        return self.vertices

    def get_all_edges(self):
        return self.edges

    def get_vertex_index(self, vertex_name):
        return self.vertices.index(vertex_name)

    def get_edges(self, vertex_name):
        return self.edges[vertex_name]

    def get_distance(self, vertex_start, vertex_cible):
        edges = self.get_edges(vertex_start)
        return edges[vertex_cible]

    def edges_exist(self, vertex_name):
        for i in self.edges:
            if vertex_name == i:
                return True
        return False

    def add_vertex(self, vertex_name):
        self.vertices.append(vertex_name)
        if not (self.edges_exist(vertex_name)):
            self.edges[vertex_name] = {}
        return True

    def add_edge(self, vertex_debut, vertex_fin, distance):
        if not (self.edges_exist(vertex_debut)):
            self.edges[vertex_debut] = {}
        self.get_edges(vertex_debut)[vertex_fin] = distance
        return True

    def get_neighbours(self, vertex_name):
        neighbours = []
        edges = self.get_edges(vertex_name)
        for i in edges:
            neighbours.append(i)
        return neighbours


def distance_chemin(prev, dist, debut, fin,intermediare):
    distance = dist[fin]
    chemin = [fin]
    previous = prev[fin]

    while previous != debut:
        chemin.append(previous)
        previous = prev[previous]
    chemin.append(debut)
    chemin.reverse()
    chemin_string = ""
    for ch in chemin:
        if ch != fin and intermediare != math.inf :
            chemin_string += ch + intermediare 
        
       
        else:
        
            chemin_string += ch
    print("prev : ", prev)
    print("dist : ", dist)
    print("From '" + str(debut) + "' to '" + str(fin) + "'  : ")
    print("votre distance est : ", distance)
    print("votre chemin est : ", chemin_string)
    return distance, chemin_string, chemin


def dijkstra(s, graph):
    dist = {}
    prev = {}
    dist[s] = 0
    Q = []

    for v in graph.vertices:
        if v != s:
            dist[v] = math.inf
            prev[v] = None
        Q.append(v)

    while Q:
        minimum = min(dist[v] for v in Q)
        u = next(v for v in Q if dist[v] == minimum)
        Q.remove(u)

        for v in graph.get_neighbours(u):
            temp = dist[u] + graph.get_distance(u, v)
            if temp < dist[v]:
                dist[v] = temp
                prev[v] = u
        

    return dist, prev

def chemin_A_B_C(debut, graph, intermediaire, fin):
    dist_debut, prev_debut = dijkstra(debut, graph)
    dist_intermediaire, prev_intermediaire = dijkstra(intermediaire, graph)

    distance1, chemin_string1, chemin1 = distance_chemin(prev_debut, dist_debut, debut, intermediaire)
    distance2, chemin_string2, chemin2 = distance_chemin(prev_intermediaire, dist_intermediaire, intermediaire, fin)
    #print("distance1, chemin_string1, chemin1 = ", distance1, chemin_string1, chemin1)
    #print("distance2, chemin_string2, chemin2 = ", distance2, chemin_string2, chemin2)

    distance = distance1  + distance2
    chemin_string = chemin_string1 + " -> " + chemin_string2
    chemin = chemin1 + chemin2
    #print("distance, chemin_string, chemin = ", distance, chemin_string, chemin)
    chemin_final = chemin1
    leng = len(chemin2)
    for i in range(leng-1):
        chemin_final.append(chemin2[i+1])
    print("distance = ", distance)
    print("chemin = ", chemin_final)
    #print("distance = ", distance)
    return distance

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = {'A': {'B': 3,'D': 5, 'C': 10},
         'B': {'E': 7, 'D': 4},
         'C': {'D': 2, 'F': 29},
         'D': {'F': 1, 'E': 1},
         'E': {'F': 2},
         'F': {}
         
         }

graph = Graph(vertices, edges)
debut = 'A'
fin = 'F'
intermediare='E'
dist, prev = dijkstra(debut, graph)

distance, chemin_string, chemin = distance_chemin(prev, dist, debut, fin,intermediare)


# In[ ]:




