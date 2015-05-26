# Author  :  Yagao0o
# Date    :  2015-05-26
# Source  :  https://leetcode.com/problems/gas-station/

# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i]
# of gas to travel from station i to its next station (i+1).
#  You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index
#  if you can travel around the circuit once, otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0:
            return -1
        if len(gas) == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
        start = 0
        total_gas = gas[0]
        total_gas_cost = cost[0]
        current_length = 1
        length = len(gas)
        while start < length and current_length <= length:
            if total_gas < total_gas_cost:
                total_gas -= gas[start]
                total_gas_cost -= cost[start]
                start += 1
                current_length -= 1
            else:
                total_gas += gas[(start + current_length) % length]
                total_gas_cost += cost[(start + current_length) % length]
                current_length += 1
        return -1 if start == length else start