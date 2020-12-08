# for문 4번문제
# 15552
# 빠른 A+B

import sys

T = sys.stdin.readline()


T = int(T)

for i in range(T):
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    print(A+B)


# 다른 사람 코드 map() 함수를 사용하여 int형으로 변환한다.

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
