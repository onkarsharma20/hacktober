# python3 code for trappingWater() which takes arr[] and N as input parameters and returns the total amount of water that can be trapped

class Solution:
    def trappingWater(self, arr,n):
        k=arr[0]
        final1=0
        ans=0
        for i in range(1,n,1):
            if arr[i]>=k:
                t=True
                final1=final1+ans
                ans=0
                k=arr[i]
            else:
                t=False
                ans+=k-arr[i]
        k=arr[n-1]
        final2=0
        ans=0
        if t==True:
            return final1
        else:
            for j in range(n-2,-1,-1):
                if arr[j]>k:
                    final2=final2+ans
                    ans=0
                    k=arr[j]
                else:
                    ans+=k-arr[j]
        return final1+final2
