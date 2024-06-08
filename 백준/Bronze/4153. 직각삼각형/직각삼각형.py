while True:
    s = input()
    if s == "0 0 0":
        break

    nums = list(map(int, s.split()))
    nums.sort()

    tmp = 0
    for i in range(len(nums)):
        if i != len(nums)-1:
            tmp += nums[i] * nums[i]
        else:
            c = nums[i] * nums[i]

    if tmp == c:
        print("right")
    else:
        print("wrong")