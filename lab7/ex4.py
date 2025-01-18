import matplotlib.pyplot as plt
import networkx as nx

# Define the 7 points in the plane
points = {
    "A": (0, 0),
    "B": (2, 0),
    "C": (1, 3),
    "D": (3, 2),
    "E": (0, 4),
    "F": (-2, 2),
    "G": (2, 4)
}

# Define the 11 edges of the triangulation
edges = [
    ("A", "B"),
    ("B", "C"),
    ("C", "A"),  # Triangle 1: A-B-C
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),  # Triangle 2: C-B-D-E
    ("C", "F"),
    ("C", "G"),  # Triangle 3: C-F-E-G
    ("E", "F"),
    ("E", "G"),
    ("F", "G")  # Triangle 4: F-E-G
]

# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from(edges)

# Perform 3-coloring of the graph
color_map = nx.coloring.greedy_color(G, strategy="largest_first")

# Dynamically generate enough colors to match color indices
unique_colors_required = max(color_map.values()) + 1
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']  # Predefined colors for visualization
if len(colors) < unique_colors_required:
    # Add more colors dynamically if required
    colors.extend([f'color_{i}' for i in range(len(colors), unique_colors_required)])

# Assign colors to graph nodes
assigned_colors = [colors[color_map[node]] for node in G.nodes]  # Map node indices to actual colors dynamically

# Visualize the triangulation graph
plt.figure(figsize=(8, 8))
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
