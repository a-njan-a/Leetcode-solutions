#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        
        def ratmaze(maze, path, r, c, result):
            if r == len(maze)-1 and c == len(maze[0])-1 and maze[r][c]== 1:
                result.append(path)
                return result
            
            if maze[r][c] == 0:
                return result
            
            maze[r][c] = 0
            
            if r < len(maze) - 1:
                result = ratmaze(maze, path+"D", r+1, c, result)
                
            if c < len(maze[0]) - 1:
                result = ratmaze(maze, path+"R", r, c+1, result)
                
            if r > 0:
                result = ratmaze(maze, path+"U", r-1, c, result)
                
            if c > 0:
                result = ratmaze(maze, path+"L", r, c-1, result)
                
            
            maze[r][c] = 1
            
            
            return result
            
            
        path = ""    
        result = []
        return ratmaze(m, path, 0, 0, result)
                
            

    #r+1 -> D, r-1 -> U, c+1 -> R, c-1 -> L
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends