# Day 3 — Problem 4: Common Product IDs
# Two warehouses have their product IDs in sorted order:
# warehouse_a = [101, 105, 110, 120, 130, 150]
# warehouse_b = [100, 105, 115, 120, 140, 150]
# Find the product IDs that exist in both warehouses.
# Expected result:
# [105, 120, 150]
# Rules
# Use two pointers
# One pointer for each list
# No nested loops
# Don't use set()

warehouse_a = [101, 105, 110, 120, 130, 150]
warehouse_b = [100, 105, 115, 120, 140, 150]

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
    elif warehouse_b[p2] < warehouse_a[p1]:
        p2 += 1

print(common_elements)

# Time and Space Complexity:
# Time Complexity: O(n + m) - Where n and m are lengths of the lists
# Space Complexity: O(min(n, m)) - List to store common elements
