# Dynamic Programming (DP)

Class: CSC373
Created: Apr 28, 2021 6:45 PM
Reviewed: No
# Dynamic Programming
## Weighted Interval Scheduling

    Input: 

    Given n intervals jobs, interval j starts at time $s_j$ and finishes at time $s_j$ with weight $w_j$

    Output: 

    Subset S of compatible intervals with maximum total weight $\sum_{j\in S}w_j$

    If all weights are the same, then this is simply the interval scheduling problem
    Solve with greedy algorithm based on earliest finish time ordering is optimal for this case

Define Sub-problem

    Define $OPT(j)$ as the maximum total weight of the compatible intervals in $\{1,2,...,j\}$ 

    $OPT(n)$ is the solution for the problem.

    Suppose all intervals are sorted by increasing finishing time 

     $p[j]$ stores the largest index  $i < j$ such that interval i is compatible with interval j

Bellman equation

    $$ OPT(j) = 
      \begin{cases}
        0 & \text{for } 0 = j \\
       max \{ OPT(j-1), OPT(p[j] + w_i)  \}, & \text {if } 0 \leq j  \\

      \end{cases}$$

Code

    ```markdown
    Sort intervals by finishing time
    compute p[1], p[2], ..., p[n] (binary search)
    for j = 1 to n 
        OPT[j] = max (OPT[j-1], OPT[p[j]] + w_j)
    ```
Time Complexity 
    $O(n\log(n))$