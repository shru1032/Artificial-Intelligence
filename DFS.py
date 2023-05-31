#DFS in Python.
graph = {
 '5' : ['3','7'],
 '3' : ['2', '4'],
 '7' : ['8'],
 '2' : [],
 '4' : ['8'],
 '8' : []
}
visited = []
def DFS(visited, graph, node):
 if node not in visited:
 print(node, "->", end=" ")
 visited.append(node)
 for adjacents in graph[node]:
 DFS(visited, graph, adjacents)

#driver code
print("Path: ", end='\n')
DFS(visited, graph, '5')
