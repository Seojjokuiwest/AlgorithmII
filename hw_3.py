import sys
from collections import deque

p1, p2 = map(int, sys.stdin.readline().split())
p3 = list(map(int, sys.stdin.readline().split()))

"""

input :

N, L
A1 A2 A3, ... An

배열을 앞에서부터 잘라서 최소값 찾기

i - L+1 ~ N 까지의 슬라이스 된 배열에서의 최소값을 가져옴

>> 5kk 의 배열을 받자마자 정렬해버리면 어떻게 되지

"""

def sol(N, L, A):
    dq = deque()
    D = []
    for i in range(N):
        # 범위를 벗어난 인덱스 제거
        while dq and dq[0] <= i - L:
            dq.popleft()

        # 현재 값보다 크거나 같은 값의 인덱스 제거
        while dq and A[dq[-1]] >= A[i]:
            dq.pop()
        dq.append(i)
        D.append(A[dq[0]])
    return D


if __name__ == "__main__":
    pass
