#!/usr/bin/env python3

#Import section
import numpy as np
import matplotlib.pyplot as plt
import random





class dfs():
    def __init__(self, graphSize=1, numberOfBlockedNodes=1):
        self.graphSize = graphSize
        self.maze = np.zeros((graphSize,graphSize ))
        self.blockedNodes = np.zeros((graphSize,graphSize))
        self.generateBlockedNodes(numberOfBlockedNodes)
        print(self.blockedNodes)
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

    def generateBlockedNodes(self, numberofBlockedNodes):
        '''
            generate the banned points in the graph

            Args:
                np array
            
            returns:
                None
        '''
        while numberofBlockedNodes > 0:
            
            x, y =  random.randint(0,self.graphSize-1) ,random.randint(0,self.graphSize-1)
            if self.blockedNodes[x,y] == 0:
                numberofBlockedNodes -= 1
                self.blockedNodes[x,y] = 1
            
        


    def visit(self, node):
        '''
            to visit the node

            Args:
                node : which is a node in our graph to mark it as visited
            
            Returns:
                None
        '''
        self.maze[node] = 1

    def dfs(self, startNode, blockedVersion=None):
        '''
            a d-first search Recursive implementation

            Args : 
                Graph: Adjacency list
                v : node 
        '''
        if blockedVersion and self.blockedNodes[startNode] == 1:
            return 
        self.visit(startNode)
        self.showUsWtfIsHappening()
        self.marked[startNode] = True
        random.shuffle(self.Graph[startNode])
        for w in self.Graph[startNode]:
            if not self.marked[w]:
                self.dfs(w,blockedVersion)

    def showUsWtfIsHappening(self):
        plt.imshow(self.maze, cmap='binary', interpolation='nearest')
        plt.title('DFS Maze Generation')
        plt.pause(.0001)  # Adjust as needed for visualization speed


    




if __name__ == '__main__':
    print("Hello world!")
    #graph = {'A': ['B', 'S'], 'B': ['A'], 'S': ['A', 'G', 'C'], 'D': ['C'], 'G': ['S', 'F', 'H'], 'H': ['G', 'E'], 'E': ['C', 'H'], 'F': ['C', 'G'], 'C': ['D', 'S', 'E', 'F']}
    #marked = {node:False for node in graph}
    #dfs(Graph=graph,root='A' )
    m = dfs(20, numberOfBlockedNodes=100)
    for i in range(20):
        for y in range(20):
            if m.maze[i,y] == 0 :
              m.dfs((i,y), blockedVersion=True)
    input("Done: ")

