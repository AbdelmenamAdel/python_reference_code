
# ! ################## Depth First Search ##################
def DFS(graph,start,goal):
    visited =[]
    stack=[[start]]
    while stack:
        path =stack.pop()
        node=path[-1]
        if node in visited:
            continue
        visited.append(node)  
        if node is goal:
            return path
        else:
            for adjacent in graph.get(node,[]):
                new_path=path.copy()
                new_path.append(adjacent)
                stack.append(new_path)
            
graph = {
    'S': ["A", "B","D"],
    "A": ["C"],
    "B": ["D"],
    "C": ["G","D"],
    "D": ["G",],
    "g":[]
}
path =DFS(graph, "S", "G")
print(path)  
