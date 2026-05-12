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

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Key represents the input value that is used to match the data. |
| What the values represent | The value represents the distance stored in the dictionary for a given key. |
| Lookup time complexity | The lookup time complexity is O(n), given that the whole dictionary must be searched for one length. |
| Why O(1) lookup is possible | This is possible given that if the key is provided and the algorithm does not have to search for it, the C++ compiler, interpreting the dictionary, can just find the binary digits sector of memory representing the weight and return it. |

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
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- [1] https://sdsu.instructure.com/courses/199070/pages/single-source-shortest-path-algorithms-2?module_item_id=5959856.
- [2] https://sdsu.instructure.com/courses/199070/files/19768796?module_item_id=5651072.
- [3] https://sdsu.instructure.com/courses/199070/files/20659890?module_item_id=5895131.
- [4] https://docs.python.org/3/.
- [5] https://primer.dynamobim.org/10_Custom-Nodes/10-4_Python.html.