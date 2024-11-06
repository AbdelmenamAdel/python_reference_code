
# ! ################## Breadth First Search ##################

def BFS(graph, start, end):
    visited=[]
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node in visited:
            continue
        visited.append(node)
        if node == end:
            return path
        else :
            for adjacent in graph.get(node, []):
                new_path = path.copy()
                new_path.append(adjacent)
                queue.append(new_path)
       
graph = {
    'S': ['B','D','A'],
    "A": ["C"],
    "B": ["D"],
    "C": ['G','D'],
    "D": ['G',],
    "g":[]
}
path =BFS(graph, "S", "G")
print(path)  
