import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import triangulate

# Define the points of the polygon
points = [
    (-5, 6),(4, 4),(6, 4), (9, 6), (11, 6),
    (11, -6), (9, -6), (6, -4),(4,-4), (-5, -6), (-7, -4), (-7, 4),
]

# Create the polygon using Shapely
polygon = Polygon(points)

# Triangulate the polygon
triangles = triangulate(polygon)

# Extract unique vertices from all triangles
unique_vertices = set()
for triangle in triangles:
    for coord in triangle.exterior.coords[:-1]:  # Exclude duplicate last point
        unique_vertices.add(coord)

# Select vertices for cameras based on the Art Gallery Theorem
# Place cameras at unique vertices
camera_positions = list(unique_vertices)[:len(points) // 3]

# Plot the polygon and triangles
fig, ax = plt.subplots(figsize=(8, 8))
for triangle in triangles:
    x, y = triangle.exterior.xy
    ax.fill(x, y, alpha=0.3, color='lightblue', edgecolor='blue')

# Plot the original polygon
x, y = polygon.exterior.xy
ax.plot(x, y, color='black', linewidth=1, label='Polygon')

# Plot camera positions
for camera in camera_positions:
    ax.plot(camera[0], camera[1], 'ro', label='Camera' if 'Camera' not in ax.get_legend_handles_labels()[1] else '')

# Add legend and labels
ax.legend()
ax.set_title("Art Gallery Theorem - Surveillance Camera Placement")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid()
plt.show()
