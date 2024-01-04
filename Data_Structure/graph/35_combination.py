def combine(n, k):
    res = []

    def dfs(elements, start, k):
        # 조합 길이가 충족되면 백트래킹
        if k == 0:
            res.append(elements[:])
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
    dfs([], 1, k)
    return res


print(combine(4, 2))
