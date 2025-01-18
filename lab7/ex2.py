import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import triangulate

# Points for Variant 1 (one camera sufficient): Convex polygon
points_variant_1 = [
    (0, 0),  # P1
    (4, 1),  # P2
    (3, 4),  # P3
    (1, 5),  # P4
    (-2, 4),  # P5
    (-3, 1),  # P6
]

# Points for Variant 2 (two cameras necessary): Non-convex polygon
points_variant_2 = [
    (0, 5),  # P1
    (1, 2),  # P5
    (3, 2),  # P6
    (3, 0),  # P4
    (3, -2),  # P2
    (-1, -2)  # P3
]


def plot_polygon_with_cameras(points, title):
    """
    Function to triangulate a polygon, determine camera positions, and visualize the result.
    """
    # Create the polygon using Shapely
    polygon = Polygon(points)

    # Triangulate the polygon
    triangles = triangulate(polygon)

    # Extract unique vertices from triangles for camera placement
    unique_vertices = set()
    for triangle in triangles:
        for coord in triangle.exterior.coords[:-1]:  # Exclude duplicate last point (closing the triangle)
            unique_vertices.add(coord)

    # Choose camera positions (at most ⌊n/3⌋ cameras based on the Art Gallery Theorem)
    camera_positions = list(unique_vertices)[:len(points) // 3]

    # Plot the polygon, triangulation, and cameras
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the triangulated triangles
    for triangle in triangles:
        x, y = triangle.exterior.xy
        ax.fill(x, y, alpha=0.3, color='lightblue', edgecolor='blue', linewidth=1)

    # Plot the original polygon
    x, y = polygon.exterior.xy
    ax.plot(x, y, color='black', linewidth=2, label='Polygon')

    # Plot camera positions
    for camera in camera_positions:
        ax.plot(camera[0], camera[1], 'ro', label='Camera' if 'Camera' not in ax.get_legend_handles_labels()[1] else '')

    # Annotate vertices with their labels (P1, P2, etc.)
    vertex_labels = ['P' + str(i + 1) for i in range(len(points))]
    for i, (x, y) in enumerate(points):
        ax.text(x, y, f" {vertex_labels[i]}", fontsize=10, color='purple')

    # Add legend, title, and labels
    ax.legend()
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid()
    plt.show()

    # Output the camera positions
    print(f"Camera positions for '{title}':")
    for camera in camera_positions:
        print(camera)


# Plot Variant 1 (One Camera Sufficient)
plot_polygon_with_cameras(points_variant_1, "Variant 1: One Camera Sufficient")

# Plot Variant 2 (Two Cameras Necessary)
plot_polygon_with_cameras(points_variant_2, "Variant 2: Two Cameras Necessary")
