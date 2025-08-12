from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        Avg = (sum(salary) - (max(salary) + min(salary))) / (len(salary)-2)
        return Avg