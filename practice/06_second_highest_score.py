# ================================================================
#  SCENARIO
#  During a sports event you must announce Gold and Silver winners.
#  You already know how to find the highest.  Now find the second.
#
#  LEARNING GOALS
#  • Conditional logic and variable tracking
#  • Sorting lists and indexing
#
#  PROBLEM DESCRIPTION
#  Read a line of integers (scores).
#  Output the second-highest score twice (manual vs. sorted()).
#  If all scores are equal, print that value.
#
#  EXAMPLE
#     Input:  10 50 40 50
#     Output: 50
#             50
# ================================================================

scores = list(map(int, input("Enter scores: ").split()))

# TODO 1 – Manual: track largest and second largest.
second_manual = 0
# HINT: iterate and update 'largest' and 'second'

# TODO 2 – Built-in: sort descending and pick the second distinct value.
second_builtin = 0
# HINT: sorted(scores, reverse=True)

print(second_manual)
print(second_builtin)

# REFLECTION:
# Which method handles ties more reliably? Why?
