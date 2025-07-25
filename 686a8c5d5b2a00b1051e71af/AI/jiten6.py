import itertools

# Function to calculate total path cost
def calculate_path_cost(path, distance_matrix):
    cost = 0
    for i in range(len(path) - 1):
        cost += distance_matrix[path[i]][path[i+1]]
    cost += distance_matrix[path[-1]][path[0]]  # Return to starting city
    return cost

def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    cities = list(range(num_cities))
    min_path = None
    min_cost = float('inf')

    for perm in itertools.permutations(cities):
        cost = calculate_path_cost(perm, distance_matrix)
        if cost < min_cost:
            min_cost = cost
            min_path = perm

    return min_path, min_cost

# Example usage
if __name__ == "__main__":
    # Distance matrix: symmetric with 0 on diagonal
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    path, cost = tsp_brute_force(distance_matrix)
    print("Optimal Path:", path)
    print("Minimum Cost:", cost)
