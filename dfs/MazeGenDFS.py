#!/usr/bin/env python3

#Import section
import numpy as np




class dfs():
    def __init__(self, graphSize=1):
        self.Graph = self.generateGraph(np.zeros((graphSize,graphSize)))
        self.marked = {node:False for node in self.Graph}
        self.maze = np.zeros((graphSize,graphSize ))

    def generateGraph(self, mazeArrayPoints):
        '''
            generate graph adjacency list from np zeros array

            Args:
                np array
            
            Returns:
                dict with every point to it's all neighbors
        '''
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        Graph = {}
        rows, cols = mazeArrayPoints.shape
        for x in range(rows):
            for y in range(cols):
                Graph[(x,y)] = []
                for neighbor in directions:
                    Graph[(x,y)].append(tuple(np.add((x,y), neighbor)))
        return Graph

    def visit(self, node):
        '''
            to visit the node

            Args:
                node : which is a node in our graph to mark it as visited
            
            Returns:
                None
        '''
        self.maze[node] = 1

    def dfs(self, startNode):
        '''
            a breadth-first search Recursive implementation

            Args : 
                Graph: Adjacency list
                v : node 
        '''
      
        self.visit(startNode)
        self.marked[startNode] = True

        for w in self.Graph[startNode]:
            if not self.marked[w]:
                self.dfs(w)




    




if __name__ == '__main__':
    print("Hello world!")
    #graph = {'A': ['B', 'S'], 'B': ['A'], 'S': ['A', 'G', 'C'], 'D': ['C'], 'G': ['S', 'F', 'H'], 'H': ['G', 'E'], 'E': ['C', 'H'], 'F': ['C', 'G'], 'C': ['D', 'S', 'E', 'F']}
    #marked = {node:False for node in graph}
    #dfs(Graph=graph,root='A' )
