import matplotlib.pyplot as plt
import networkx as nx

# Define the points
points = {
    "A": (0, 0),
    "B": (2, 0),
    "C": (1, 3),
    "D": (3, 2),
    "E": (0, 4),
    "F": (-2, 2)
}

# Define the 10 edges for the full triangulation
edges_full = [
    ("A", "B"),
    ("B", "C"),
    ("C", "A"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D"),
    ("C", "E"),
    ("C", "F"),
    ("E", "F"),
    ("A", "E")
]

# Define the 4 edges for the subset {A, B, C, F}
edges_subset = [
    ("A", "B"),
    ("B", "C"),
    ("C", "F"),
    ("A", "F")
]

# Create graphs
G_full = nx.Graph()
G_full.add_edges_from(edges_full)

G_subset = nx.Graph()
G_subset.add_edges_from(edges_subset)

# Visualize the full triangulation
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos = {key: (x, y) for key, (x, y) in points.items()}
nx.draw(
    G_full, pos, with_labels=True, node_size=700, font_weight="bold", node_color="lightblue", edge_color="black"
)
plt.title("Full Triangulation (10 Edges)")

# Visualize the subset triangulation
plt.subplot(1, 2, 2)
subset_points = {key: points[key] for key in ["A", "B", "C", "F"]}
pos_subset = {key: (x, y) for key, (x, y) in subset_points.items()}
nx.draw(
    G_subset, pos_subset, with_labels=True, node_size=700, font_weight="bold", node_color="lightgreen",
    edge_color="black"
)
plt.title("Subset {A, B, C, F} (4 Edges)")

plt.show()
