#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        a=A
        b=B
        while a!=b:
            if(a>b):
                a-=b
            else:
                b-=a
        hcf=a
        lcm=(A*B)//hcf
        dividend=A
        divisor=B
        remainder=dividend%divisor
        while(remainder!=0):
            dividend=divisor
            divisor=remainder
            
            remainder=dividend%divisor
        gcd=divisor
        return lcm,gcd
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends