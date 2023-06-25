#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        # code here 
        
        if S == 0:
            if D == 1:
                return 1
                
            else:
                return -1
                
        if S > 9*D:
            return -1
            
        S -= 1
        
        digits = [0] * D
        
        for i in range(D-1, 0, -1):
            if S > 9:
                digits[i] = 9
                S -= 9
                
            else:
                digits[i] = S
                S = 0
                
        digits[0] = S + 1
        
        num = 0
        
        for i in range(D):
            num = (num * 10) + digits[i]
            
        return num
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends