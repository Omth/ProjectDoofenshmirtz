# ProjectDoofenshmirtz
BytelandianGoldCoins
dp = {}
dp[0] = 0
dp[1] = 1
 
def check(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = max(n,check(n/2)+check(n/3)+check(n/4))
        return dp[n]
 
try:
    while True:
        n = int(input())
        print check(n)
except:
    pass
