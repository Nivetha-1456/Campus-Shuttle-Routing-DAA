# Campus Shuttle Routing & Capacity Scheduling
# DAA Project

import heapq

# -------------------------------
# Dijkstra's Algorithm
# -------------------------------
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# -------------------------------
# Greedy Shuttle Scheduling
# -------------------------------
def greedy_shuttle_assignment(routes, capacity):
    routes.sort(key=lambda x: x[1], reverse=True)
    assigned_routes = []
    total_load = 0

    for route in routes:
        if total_load + route[1] <= capacity:
            assigned_routes.append(route)
            total_load += route[1]

    return assigned_routes, total_load


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":

    # Graph representing campus stops
    campus_graph = {
        'A': [('B', 5), ('C', 10)],
        'B': [('A', 5), ('C', 3), ('D', 7)],
        'C': [('A', 10), ('B', 3), ('D', 1)],
        'D': [('B', 7), ('C', 1)]
    }

    print("Shortest paths from Stop A:")
    shortest_paths = dijkstra(campus_graph, 'A')
    for stop, distance in shortest_paths.items():
        print(f"Stop {stop}: {distance} minutes")

    # Shuttle routes: (Route ID, Passenger Count)
    routes = [
        ('Route 1', 40),
        ('Route 2', 30),
        ('Route 3', 20),
        ('Route 4', 10)
    ]

    shuttle_capacity = 70

    assigned, load = greedy_shuttle_assignment(routes, shuttle_capacity)

    print("\nAssigned Routes:")
    for route in assigned:
        print(route)

    print(f"Total Passenger Load: {load}")
