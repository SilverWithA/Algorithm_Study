def subsets(nums):
    res = []
    def dfs(index, path):
        res.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path + [nums[i]])





print(subsets([1,2,3]))