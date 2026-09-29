from collections import deque


def sol1(n: int):
    res, st_idx, ed_idx, sum_val = 1, 1, 1, 1
    # 15 -> 1 2 3 4 5, 7 8, 4 5 6, 15
    while ed_idx != n:
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
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    res = [0, 0, 0]
    l1, l2, l3 = len(p1), len(p2), len(p3)
    for i, answer in enumerate(answers):
        if answer == p1[i % l1]:
            res[0] += 1
        if answer == p2[i % l2]:
            res[1] += 1
        if answer == p3[i % l3]:
            res[2] += 1
    M = max(res)
    ans = []
    for idx, score in enumerate(res):
        if score == M:
            ans.append(idx + 1)
    return ans


def sol3(board, moves):
    res = 0
    s= []
    for i in moves:
        for j in range(len(board)):
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
    """
    1,2,3,4,5,6,7 pos = 3
    1 2 4 5 6 7 3 pos = 7
    1 2 4 5 7 3 6 pos = 2

    1 2 3 4 5 6 7
    2 3 4 5 6 7 1
    3 4 5 6 7 1 2
    3
    4 5 6 7 1 2
    5 6 7 1 2 4
    6 7 1 2 4 5
    6
    앞에서 빼고 뒤에 넣기
    append leftpop
    """
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
    # 특정 idx 서칭 O(k), 트리를 잘 나누면 O(log k)?
    pass

print(sol1(15))