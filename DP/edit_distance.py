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

    output = "      "
    for y_j in y:
        output += y_j
        output += "  "
    output += "\n"
    for i in range(-1, xm):
        if i > -1:
            output += x[i]
            output += "  "
        else:
            output += "   "
        for j in range(-1, yn):
            output += str((E[(i, j)]))
            output += "  "
        output += "\n"
    print(output)

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

    return E[(xm - 1, yn - 1)]


if __name__ == '__main__':
    X = "boarder"
    Y = "barbers"
    delete_cost = lambda x: 1
    replace_cost = lambda x, y: 0 if x == y else 1
    print("Edit Distance: ", edit_distance(X, Y, delete_cost, replace_cost))
