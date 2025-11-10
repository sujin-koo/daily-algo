class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0

        for i, h in enumerate(height):
            # If current height is greater than the bar at the top of the stack,
            # we can calculate trapped water
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()  # the valley floor index

                if not stack:
                    break  # no left boundary → cannot trap water

                left = stack[-1]  # index of the left boundary (wall)
                width = i - left - 1  # distance between left and right boundaries
                bounded_height = min(height[left], h) - height[bottom]  # water level height
                water += width * bounded_height  # add trapped water

            stack.append(i)  # push the current index as a potential boundary

        return water
