class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        
        total = 0
        res = 0
        i = 0
        while i < len(gas):
            total += diff[i]
            if total < 0:
                total = 0
                i += 1
                res = i
            else:
                i += 1
        return res
