import sys
import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def nearest_neighbor(graph):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    tour = []

    # Start from the first node
    current_node = 0
    tour.append(current_node)
    visited[current_node] = True

    for _ in range(num_nodes - 1):
        min_distance = sys.maxsize
        nearest_node = None

        for neighbor in range(num_nodes):
            if not visited[neighbor] and graph[current_node][neighbor] < min_distance:
                min_distance = graph[current_node][neighbor]
                nearest_node = neighbor

        tour.append(nearest_node)
        visited[nearest_node] = True
        current_node = nearest_node

    # Return to the starting node to complete the tour
    tour.append(tour[0])

    return tour

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour = nearest_neighbor(graph)

print("Optimal Tour:", tour)
