import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Maze dimensions
N = 10  # Number of rows
M = 10  # Number of columns
c = 0

# Initialize maze grid
maze = np.zeros((N, M))

# Visualization settings
plt.figure(figsize=(8, 8))

def dfs_maze_generation(x, y):
    # Mark the current cell as visited
    maze[x, y] = 1  # 1 represents visited or path
    plt.imshow(maze, cmap='binary', interpolation='nearest')
    plt.title('DFS Maze Generation')
       
    plt.pause(.9)  # Adjust as needed for visualization speed
            #plt.close()
    global c
    c += 1
    print(c)
    # Define movement directions (right, left, down, up)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)  # Randomize the order of directions

    # Explore neighbors in random order
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # Check if the neighbor is within bounds and not visited
        if 0 <= nx < N and 0 <= ny < M and maze[nx, ny] == 0:
            # Carve a passage between the current cell and the neighbor
            maze[x+nx//2,y+ny//2] = 1
            dfs_maze_generation(nx, ny)

            # Pause to visualize each step (optional)
            

# Start DFS maze generation from the top-left corner (0, 0)
dfs_maze_generation(0, 0)

# Final visualization
#plt.imshow(maze, cmap='binary', interpolation='nearest')
#plt.title('DFS Maze Generation')
#plt.xticks([])
#plt.yticks([])
#plt.show()
