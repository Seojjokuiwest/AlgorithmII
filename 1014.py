from collections import deque


def sol1(n, a, b):
    ans = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        ans += 1

    return ans


def sol2(maps):
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i, j

    visited = [ [ [False] * 2 for _ in range(m)] for _ in range(n)]

    q = deque([(sx, sy, 0, 0)])
    visited[sx][sy][0] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, lever, dist = q.popleft()

        if maps[x][y] == "E" and lever == 1:
            return dist

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == "X":
                    continue

                next_lever = lever

                if maps[nx][ny] == "L":
                    next_lever = 1

                if not visited[nx][ny][next_lever]:
                    visited[nx][ny][next_lever] = True
                    q.append((nx, ny, next_lever, dist + 1))

    return -1


def sol3():
    pass

def sol4():
    pass