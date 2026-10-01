# 🏢 Problem 4 — Warehouse Container Capacity
# You're working on a warehouse system. Several vertical barriers are placed along a storage area, and their heights are represented by:
# heights = [3, 1, 2, 5, 4, 8, 2]
# Choose two barriers that can hold the maximum amount of material between them.
# The capacity between two barriers is:
# capacity = shorter barrier × distance between barriers
# Example
# If you choose:
# height 3 at index 0
# height 8 at index 5
# then:
# shorter height = 3
# distance = 5 - 0 = 5
#
# capacity = 3 × 5 = 15
# Your task

heights = [3, 1, 2, 5, 4, 8, 2]
l_height = 0
r_height = len(heights) - 1
max_capacity = 0

while l_height < r_height:
    min_height_wall = min(heights[l_height], heights[r_height])
    distance = r_height - l_height
    capacity = min_height_wall * distance
    max_capacity = max(max_capacity, capacity)
    # pointers moving now
    if heights[l_height] < heights[r_height]:
        # Move left pointer
        l_height += 1
    elif heights[r_height] < heights[l_height]:
        # Move Right pointer
        r_height -= 1
    elif heights[r_height] == heights[l_height]:
        l_height += 1

print(f"The Maximum water contains: {max_capacity}")

# Write a Two Pointers solution.
# Rules
# Start with left at the beginning.
# Start with right at the end.
# Don't use nested loops.
# Don't sort the array.
# Find the maximum capacity.

# Step1: first na approach is nenu first starting value leftheight ki assign chesina heights ane list lo
# Step2: second vachesi last index right height ki assign chesina
# Step3: and oka variable create chesina dani peru max_capacity
# Step4: and loop condition cesina endhi ante left height pointer index is eppudu right pointer kanna thakuva vundali
# Step5: after that manaki small wall kavali 2 walls lo endhukante 2 walls vunnai okati chinnadi and okati peddadi manamu peddha wall tesukonte water padipothai so anduke okati peddawall and okati chinna wall vunnappudu manam chinna wall tesukovali
# Step6: and tharuvatha manam a heights okka index calculate cheyali nenu distance ane variable tesukunnanu then indexes calculate chesinanu ela ante eppudu manamu ekkuva vunde index - thakuvva vunte index e calculate cheyali
# Step7: and capacity ane variable tesukoni nenu height * distance calculate chesthe width vasthundi ade manam capacity antam e program lo
# Step8: so ikkada nenu max capacity calculate chesthanu e dantlo ekkuva nellu padathayo adhi tesukuntanu.
# Step9: ippudu pointers i move cheyali ela ante a wall height takkuva vunte a wall move cheyali (meaning enti ante ippudu left variable value low ga vunte right kanna manamu left move chestham ade right thakuva vunte right move chestham and 2ndu wallsu equal ga vunte manam edo okati move chesthamu.)
# Step10: inka manamu a maximum capacity container ni print chesthamu anthe ingga ipoindhi problem.


# Time and Space Complexity:
# Time Complexity : O(n) -> Linear because we used only single loop
# Space Complexity: O(1) -> Constant because we use one variable that stores only one value
