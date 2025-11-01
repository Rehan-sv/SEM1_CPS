# ================================================================
#  SCENARIO
#  The class rep combines attendance from multiple sheets.
#  Some names repeat.  Keep only the first occurrence.
#
#  LEARNING GOALS
#  • Lists and membership testing
#  • Dict keys as an ordered de-duplication technique
#
#  PROBLEM DESCRIPTION
#  Input: space-separated names
#  Output: names with duplicates removed, in original order.
#  Print twice (manual loop vs. dict.fromkeys()).
#
#  EXAMPLE
#     Input:   ravi anu ravi teja anu
#     Output:  ravi anu teja
#              ravi anu teja
# ================================================================

names = input("Enter names: ").split()

# TODO 1 – Manual removal using a “seen” list.
unique_manual = []
# HINT: for each name, if not already in a 'seen' list, append to both

# TODO 2 – Built-in method using dict.fromkeys().
unique_builtin = []

print(" ".join(unique_manual))
print(" ".join(unique_builtin))

# REFLECTION:
# Which approach would you prefer for long lists? Why?
