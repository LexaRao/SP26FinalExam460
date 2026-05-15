"""
CS 460 - Algorithms: Final Programming Assignment
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
Node = str
debuggerMode = True


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return """A single Dijkstra-algorithm process being run is not sufficient since it 
        cannot choose which path covers every relic chamber. It can also not 
        determine if each node on the path will be accessible from the last node 
        on the path it chooses using the Dijkstra algorithm without being run 
        more than once.  After the travel costs are known, the remaining decision 
        is to calculate the cheapest path that uses the least amount of fuel. 
        Calculating this path will require determining which of the 
        inter-location costs decision leads to an optimal solution.  This is a 
        search over orders and not a single computation since it requires us to 
        determine which of the shortest paths found using Dijkstra's shortest 
        algorithm is the optimal solution with the least fuel used."""


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
    returnSet = set()

    # Append the head none labled the spawn node to the returnSet.
    returnSet.add(spawn)

    # For all the elements in the relics list append them to the returnSet.
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
    # Add value for inifity.
    INFINITY = float('inf')

    # Create a dictionary for storing the minimum elements.
    lengthDict = {source: 0.0}
    for element in graph: # Add the empty dictionary list.
        if element != source:
            lengthDict[element] = INFINITY

    # Create a for loop for iterating through each of the nodes and determine the lower cost from source to that element.
    for elementX in graph:
        # Create the required set for storing the greedy solution.
        optimalCost = set() # Keep track of optimal cost by removing duplicate entries.

        # Create a value for storing the last wieght.
        lastWeight = INFINITY

        # Index value.
        indexVal = 0

        # Greedy path from source.
        greedyPath = [source, 0.0]

        # Determine the entry of the min length;.
        if (graph[elementX][indexVal:] != None and len(graph[elementX][indexVal:]) != 0):
            minVal = min(graph[elementX][indexVal:])

        # Cross examine the current element against all other elements to determine if it has the smallest length.
        for elementY in graph[elementX]: # Cycle sorting.
            # Cross referent the min value to determine if we have passed it.
            if (elementY == minVal or elementY == elementX[0]):
                if elementY != elementX[0]: # If the element are not equal.
                    if (elementY[1] < lastWeight): # Append the greedy choice.
                        greedyPath.append([elementY[0], elementY[1]]) # Append the smaller length.
                        optimalCost.add(elementY[1]) # Add elements to a set to prevent duplicate entries.
                        lastWeight = elementY[1] # Determine the smallest last weight.
                else: # The algorithm has reach the destination path so exit the loop.
                    greedyPath.append([elementY[0], elementY[1]]) # Append the destination cost.
                    optimalCost.add(elementY[1]) # Add the transaction cost to get to the destination to the entries.
                    break
            else: # Calculate the new min value.
                if (len(elementX[indexVal:]) != 0):
                    minVal = min(elementX[indexVal:])


            # Increment index.
            indexVal += 1

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
    # Create a empty list for storing relics.
    vistedRelics = list()

    # Create a return dictionary for the data to be placed in. 
    returnNodeLength = dict()

    # Select a source with the given data.
    source = select_sources(spawn=spawn, relics=relics, exit_node=exit_node)

    # Create a for loop for each of the element in the source.
    for element in source:
        # For each element run dijkstra algorithm on the element as the source.
        lengthDict = run_dijkstra(graph, element)

        # For each of the elements in the source append the element to the return list.
        returnNodeLength[element] = lengthDict

        # Try the process of appending the data.
        try:
            # Record relics visited.
            if (source != [None] and (element != source[0] or element != element[-1])):
                vistedRelics.append(element)
        except TypeError as E:
            if debuggerMode == True:
                print("Debugger: Source is empty.")

    # Return the precomputed distances lookup for every source in you destination table.
    return returnNodeLength


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
    return """Before the first iteration, the invariant cases should contain an index 
        of the first key in the dictionary.  The non-finalized pairs should 
        contain the first element in a given row of non-finalized pairs.  
        Because the program makes sure that upon each iteration, it has not
        gotten past the destination.  It is also because the values for the min 
        distances are added to the output array using dynamic programming.  The 
        invariant guarantees that the algorithm ends since the inner loop always 
        terminates once it has gotten to the end of the list or the destination.  
        The outer loop terminates after it has accounted for every node in the 
        list.  The correct distance, as determined by the Dijkstra shortest path 
        algorithm, is used to plot the path, which would be the optimal path for 
        the Torchbearer."""



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
    return "The greedy method fails because it finds all greedy solutions and " \
    "the optimal solution.  This means that it is unable to determine which good " \
    "solutions are optimal out of all the solutions that are provided.  One " \
    "example of a solution that does not work well is when you have two different " \
    "greedy paths {2, 4, 8} and {5, 7, 9}. The greedy algorithm sees them both as " \
    "perfectly valid; however, path one has a cost of 14, while path two has a cost " \
    "of 21. This means that it cannot determine which path is more efficient, and the " \
    "torchbearer loses more fuel as a direct result.   However, both solutions provided" \
    "are the greedy solution found using dijkstra algorithm.  A greedy pick is a " \
    "choice that includes the maximum possible decisions that are smallest based on " \
    "the current choice.  How effective are choices measured using the weight?  " \
    "The number of decisions is returned based on how many nodes are returned." \
    "The optimal choice, if all choices are optimal, leads to the global optimal." \
    "This choice is the most fuel-efficient set of greedy choices allowed." \
    "The decision at each choice must be made by factoring into account all " \
    "possible greedy decisions and then choosing the greediest decision.  The " \
    "greedy decision loses since many greedy decisions cost more fuel than the " \
    "optimal decision.  There are more greedy decisions available for any set of " \
    "stops that are less efficient than the optimal decision.  Hence, this " \
    "reasoning is why the greedy decision loses as a direct result.  The " \
    "algorithm must explore the order of elements that is the most efficient " \
    "and hits the most destinations when factoring into account the cost."


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table: dict[node, dict[node, float]], spawn: node, relics: list[node], exit_node: node):
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
    # Add the entry to the distance node.
    routeList = list()
    # routeList.append(spawn)

    # Create a variable to contain the minimal fuel costs.
    minFuelCost = 0

    # Calculate the total cost using this route.
    minNode = min(dist_table[spawn])
    curNodeSet = dist_table[spawn]
    minNodeVal = curNodeSet[minNode]
    minFuelCost = float(minFuelCost) + float(minNodeVal)

    # Iterate over every element in the distance table.
    for relic in dist_table:
        # Determine if the value is in the list of relics.
        for pathRelic in relics:
            # Use the if then logic to determine the value.
            if (relic != spawn and relic != exit_node and relic == pathRelic):
                # Append this value onto the list.
                routeList.append(min(relic))

                # Calculate the total cost using this route.
                minNode = min(dist_table[relic])
                curNodeSet = dist_table[relic]
                minNodeVal = curNodeSet[minNode]
                minFuelCost = float(minFuelCost) + float(minNodeVal)

            # If the relic is equal to the destination node please exit the loop.
            if (relic == exit_node):
                break

    # Place the destination node in the list of nodes as well.
    routeList.append(exit_node)

    # Find the min fuel cost.
    exitVisted = exit_node in routeList
    if (not(exitVisted)):
        minNode = min(dist_table[exit_node])
        curNodeSet = dist_table[exit_node]
        lastNodeVal = curNodeSet[minNode]
        minFuelCost += lastNodeVal

    # Create a optimal route list.
    optimalRoute = float(minFuelCost), list(routeList)

    # Return the value for the route.
    return optimalRoute


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
    # Create a varible for reaching the current location.
    curLocationReached = False

    # Append the value for the current node to the best path.
    if (best == [None]):
        best.append(current_loc)

    # Define relic as equal to the current node.
    relic = dist_table[current_loc]
        
    # Determine if the relic has already been visted and is not a current node or exit node.
    if (relic != current_loc and relic != exit_node and relic in relics_remaining):
        # Find the optimal path at the current relic using a dynamic function call instead 
        # of deleting entries in dist_table.this for safety.  This condition prevents paths that are 
        # not using the minimal amount of fuel from interfering.
        curMinRelic = min(relic)
                
        # Determine the current min cost.
        minCost = relic[curMinRelic]

        # Add this to the total cost so far.
        cost_so_far += minCost

        # Add this to the current relics visted in the correct order.
        relics_visited_order.append(curMinRelic)

        # Dequeue it from relics remaining.  
        del(relics_remaining[curMinRelic])

        # Add the current relics for the best solution found so far.
        best.append(curMinRelic)
    elif (relic == exit_node or nextElement == None): # Exit the current node. (Base case.)
        # Append the end node onto the current path.
        best.append(exit_node)

        # Exit since this is the last position in the path.
        return

    
    # Define the next node based on the position of the first node.
    nextElement = None

    # Create a value for finding the next value in the current node.
    for curRelic in dist_table:
        # If the current location has been reached make sure to get to that position.
        if curRelic is current_loc:
            curLocationReached = True
            continue

        # If the current node has been reach make sure to record the element and break the loop.
        if curLocationReached == True:
            nextElement = curRelic
            break

    # Recurisively call the function.
    _explore(dist_table=dist_table, current_loc=nextElement, relics_remaining=relics_remaining, relics_visited_order=relics_visited_order,
             cost_so_far=cost_so_far, exit_node=exit_node, best=best)

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph: dict[node, list[tuple[node, int]]], spawn: node, relics: list[node], exit_node: node):
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
    # Calculate the distance.  
    distanceFromSource = precompute_distances(graph=graph, spawn=spawn, relics=relics, exit_node=exit_node)

    # Determine the return value based on the prior values.
    returnVal = find_optimal_route(dist_table=distanceFromSource, spawn=spawn, relics=relics, exit_node=exit_node)

    # The empty set.
    emptySet = list()

    # Determine cases.
    if (returnVal == None or returnVal == [0, [None]]):
        return float('inf'), emptySet
    # Return the found return case.
    else:
        return returnVal

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
