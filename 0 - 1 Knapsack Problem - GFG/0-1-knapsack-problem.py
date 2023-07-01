#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        weight = [[0] * (W+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for w in range(1, W+1):
                if wt[i-1] <= w:
                    weight[i][w] = max(weight[i-1][w], weight[i-1][w-wt[i-1]] + val[i-1])
                else:
                    weight[i][w] = weight[i-1][w]
                    
        return weight[n][W]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends