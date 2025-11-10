from collections import deque
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([0])          # stores sums we can make at the current step
        checked_sums = {0}          # prevents recomputing the same sum
        coin_count = 0              # number of coins used (BFS level)

        while queue:
            coin_count += 1         # we are now trying all sums using +1 more coin

            for _ in range(len(queue)):
                current_sum = queue.popleft()

                for coin in coins:
                    next_sum = current_sum + coin

                    if next_sum == amount:
                        return coin_count  # found minimum number of coins!

                    if 0 < next_sum < amount and next_sum not in checked_sums:
                        checked_sums.add(next_sum)
                        queue.append(next_sum)

        return -1  # if we exhausted all options and didn't reach amount
