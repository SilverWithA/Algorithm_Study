import sys

n = int(sys.stdin.readline())

cal_cnt = [[1, 0], [0, 1]] + [[0, 0] for i in range(2, 41)]


def fibonacci(num):

    if num > 1:
        if cal_cnt[num - 2][0] == 0 and cal_cnt[num - 2][1] == 0:
            fibonacci(num - 2)
        if cal_cnt[num - 1][0] == 0 and cal_cnt[num - 1][1] == 0:
            fibonacci(num - 1)

        cal_cnt[num][0] = (cal_cnt[num - 1][0] + cal_cnt[num - 2][0])
        cal_cnt[num][1] = (cal_cnt[num - 1][1] + cal_cnt[num - 2][1])


for _ in range(n):
    num = int(sys.stdin.readline())
    fibonacci(num)
    print(cal_cnt[num][0], cal_cnt[num][1])
