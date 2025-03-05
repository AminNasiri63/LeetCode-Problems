class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalTank = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            totalTank += gas[i] - cost[i]
            tank += gas[i] - cost[i]

            if tank < 0 :
                tank = 0
                start = i + 1
        if totalTank >= 0:
            return start
        else:
            return -1