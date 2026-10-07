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
    report = set(report)

    reported_count = {}
    reporters = {}

    for r in report:
        user, target = r.split()

        reported_count[target] = reported_count.get(target, 0) + 1

        if target not in reporters:
            reporters[target] = []

        reporters[target].append(user)

    result = {user: 0 for user in id_list}

    for target in reported_count:
        if reported_count[target] >= k:
            for user in reporters[target]:
                result[user] += 1

    return [result[user] for user in id_list]

def sol4(record):
    users = {}

    for r in record:
        parts = r.split()

        if parts[0] == "Enter" or parts[0] == "Change":
            users[parts[1]] = parts[2]

    answer = []

    for r in record:
        parts = r.split()

        if parts[0] == "Enter":
            answer.append(users[parts[1]] + "님이 들어왔습니다.")

        elif parts[0] == "Leave":
            answer.append(users[parts[1]] + "님이 나갔습니다.")

    return answer