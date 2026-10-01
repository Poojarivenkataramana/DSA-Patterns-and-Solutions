# 🔥 Problem 3 — Payment Processing System
# A payment system stores transaction values:
# transactions = [0, 150, 0, 200, 350, 0, 500]
# Here:
# 0 = failed/empty transaction
# The system wants all valid transactions at the beginning and all 0s at the end.
# Expected:
# [150, 200, 350, 500, 0, 0, 0]
# Rules:
# Modify the existing array in-place
# Don't create another array
# Don't use remove()
# Don't use sort()
# Use Two Pointers

transactions = [0, 150, 0, 200, 350, 0, 500]
f = 0
s = 0

while f < len(transactions):
    if transactions[f] == 0:
        f += 1
    elif transactions[f] != 0:
        transactions[s], transactions[f] = transactions[f], transactions[s]
        f += 1
        s += 1

print(transactions)

# Approach: First I initialize the fast and slow pointers at the same direction and same index.
# Why same index: -> because here we didn't compare adjacent elements we are just checking the element is itself is a zero
# if zero move one stem here the element checking/seeing nonzero elements is fast and slow is just places at the nonzero place
# so whenever we found nonzero we swap with zero and move both pointers until fast reach transactions length.

# Time and Space Complexity:
# Time Complexity is: O(n) Linear
# Space Complexity is: O(1) constant
