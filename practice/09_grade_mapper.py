# ================================================================
#  SCENARIO
#  The department office wants quick grade conversions for reports.
#
#  LEARNING GOALS
#  • if/elif decision structures
#  • Dictionary look-ups
#
#  PROBLEM DESCRIPTION
#  Read an integer mark (0–100).
#  Output the letter grade twice (manual and dict-based).
#  Use standard scale: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60 else F.
#
#  EXAMPLE
#     Input: 83
#     Output: B
#             B
# ================================================================

mark = int(input("Enter mark: "))

# TODO 1 – Manual if/elif ladder.
grade_manual = ""

# TODO 2 – Dict lookup based on decade (mark//10).
grade_builtin = ""
# HINT: table = {10:'A', 9:'A', 8:'B', 7:'C', 6:'D'}; default 'F'

print(grade_manual)
print(grade_builtin)

# REFLECTION:
# Which version will be easier to update if bands change?
