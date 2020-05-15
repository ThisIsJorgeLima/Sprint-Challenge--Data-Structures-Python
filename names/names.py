# Task 2. Runtime Optimization

# (Hint: You might try importing a data structure you built during the week)

import time
from binary_search_tree import BSTNode


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
However, you can and should use the provided duplicates list to return your solution.
"""
duplicates = []  # Return the list of duplicates in this data structure

##********Note*********##
###***comment in/out***###
##*****^Above^********##
#**disregard error below **##
##**runs fine in terminal**##

# Replace the nested for loops below with your improvements
# for name_1 in names_1: # O(n)
#     for name_2 in names_2:
#         if name_1 == name_2: # O(n)
#             duplicates.append(name_1)

# Use Binary Search Tree:
# initally used 'names' as root buy using blank space to make it faster
"""
The current runtime of the starter code has nested for loops, which makes our inner loop run each time.

Our outer loop is running, and they are the same length of (10,000), we are looking at O(n^2).

By implementing our Binary Search Tree, it has an O(log n) time complexity.


Since it is eliminating half of our tree and or subtree as it continues to search.

We, Will, be adding duplicates to our list; it will depend on how many duplicates there are and which size of the input is so its feasible that it would make an O(n log n).

"""

# bst = BSTNode(names_2[0])
# for name_2 in names_2[1:]:
#     bst.insert(name_2)

# for name_1 in names_1:
#     if bst.contains(name_1):
#         duplicates.append(name_1)

"""
A lot faster:
"""
# duplicates = list(names_1.intersection(names_2))
"""
 Using the intersection method returns set containing only items that exist in both sets,  or all sets if the comparison is done with more than two sets.
"""
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
