def dijkstra(graph, source, sink):


    shortest_path = {}
    predecessor = {}
    unexplored_vertices = graph
    infini = 9999999
    path=[]


    for Vertex in unexplored_vertices:
        shortest_path[Vertex] = infini
    shortest_path[source] = 0


    while unexplored_vertices:
        minVertex = None
        for Vertex in unexplored_vertices:
            if minVertex is None:
                minVertex = Vertex
            elif shortest_path[Vertex] < shortest_path[minVertex]:
                minVertex = Vertex
 
        for adjacent_vertex, weight in graph[minVertex].items():
            if weight + shortest_path[minVertex] < shortest_path[adjacent_vertex]:
                shortest_path[adjacent_vertex] = weight + shortest_path[minVertex]
                predecessor[adjacent_vertex] = minVertex
        unexplored_vertices.pop(minVertex)
    Vertex_actuel = sink


    while Vertex_actuel != source:
        path.insert(0, Vertex_actuel)
        Vertex_actuel = predecessor[Vertex_actuel]


    path.insert(0, source)
    if shortest_path[sink] != infini:
        return ('the shortest path is : %s with a distance of %d' %(path,shortest_path[sink]))



graph = {'a':{'b':5,'c':7,'d':1},'b':{'d':4,'e':5},'c':{'d':2,'f':4},'d':{'f':11} ,'f':{'g':2},'e':{'g':2},'g':{}}
print(dijkstra(graph, 'a', 'f'))

