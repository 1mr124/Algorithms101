import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
from matplotlib.animation import FuncAnimation

def dfs_with_visualization(graph, start_node):
    visited = set()
    dfs_steps = []

    def dfs(node):
        visited.add(node)
        dfs_steps.append((node, visited.copy()))
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                dfs_steps.append((node, visited.copy()))

    dfs(start_node)

    return dfs_steps

def visualize_dfs(graph, dfs_steps):
    pos = nx.spring_layout(graph)  # Position nodes using spring layout
    node_colors = ['lightblue' for _ in graph.nodes()]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title('DFS Visualization')

    def update(step):
        ax.clear()
        current_node, visited_nodes = dfs_steps[step]

        # Draw graph
        nx.draw_networkx_nodes(graph, pos, ax=ax, node_color=node_colors)
        nx.draw_networkx_labels(graph, pos, ax=ax)
        nx.draw_networkx_edges(graph, pos, ax=ax)

        # Highlight current node and visited nodes
        node_colors_highlighted = ['salmon' if node == current_node else 'lightblue' for node in graph.nodes()]
        node_colors_visited = ['gray' if visited else 'lightblue' for visited in visited_nodes]

        nx.draw_networkx_nodes(graph, pos, ax=ax, node_color=node_colors_highlighted, node_size=500)
        nx.draw_networkx_nodes(graph, pos, ax=ax, node_color=node_colors_visited, node_size=500)

        ax.set_title(f'Step {step + 1}: Visiting {current_node}')
        ax.set_xticks([])
        ax.set_yticks([])

    anim = FuncAnimation(fig, update, frames=len(dfs_steps), repeat=False)
    plt.show()

# Example usage:
graph = defaultdict(list)
graph['A'] = ['B', 'C']
graph['B'] = ['D', 'E']
graph['C'] = ['F']
graph['D'] = []
graph['E'] = ['F']
graph['F'] = []

start_node = 'A'
dfs_steps = dfs_with_visualization(graph, start_node)
visualize_dfs(nx.DiGraph(graph), dfs_steps)
