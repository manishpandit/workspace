
def del_cost(x):
    return 1
def ins_cost(x):
    return 1
def subs_cost(x, y):
    if x == y: return 0
    return 2

def min_edit_distance(source, target):
    n = len(source) + 1
    m = len(target) + 1
    D = [[0 for j in range(m)] for i in range(n)]
    D[0][0] = 0
    
    for i in range(1, n):
        D[i][0] = D[i-1][0] + del_cost(source[i-1])
    print(D)
    for j in range(1, m):
        D[0][j] = D[0][j-1] + ins_cost(target[j-1])
    for i in range(1, n):
        for j in range(1, m):
            D[i][j] = min(
                D[i-1][j] + del_cost(source[i-1]),
                D[i][j-1] + ins_cost(target[j-1]),
                D[i-1][j-1] + subs_cost(source[i-1], target[j-1]))
    print(D)
    return D[n-1][m-1]

print(min_edit_distance('intention', 'execution'))
#print(min_edit_distance('cat', 'dog'))
