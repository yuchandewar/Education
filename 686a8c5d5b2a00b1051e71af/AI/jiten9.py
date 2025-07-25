import math

# Alpha-Beta Pruning implementation
def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player, tree):
    if depth == 0 or node not in tree:
        return node  # return static evaluation value (leaf node)

    if maximizing_player:
        max_eval = -math.inf
        for child in tree[node]:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False, tree)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for child in tree[node]:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True, tree)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

# Example game tree:
# Each non-leaf node points to a list of children (could be values or other nodes)
example_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

# Run alpha-beta pruning starting from root 'A'
if __name__ == "__main__":
    result = alpha_beta_pruning('A', depth=3, alpha=-math.inf, beta=math.inf,
                                 maximizing_player=True, tree=example_tree)
    print("Best value using Alpha-Beta Pruning:", result)
