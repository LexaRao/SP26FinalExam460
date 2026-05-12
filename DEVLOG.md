# Development Log – The Torchbearer

**Student Name:** __Lexa Hope________________
**Student ID:** __828505412__________________

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – 05/12/2026: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

    I will implement a solution that enables the Touchbearer engine to traverse the map and hit all the relics with minimal fuel.  The code will use two recursive for loops using the cycle algorithm.  It will use the cycle algorithm because it is most efficient.  One will repeatedly call the Dijkstra algorithm to find the shortest paths.  The next loop will determine which of the paths is optimal and remove non-optimal paths from the solution set.  

    The next portion that will be difficult to implement is responsible for choosing which solutions are optimal.  Hence, this will require comparing older shortest decisions to newer shortest decisions.  This is done using the optimal solution.  Each graph is traversed in the outer recursive loop, and the cost is calculated.  Only the optimal solutions are kept in a queue containing them.  Finally, this queue containing the optimal solution is returned.  

    The inner four loop is responsible for dynamically calculating the map on each recursion.  This aids in determining if the map has changed since the last recursive call.  This process helps calculate maps that can change over the course of the flight.  This will allow for the engine to have a up to data course plotted. This will prevent it from using more fuel than it requires to get to the destination where fuel is costly.  
    
    These programs will be implemented using the template.  This includes the function laid out in the torchbearer.py assignment.  The data from the README.md document will be used to help develop the function within the touchbearer.py portion of the project.  It will aid in making sure the project works as intended.  This document serves to document the toucherbearer.py assignment.  
    
    I will be testing this project using Python.  The scripts will be tested using Visual Studio.  The data from the Assignment.md document will be used to write a testing script called toucherbearer-tester.md.  This will be used to test the project's integrity if it cannot be tested on Python alone.  This will also speed up the development time.  Your feedback on this project is helpful, so please let me know if you have any in the discussion section of this repo.

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 2 Hours |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
