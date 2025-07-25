import heapq

# Goal state for the 8-puzzle
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank space

# Moves: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def is_goal(state):
    return state == goal_state

def a_star(start):
    heap = []
    visited = set()
    path = []

    def serialize(state):
        return tuple(num for row in state for num in row)

    heapq.heappush(heap, (manhattan_distance(start), 0, start, []))

    while heap:
        est_total, cost, current, route = heapq.heappop(heap)

        serial = serialize(current)
        if serial in visited:
            continue
        visited.add(serial)

        if is_goal(current):
            return route + [current]

        for neighbor in get_neighbors(current):
            if serialize(neighbor) not in visited:
                heapq.heappush(heap, (
                    cost + 1 + manhattan_distance(neighbor),
                    cost + 1,
                    neighbor,
                    route + [current]
                ))

    return None

def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else " " for x in row))
    print()

# Example starting state
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = a_star(start_state)

if solution:
    print("Steps to solve the 8-puzzle:")
    for step in solution:
        print_state(step)
else:
    print("No solution found.")
