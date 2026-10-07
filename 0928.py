ans = "(()[[]])([])"
opn = ["(", "["]
st = []
idx, top = 0, len(ans)-1

for i in range(len(ans)):
    if ans[i] == opn[0] or ans[i] == opn[1]:
        st.append(ans[i])
    