#!/usr/bin/env python3

#Import section







def visit(node):
    print(f"{node} has been visited")

def dfs(Graph, root):
    '''
        a breadth-first search Recursive implementation

        Args : 
            Graph: Adjacency list
            v : node 
    '''
    visit(root)
    marked[root] = True
    
    for w in Graph[root]:
        if not marked[w]:
            dfs(Graph, w)






if __name__ == '__main__':
    print("Hello world!")
    graph = {'A': ['B', 'S'], 'B': ['A'], 'S': ['A', 'G', 'C'], 'D': ['C'], 'G': ['S', 'F', 'H'], 'H': ['G', 'E'], 'E': ['C', 'H'], 'F': ['C', 'G'], 'C': ['D', 'S', 'E', 'F']}
    marked = {node:False for node in graph}
    dfs(Graph=graph,root='A' )