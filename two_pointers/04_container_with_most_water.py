"""
================================================================================
Problem: Container With Most Water / Warehouse Container Capacity
Pattern: Two Pointers (Greedy Inward Shrinking)
LeetCode: LC 11 - Container With Most Water
================================================================================

Scenario: Warehouse Container Capacity
Several vertical barriers are placed along a storage area, and their heights are:
    heights = [3, 1, 2, 5, 4, 8, 2]

Choose two barriers that can hold the maximum amount of material between them.
The capacity between two barriers is:
    capacity = shorter barrier height × distance between barriers (width)

Example:
    height 3 at index 0 and height 8 at index 5:
    shorter height = min(3, 8) = 3
    distance = 5 - 0 = 5
    capacity = 3 × 5 = 15

    Best pair:
    height 5 at index 3 and height 8 at index 5:
    shorter height = min(5, 8) = 5
    distance = 5 - 3 = 2 -> capacity = 10
    Checking all pairs gives maximum capacity = 15.

Approach (Opposite Direction Two Pointers):
1. Place left pointer at start (0) and right pointer at end (len(heights) - 1).
2. Compute distance = right - left.
3. Compute capacity = min(heights[left], heights[right]) * distance.
4. Update max_capacity = max(max_capacity, capacity).
5. Move the pointer pointing to the shorter wall:
   - If heights[left] < heights[right]: move left += 1 (hoping to find a taller barrier).
   - If heights[right] < heights[left]: move right -= 1.
   - If heights[left] == heights[right]: move either (e.g., left += 1).
6. Repeat while left < right.

Complexity:
- Time Complexity: O(n) - Single pass over the array.
- Space Complexity: O(1) - Constant auxiliary space.
================================================================================
"""

def max_container_capacity(heights: list[int]) -> int:
    l_height = 0
    r_height = len(heights) - 1
    max_capacity = 0

    while l_height < r_height:
        min_height_wall = min(heights[l_height], heights[r_height])
        distance = r_height - l_height
        capacity = min_height_wall * distance
        max_capacity = max(max_capacity, capacity)

        # Move the pointer with the shorter barrier
        if heights[l_height] < heights[r_height]:
            l_height += 1
        elif heights[r_height] < heights[l_height]:
            r_height -= 1
        else:
            l_height += 1

    return max_capacity


if __name__ == "__main__":
    heights = [3, 1, 2, 5, 4, 8, 2]
    result = max_container_capacity(heights)
    print(f"Barrier Heights: {heights}")
    print(f"Maximum Storage Capacity: {result}")
