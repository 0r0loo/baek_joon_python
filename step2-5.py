# 알람 시계

H, M = input().split()

h = int(H)
m = int(M)


if h == 0:
    if m - 45 >= 0:
        print(h, m-45)
    else:
        print(h+23, m+15)
else:
    if m - 45 >= 0:
        print(h, m-45)
    else:
        print(h-1, m+15)
