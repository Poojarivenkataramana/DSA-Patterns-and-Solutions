"""
================================================================================
Problem: Intersection of Two Sorted Arrays / Common Warehouse Product IDs
Pattern: Two Pointers (Two Lists Parallel Traversal)
LeetCode: LC 349 / LC 350 - Intersection of Two Arrays (Sorted variant)
================================================================================

Scenario: Common Product IDs in Two Warehouses
Two warehouses have their product IDs in sorted order:
    warehouse_a = [101, 105, 110, 120, 130, 150]
    warehouse_b = [100, 105, 115, 120, 140, 150]
Find the product IDs that exist in both warehouses.

Expected Output:
    [105, 120, 150]

Rules:
- Use two pointers (one pointer for each list).
- No nested loops.
- Do not use Python set().

Approach:
1. Initialize p1 = 0 (for warehouse_a) and p2 = 0 (for warehouse_b).
2. While p1 < len(warehouse_a) and p2 < len(warehouse_b):
   - If warehouse_a[p1] == warehouse_b[p2]:
       Found a common element -> append to common_elements.
       Increment both p1 and p2.
   - If warehouse_a[p1] < warehouse_b[p2]:
       warehouse_a's element is smaller, so advance p1 to catch up.
   - If warehouse_b[p2] < warehouse_a[p1]:
       warehouse_b's element is smaller, so advance p2 to catch up.
3. Return common_elements.

Complexity:
- Time Complexity: O(n + m) - Where n and m are lengths of the two arrays.
- Space Complexity: O(min(n, m)) - To store the output list.
================================================================================
"""

def find_common_products(warehouse_a: list[int], warehouse_b: list[int]) -> list[int]:
    common_elements = []
    p1 = 0
    p2 = 0

    while p1 < len(warehouse_a) and p2 < len(warehouse_b):
        if warehouse_a[p1] == warehouse_b[p2]:
            common_elements.append(warehouse_a[p1])
            p1 += 1
            p2 += 1
        elif warehouse_a[p1] < warehouse_b[p2]:
            p1 += 1
        else:
            p2 += 1

    return common_elements


if __name__ == "__main__":
    warehouse_a = [101, 105, 110, 120, 130, 150]
    warehouse_b = [100, 105, 115, 120, 140, 150]
    result = find_common_products(warehouse_a, warehouse_b)
    print(f"Warehouse A: {warehouse_a}")
    print(f"Warehouse B: {warehouse_b}")
    print(f"Common Product IDs: {result}")
