from collections import deque


def sol1(n: int):
    res, st_idx, ed_idx, sum_val = 1, 1, 1, 1
    # 15 -> 1 2 3 4 5, 7 8, 4 5 6, 15
    while ed_idx != n//2 + 1:
        if sum_val == n:
            res += 1
            ed_idx += 1
            sum_val += ed_idx
        elif sum_val > n:
            sum_val -= st_idx
            st_idx += 1
        else:
            ed_idx += 1
            sum_val += ed_idx
    return res


def sol2(answers):
    p1 = (1, 2, 3, 4, 5)
    p2 = (2, 1, 2, 3, 2, 4, 2, 5)
    p3 = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    p,q,r = 0,0,0
    for i, answer in enumerate(answers):
        if answer == p1[i % 5]: p += 1
        if answer == p2[i % 8]: q += 1
        if answer == p3[i % 10]: r += 1
    M = max(p, q, r)
    res = []
    if p == M: res.append(1)
    if q == M: res.append(2)
    if r == M: res.append(3)
    return res

def sol2_2(answers):
    pass

def sol3(board, moves):
    res = 0
    s= []
    size = len(board)
    for i in moves:
        for j in range(size):
            if board[j][i - 1] != 0:
                t = board[j][i - 1]
                board[j][i - 1] = 0
                if s and s[-1] == t:
                    s.pop()
                    res += 2
                else:
                    s.append(t)
                break
    return res

def sol4(n:int, k:int):
    tmp = [i for i in range(1, n+1)]
    res = []
    idx, cnt = 0, 0
    for _ in range(n-1):
        while cnt < k:
            if tmp[idx] != 0:
                cnt += 1
                if cnt == k:
                    res.append(tmp[idx])
                    tmp[idx] = 0
                    cnt = 0
                    idx = (idx+1)%n
                    break
            idx = (idx+1)%n
    for i in tmp:
        if i != 0:
            res.append(i)
            break
    return res


def sol4_2(n:int, k:int):
    res = []
    dq = deque(x for x in range(1,n+1))
    while True:
        for _ in range(k-1):
            dq.append(dq.popleft())
        res.append(dq.popleft())
        if len(res) == n:
            break
    return res

def sol4_3(n,k):
    pass

print(sol4_2(100,1001))