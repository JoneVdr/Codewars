def cube(n):
    r = []
    for i in range(1, n+1):
        j = ' ' * (n-i) + "/\\" * i + '_\\' * n
        r.append(j)
    for i in range(n, 0, -1):
        j = ' ' * (n-i) + "\\/" * i + '_/' * n
        r.append(j)
    return '\n'.join(r)