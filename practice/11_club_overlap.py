# ================================================================
#  SCENARIO
#  Two students compare their club memberships to plan a joint event.
#
#  LEARNING GOALS
#  • Nested loops and list membership
#  • Set operations (intersection and difference)
#
#  PROBLEM DESCRIPTION
#  Input: two comma-separated lines of club names.
#  Output: common | only_A | only_B (in one line).
#  Print twice (manual and sets).
#
#  EXAMPLE
#     Input:
#        Robotics, AI, Drama
#        AI, Music
#     Output:
#        AI|Drama,Robotics|Music
#        AI|Drama,Robotics|Music
# ================================================================

A = [x.strip() for x in input("Student A clubs: ").split(",") if x.strip()]
B = [x.strip() for x in input("Student B clubs: ").split(",") if x.strip()]

# TODO 1 – Manual loop comparisons.
common_manual, onlyA_manual, onlyB_manual = [], [], []
# HINT: build each list by checking membership in the other

# TODO 2 – Set operations.
common_builtin, onlyA_builtin, onlyB_builtin = [], [], []
# HINT: convert to sets; use &: intersection, -: difference

print(f"{','.join(sorted(common_manual))}|{','.join(sorted(onlyA_manual))}|{','.join(sorted(onlyB_manual))}")
print(f"{','.join(sorted(common_builtin))}|{','.join(sorted(onlyA_builtin))}|{','.join(sorted(onlyB_builtin))}")

# REFLECTION:
# How did sets change your thinking about the problem?
