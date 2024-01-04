def combineSum(candidates, target):
    res = []

    def dfs(csum, index, path):

        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            res.append(path[:])

        # 중복이 허용되므로 자신 i를 포함한 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum-candidates[i], i, path + [candidates[i]])
    dfs(target, 0, [])
    return  res

print(combineSum([2,3,5], 8))