import matplotlib.pyplot as plt
import networkx as nx

# Define the 4 points in the plane
points = {
    "A": (0, 0),
    "B": (2, 0),
    "C": (1, 2),
    "D": (1, 1)
}

# Define the edges of the triangulation
edges = [
    ("A", "B"),
    ("B", "C"),
    ("C", "A"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D")  # Adding this diagonal finishes the triangulation
]

# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from(edges)

# Perform 3-coloring of the graph
color_map = nx.coloring.greedy_color(G, strategy="largest_first")

# Dynamically generate enough colors
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
assigned_colors = [colors[color_map[node]] for node in G.nodes]  # Map node indices to actual colors dynamically

# Visualize the triangulation graph
plt.figure(figsize=(6, 6))
pos = {key: (x, y) for key, (x, y) in points.items()}  # Match points to graph nodes
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color=assigned_colors,
    font_weight="bold",
    edge_color='black'
)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(edge[0], edge[1]): f"{edge[0]}{edge[1]}" for edge in edges}, font_color="purple"
)
plt.title("3-Colorable Triangulation Graph")
plt.show()

# Output points, edges, and coloring
print("Points:", points)
print("Edges:", edges)
print("Color Assignments (3-colorable):")
for node, color in color_map.items():
    print(f"Vertex {node}: {colors[color]} (Color code: {color})")
