beginword,endword=input().split()
wordlist=list(input().split())
def ladderLength(beginword,endword,wordlist):
    setty=set(wordlist)
    def close_word(strr):
        ans=[]
        for i in range(len(strr)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c!=strr[i]:
                    nxt=strr[:i]+c+strr[i+1:]
                    if nxt in setty:
                        ans.append(nxt)
        return ans
    visited=set()
    from collections import deque
    queue=deque([beginword])
    count=0
    size=len(queue)
    while queue:
        for _ in range(size):
            xx=queue.popleft()
            visited.add(xx)
            if xx==endword:
                print(count+1)
                return count+1
            arr=close_word(xx)
            print(arr)
            for s in arr:
                if s not in visited:
                    visited.add(s)
                    queue.append(s)
        count+=1
        size=len(queue)
    print(0)
    return 0




    