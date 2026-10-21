import heapq
from collections import defaultdict

def sol1(part, comp):
    d = {}

    for name in part:
        d[name] = d.get(name, 0) + 1

    for name in comp:
        d[name] -= 1

    for name in d:
        if d[name] > 0:
            return name
    return None

def sol2(gen, plays):
    t = defaultdict(int)
    s = defaultdict(list)

    for i, (g, play) in enumerate(zip(gen, plays)):
        t[g] += play
        s[g].append((-play, i))

    ans = []

    for genre in sorted(t, key=t.get, reverse=True):
        heapq.heapify(s[genre])
        for _ in range(min(2, len(s[genre]))):
            play, idx = heapq.heappop(s[genre])
            ans.append(idx)

    return ans

def sol3(id_list, report, k):
    re_user = {user: set() for user in id_list}

    for r in report:
        user, t = r.split()
        re_user[user].add(t)

    re_cnt = {user: 0 for user in id_list}

    for user in id_list:
        for t in re_user[user]:
            re_cnt[t] += 1

    res = {user: 0 for user in id_list}

    for user in id_list:
        for t in re_user[user]:
            if re_cnt[t] >= k:
                res[user] += 1

    return [res[user] for user in id_list]

def sol4(record):
    users = {}

    for r in record:
        parts = r.split()

        if parts[0] == "Enter" or parts[0] == "Change":
            users[parts[1]] = parts[2]

    ans = []

    for r in record:
        parts = r.split()

        if parts[0] == "Enter":
            ans.append(users[parts[1]] + "님이 들어왔습니다.")

        elif parts[0] == "Leave":
            ans.append(users[parts[1]] + "님이 나갔습니다.")

    return ans