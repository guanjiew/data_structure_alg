Input: 

Given Strings $X = x_1, ..., x_m$ and $Y = y_1,..., y_n$ and $d(a)$ the cost of deleting a symbol a and $r(a,b)$ the cost of replacing symbol a with b, $r(a,b) = 0$ if $a =b$. 

Output: 

The minimum cost of match X and Y

Optimal Structure

Consider the last symbol $x_m,y_n$ of X and Y.

Let $E(i,j)$  be the edit distance between $x_1, ..., x_i$ and $y_1,..., y_j$

Case 1:  Delete $x_i$, and optimally match string $x_1, ..., x_{i-1}$ and $y_1,..., y_j$

$E(i,j) = E(i-1, j) + d(x_i)$

Case 2:  Delete $y_j$, and optimally match string $x_1, ..., x_i$ and $y_1,..., y_{j-1}$

$E(i,j) = E(i, j-1) + d(y_j)$

Case 3:  Match $x_i, y_j$ and optimally match string $x_1, ..., x_{i-1}$  and $y_1, ...,y_{j-1}$

$E(i,j) = E(i-1, j-1) + r(x_i, y_j)$

$E(m,n)$ is the solution for the problem.

Suppose all intervals are sorted by increasing finishing time 

 $p[j]$ stores the largest index  $i < j$ such that interval i is compatible with interval j

Bellman equation

$$ E(i,j) = 
  \begin{cases} 0  & \text {if } j = 0 \wedge i = 0  \\  E(0, j-1) + d(y_j)  & \text {if } j > 0 \wedge i = 0  \\E(i-1, 0) + d(x_i)  & \text {if } i > 0 \wedge j = 0  \\
    min\{ E(i-1, j) + d(x_i), \\E(i, j-1) + d(y_j),\\E(i-1, j-1) + r(x_i,y_j)\} & \text{if } i > 0  \wedge j > 0 \\
  \end{cases}$$

```python
def edit_distance(x, y, dc, rc):
    E = {}
    xm = len(x)
    yn = len(y)
    E[(-1, -1)] = 0
    for i in range(xm):
        E[(i, -1)] = dc(x[i]) + E[(i - 1, -1)]
    for j in range(yn):
        E[(-1, j)] = dc(y[j]) + E[(-1, j - 1)]
    for i in range(xm):
        for j in range(yn):
            E[(i, j)] = min(dc(x[i]) + E[(i - 1, j)], dc(y[j]) + E[(i, j - 1)], rc(x[i], y[j]) + E[(i - 1, j - 1)])
    return E[(xm - 1, yn - 1)]
```

```jsx
    i = xm - 1
    j = yn - 1
    while i > - 1 and j > -1:
        if E[(i, j)] == E[(i - 1, j)] + dc(x[i]):
            print("Delete {} at position {} of X".format(x[i], i))
            i -= 1
        elif E[(i, j)] == E[(i, j - 1)] + dc(y[j]):
            print("Delete {} at position {} of Y".format(y[j], j))
            j -= 1
        elif E[(i, j)] == E[(i - 1, j - 1)] + rc(x[i], y[j]):
            if x[i] != y[j]:
                print("Replace {} at position {} of X with {} at position {} of Y".format(x[i], i, y[j], j))
            i -= 1
            j -= 1
```

Time Complexity $O(nm)$

Space Complexity $O(nm)$