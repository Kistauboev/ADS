import sys
from collections import deque

def solve():
    input_data=sys.stdin.read().split()
    idx=0
    t=int(input_data[idx])
    idx=idx+1
    results=[]

    for _ in range(t):
        n=int(input_data[idx])
        idx=idx+1
        letters=input_data[idx:idx+n]
        idx=idx+n

        count=[0]*26
        q=deque()
        answers=[]

        for ch in letters:
            c=ord(ch)-ord('a')
            count[c]=count[c]+1
            q.append(ch)

            while q and count[ord(q[0])-ord('a')]>1:
                q.popleft()

            if q:
                answers.append(q[0])
            else:
                answers.append('-1')
        results.append(' '.join(answers))
    print('\n'.join(results))
solve()