
# 682. Baseball Game

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        record = []

        for ops in operations:

            if ops == 'C':
                record.pop()

            elif ops == 'D':
                record.append(2*record[-1])

            elif ops == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(ops))

        return sum(record)