# ================================================================
#  SCENARIO
#  Two lab sections submit partner lists. You must merge them
#  alternately (A1, B1, A2, B2, …) and append leftovers.
#
#  LEARNING GOALS
#  • Index manipulation and while loops
#  • zip() and list concatenation
#
#  PROBLEM DESCRIPTION
#  Input: two lines of roll numbers.
#  Output: interleaved list printed twice (manual and zip()).
#
#  EXAMPLE
#     Input:
#       A1 A2 A3
#       B1 B2
#     Output:
#       A1 B1 A2 B2 A3
#       A1 B1 A2 B2 A3
# ================================================================

a = input("List A: ").split()
b = input("List B: ").split()

# TODO 1 – Manual merging with index counters.
merged_manual = []
# HINT: use i, j indices and alternate appends

# TODO 2 – Use zip() then append leftover elements.
merged_builtin = []
# HINT: for x,y in zip(a,b): out += [x,y]; then extend the remainder

print(" ".join(merged_manual))
print(" ".join(merged_builtin))

# REFLECTION:
# Which version took fewer lines but remained clear?
