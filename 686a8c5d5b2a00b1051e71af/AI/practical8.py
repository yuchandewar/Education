from collections import deque

# Define possible actions
ACTIONS = [
    "move_to_box",
    "push_box_to_banana",
    "climb_box",
    "take_banana"
]

# Define the initial state
# (monkey_position, box_position, monkey_on_box, has_banana)
initial_state = ("floor", "corner", False, False)

def is_goal(state):
    _, _, _, has_banana = state
    return has_banana

def get_successors(state):
    monkey_pos, box_pos, on_box, has_banana = state
    successors = []

    if has_banana:
        return []

    if monkey_pos != box_pos and not on_box:
        # Monkey moves to box
        new_state = (box_pos, box_pos, False, False)
        successors.append((new_state, "move_to_box"))

    if monkey_pos == box_pos and not on_box:
        # Monkey pushes box to banana (assume banana is at "middle")
        new_state = ("middle", "middle", False, False)
        successors.append((new_state, "push_box_to_banana"))

    if monkey_pos == "middle" and box_pos == "middle" and not on_box:
        # Monkey climbs box
        new_state = ("middle", "middle", True, False)
        successors.append((new_state, "climb_box"))

    if monkey_pos == "middle" and box_pos == "middle" and on_box:
        # Monkey takes banana
        new_state = ("middle", "middle", True, True)
        successors.append((new_state, "take_banana"))

    return successors

def monkey_banana_bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        state, path = queue.popleft()
        if is_goal(state):
            return path

        visited.add(state)

        for new_state, action in get_successors(state):
            if new_state not in visited:
                queue.append((new_state, path + [action]))

    return None

# Run the planner
if __name__ == "__main__":
    plan = monkey_banana_bfs(initial_state)
    if plan:
        print("Monkey's plan to get the banana:")
        for step in plan:
            print("→", step)
    else:
        print("No plan found.")
