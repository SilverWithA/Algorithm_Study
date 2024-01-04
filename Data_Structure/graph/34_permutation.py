import itertools

nums = [1,2,3]


### 풀이 1 > 구현의 효율과 성능을 위해 itertools 사용 가능
# print(list(itertools.permutations(num)))

### 풀이 2 > DFS를 이용한 순열 풀이 방법
def permute(nums):
    res = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            res.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()



    dfs(nums)
    return res



print(permute(nums))




