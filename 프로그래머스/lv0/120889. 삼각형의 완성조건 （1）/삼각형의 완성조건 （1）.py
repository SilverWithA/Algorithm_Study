def solution(sides):
    max_len = 0
    for i in range(len(sides)):
        if sides[i] >= max_len:
            max_len = sides[i]
    if sum(sides) - max_len > max_len:
        return 1
    else:
        return 2
