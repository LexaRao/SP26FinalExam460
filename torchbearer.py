"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: __Lexa Hope________________
Student ID:   __828505412________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq
from json.encoder import INFINITY
from platform import node


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        A single Dijkstra-algorithm process being run is not sufficient since it 
        cannot choose which path covers every relic chamber. It can also not 
        determine if each node on the path will be accessible from the last node 
        on the path it chooses using the Dijkstra algorithm without being run 
        more than once.  After the travel costs are known, the remaining decision 
        is to calculate the cheapest path that uses the least amount of fuel. 
        Calculating this path will require determining which of the 
        inter-location costs decision leads to an optimal solution.  This is a 
        search over orders and not a single computation since it requires us to 
        determine which of the shortest paths found using Dijkstra's shortest 
        algorithm is the optimal solution with the least fuel used.

    TODO
    """
    return "TODO"


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    # Create set that will contain the data from the source nodes.
    returnSet = {None}

    # Append the head none labled the spawn node to the returnSet.
    returnSet.add(spawn)

    # For all the lements in the relics list append them to the returnSet.
    for element in relics:
        returnSet.add(element)

    # Append the exit node to the returnSet.
    returnSet.add(exit_node)

    # Convert the set to a list.
    returnList = list(returnSet)

    # Return the return list containing the source.
    return returnList

def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    # Create a dictionary for storing the minimum elements.
    lengthDict = dict[node, float]
    lengthDict = [source, 0.0]
    for element in graph: # Add the empty dictionary list.
        lengthDict.append(element, INFINITY)

    # Create a for loop for iterating through each of the nodes and determine the lower cost from source to that element.
    for elementX in graph:
        # Create the required set for storing the greedy solution.
        greedyPath = [source, 0]
        optimalCost = {0} # Keep track of optimal cost by removing duplicate entries.

        # Create a value for storing the last wieght.
        lastWeight = INFINITY

        # Cross examine the current element against all other elements to determine if it has the smallest length.
        for elementY in elementX: # Cycle sorting.
            if elementY != elementX[0]: # If the element are not equal.
                if (elementY[1] < lastWeight): # Append the greedy choice.
                    greedyPath.append(elementY[0], elementY[1]) # Append the smaller length.
                    optimalCost.add(elementY[1]) # Add elements to a set to prevent duplicate entries.
                    lastWeight = elementY[1] # Determine the smallest last weight.
            else: # The algorithm has reach the destination path so exit the loop.
                greedyPath.append(elementY[0], elementY[1]) # Append the destination cost.
                optimalCost.add(elementY[1]) # Add the transaction cost to get to the destination to the entries.
                break

        # Determine the optimal cost of all element in the list.
        optimalCostValue = sum(optimalCost)

        # Append the element and it cost.
        lengthDict[elementX] = optimalCostValue

    # Return the minimal costs to get from source to each element in the list.
    return lengthDict

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "TODO"


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
