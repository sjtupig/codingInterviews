#动态规划直接求最大值有点难，可以退而求其次，先求到index i处结尾的最大值
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [0]*len(array)
        if not array:return 0
        dp[0] = array[0]
        for i in range(1,len(array)):
            if dp[i-1] < 0:
                dp[i] = array[i]
            else:
                dp[i] = dp[i-1]+array[i]
        return max(dp)


#贪心思想
#如果希望达到O(n)时间复杂度，我们就应该能够想到我们只能对整个数组进行一次扫描，在扫描过程中求出最大连续子序列和以及子序列的起点和终点位置。
#假如输入数组为{1,-2,3,10,-4,7,2,-5}，我们尝试从头到尾累加其中的正数，
#初始化和为0，第一步加上1，此时和为1，第二步加上-2，此时和为-1，第三步加上3，此时我们发现-1+3=2，最大和2反而比3一个单独的整数小，这是因为3加上了一个负数，发现这个规律以后我们就重新作出累加条件
#这个方法其实就是动态规划算法的改进
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxsum = min(array)-1
        sum = 0
        for i in array:
            sum += i 
            if sum < 0:
                sum = 0 
                continue 
            if sum > maxsum:
                maxsum = sum 
                
        return maxsum if maxsum >= 0 else max(array)