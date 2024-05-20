#!/usr/bin/env python3

#Import section
import numpy as np
import matplotlib.pyplot as plt
from random import shuffle





class dfs():
    def __init__(self, graphSize=1):
        self.maze = np.zeros((graphSize,graphSize ))
        self.Graph = self.generateGraph(np.zeros((graphSize,graphSize)))
        self.marked = {node:False for node in self.Graph}
        plt.figure(figsize=(8, 8))
        

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
                    MsTwo = tuple(np.add((x,y), neighbor))
                    if MsTwo[0] < 0 or MsTwo[0] >= len(self.maze) or MsTwo[1] < 0 or MsTwo[1] >= len(self.maze) :
                        continue
                    Graph[(x,y)].append(MsTwo)
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
            a d-first search Recursive implementation

            Args : 
                Graph: Adjacency list
                v : node 
        '''
    
        self.visit(startNode)
        self.showUsWtfIsHappening()
        self.marked[startNode] = True
        shuffle(self.Graph[startNode])
        for w in self.Graph[startNode]:
            if not self.marked[w]:
                self.dfs(w)

    def showUsWtfIsHappening(self):
        plt.imshow(self.maze, cmap='binary', interpolation='nearest')
        plt.title('DFS Maze Generation')
        plt.pause(.3)  # Adjust as needed for visualization speed


    




if __name__ == '__main__':
    print("Hello world!")
    #graph = {'A': ['B', 'S'], 'B': ['A'], 'S': ['A', 'G', 'C'], 'D': ['C'], 'G': ['S', 'F', 'H'], 'H': ['G', 'E'], 'E': ['C', 'H'], 'F': ['C', 'G'], 'C': ['D', 'S', 'E', 'F']}
    #marked = {node:False for node in graph}
    #dfs(Graph=graph,root='A' )
    m = dfs(10)
    m.dfs((0,0))
    

