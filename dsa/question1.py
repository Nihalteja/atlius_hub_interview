n=int(input())
dp={}
def recur(x):
    if x>n:
        return 0
    if x==n:
        return 1
    if x in dp:
        return dp[x]
    a=recur(x+1)
    b=recur(x+2)
    dp[x]=a+b
    return a+b
print(recur(0))