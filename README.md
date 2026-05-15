# The Torchbearer

**Student Name:** ___Lexa Hope______________
**Student ID:** ___828505412________________
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  * A single Dijkstra-algorithm process being run is not sufficient since it cannot choose which path covers every relic chamber. [1]  It can also not determine if each node on the path will be accessible from the last node on the path it chooses using the Dijkstra algorithm without being run more than once. [1]

- **What decision remains after all inter-location costs are known:**
  * After the travel costs are known, the remaining decision is to calculate the cheapest path that uses the least amount of fuel. [1]  Calculating this path will require determining which of the inter-location costs decision leads to an optimal solution. [3]

- **Why this requires a search over orders (one sentence):**
  * This is a search over orders and not a single computation since it requires us to determine which of the shortest paths found using Dijkstra's shortest algorithm is the optimal solution with the least fuel used. [1][3]

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Relic Chambers | A chamber that contains a relic that must be collected during the trip. [5] |
| Dungeon Location | A chamber, junction, or trap door that is visited along the way to a relic or the destination. [5] |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Data structure name | Dictionary |
| What the keys represent | Key represents the input value that is used to match the data. [2] |
| What the values represent | The value represents the distance stored in the dictionary for a given key. [2] |
| Lookup time complexity | The lookup time complexity is O(n), given that the whole dictionary must be searched for one length. [2] |
| Why O(1) lookup is possible | This is possible given that if the key is provided and the algorithm does not have to search for it, the Python compiler, interpreting the dictionary, can just find the binary digits sector of memory representing the weight and return it. [2] |

# Todo: Note that this estimate is not accurate.  Assumes that the optimal path is dynamic.
### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** The number of Dijkstra runs is defined by the size of the input array. [1]  Dijkstra will be run as many times as the max length of the outer array in the 2d array containing the nodes. [1]
- **Cost per run:** The cost per run is O(n^2), where n is the size of the outer length of the input array or the length of the longest item in the array. [2]  Whichever one is larger will end up being the value for n in the time complexity function f(n) = O(n^2). [2]  This is because larger numbers dominate smaller numbers in terms of time complexity. [2]
- **Total complexity:** The total complexity for the function is O(n^4), where n is the size of the outer length of the input array or the length of the maximum length item in the array. [2]  Whichever one is larger will end up being the value for n in the time complexity function of f(n) = O(n^4). [2]  This is because larger numbers dominate smaller numbers in terms of time complexity. [2]
- **Justification (one line):** This is because the outer function calling the Dijkstra algorithm recursively has a time complexity of O(n^2) while the inner time complexity of the Dijkstra algorithm is O(n^2). [1]

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  * The invariant means that the function is still iterating through a level of elements in the dictionary for a given node value. [4][6]

- **For nodes not yet finalized (not in S):**
  * The invariants mean that the function is iterating through all of the possible nodes that act as keys for the dictionary. [4][6]

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  * Before the first iteration, the invariant cases should contain an index of the first key in the dictionary. [4][6]
  * The non-finalized pairs should contain the first element in a given row of non-finalized pairs. [4][6]

- **Maintenance : why finalizing the min-dist node is always correct:**
  * Because the program makes sure that upon each iteration, it has not gotten past the destination. [4][6] 
  * It is also because the values for the min distances are added to the output array using dynamic programming. [4][6]

- **Termination : what the invariant guarantees when the algorithm ends:**
  * The invariant guarantees that the algorithm ends since the inner loop always terminates once it has gotten to the end of the list or the destination. [4][6] 
  * The outer loop terminates after it has accounted for every node in the list. [4][6]

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

* The correct distance, as determined by the Dijkstra shortest path algorithm, is used to plot the path, which would be the optimal path for the Torchbearer. [1]

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** 
  * The greedy method fails because it finds all greedy solutions and the optimal solution. [1] This means that it is unable to determine which good solutions are optimal out of all the solutions that are provided. [1]

- **Counter-example setup:** 
  * One example of a solution that does not work well is when you have two different greedy paths {2, 4, 8} and {5, 7, 9}. [1]
  * The greedy algorithm sees them both as perfectly valid; however, path one has a cost of 14, while path two has a cost of 21. [1]
  * This means that it cannot determine which path is more efficient, and the torchbearer loses more fuel as a direct result. [1]
  * However, both solutions provided are the greedy solution found using dijkstra algorithm. [1]  

- **What greedy picks:** 
  * A greedy pick is a choice that includes the maximum possible decisions that are smallest based on the current choice. [1]
  * How effective are choices measured using the weight? [1]
  * The number of decisions is returned based on how many nodes are returned. [1]

- **What optimal picks:** 
  * The optimal choice, if all choices are optimal, leads to the global optimal. [1]
  * This choice is the most fuel-efficient set of greedy choices allowed. [1]
  * The decision at each choice must be made by factoring into account all possible greedy decisions and then choosing the greediest decision. [1]

- **Why greedy loses:** 
  * The greedy decision loses since many greedy decisions cost more fuel than the optimal decision. [1]
  * There are more greedy decisions available for any set of stops that are less efficient than the optimal decision. [1]
  * Hence, this reasoning is why the greedy decision loses as a direct result. [1]

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

  * The algorithm must explore the order of elements that is the most efficient and hits the most destinations when factoring into account the cost. [1]

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | optimalCostValue | float | The smallest amount of fuel used for trip using greedy solution. [3] |
| Relics already collected | vistedRelics | List | Each possible greedy path that contains relics to collect. [3] |
| Fuel cost so far | lengthDict | Dictionary | The fuel cost for every possible greedy path. [1] |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | List |
| Operation: check if relic already collected | Time complexity: O(n) [2] |
| Operation: mark a relic as collected | Time complexity: O(1) [2] |
| Operation: unmark a relic (backtrack) | Time complexity: O(n) [2] |
| Why this structure fits | This data structure first since it is appending each new visted node from the data structure containing source to the relics visted list after it has been visted. [4]  Becuase of dynamic programming this means that this list is able to expand as long as the computer has memory. [4] |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** The worse case time complexity is the omega-case, k = O(k). [2]
- **Why:** This is because the code appends all of the visted relics to the visited list so the search time is just the length of the list whick is k. [2]

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** The best greedy numbers in the set that are larger than the older numbers. [1][3]
- **When it is used:** After making a greedy choice, determine which greedy decision is optimal. [1][3]
- **What it allows the algorithm to skip:** The algorithm determines which greedy number is the minimum out of the remaining numbers by skipping through the other numbers till it finds the minimal number and then calculating the new minimal number based on the present location. [1][3]

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** The current state tells you what position you are in the outermost loop and what element you are on. [1][7]
- **What the lower bound accounts for:** The lower bound accounts for the lowest entry in the returned list that takes the least amount of fuel. [1][7]
- **Why it never overestimates:** Because it determines which value for the total fuel out of the possible values for total fuel can be selected to minimize the possible fuel used during the trip. [1][7]

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- Pruning allows for minimizing the total amount of fuel used while maximizing the likelihood that the torchbearer will make it to all its designated points. [1][7]
- This deletes unnecessary data by eliminating unnessary paths and choices that are preventing the torchbearer from making it too it's designation since it is using two much fuel. [1][7]

## References

> Bullet list. If none beyond lecture notes, write that.

- [1] https://sdsu.instructure.com/courses/199070/pages/single-source-shortest-path-algorithms-2?module_item_id=5959856.
- [2] https://sdsu.instructure.com/courses/199070/files/19768796?module_item_id=5651072.
- [3] https://sdsu.instructure.com/courses/199070/files/20659890?module_item_id=5895131.
- [4] https://docs.python.org/3/.
- [5] https://primer.dynamobim.org/10_Custom-Nodes/10-4_Python.html.
- [6] https://www.cs.cornell.edu/courses/JavaAndDS/loops/01aloop1.html.
- [7] https://www.geeksforgeeks.org/python/append-a-value-to-a-dictionary-python/.
