
# ! Uniform Cost Search
def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost,path[-1][0]
        
def UCS(graph, start, end):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node is end:
            return path
        for adjacent, cost in graph.get(node,[]):
            new_path = path.copy()
            new_path.append((adjacent, cost))
            queue.append(new_path)
graph = {
    "S":[("A",2),("B",3),("D",5)],
    "C":[("G",2),("D",1)],
    "A":[("C",4)],
    "D":[("G",5)],
    "B":[("D",4)],
    "G":[]
}
path = UCS(graph, 'S', 'G')
print("Solution is : ",path)
print("Cost of the solution is : ",path_cost(path))