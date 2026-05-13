# A code bases for testing if a current project is working a intended.
test1 = {"Cat": 0, "Bat": 2, "Sat": 8}

# Test accessing data at given position using iteration.
for element in test1:
    print(test1[element])

# Test accessing tuple value.
val1 = ("val", 2)
print(val1[1])

def hello():
    """
    Returns
    -------
    str
        Before the first iteration, the invariant cases should contain an index 
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
        the Torchbearer.  

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

print(hello())