# ================================================================
#  SCENARIO
#  The library tags book summaries. You need to count how often
#  each word appears to propose suitable keywords.
#
#  LEARNING GOALS
#  • Dictionaries and counting patterns
#  • Manual search vs. dict.get()
#
#  PROBLEM DESCRIPTION
#  Input: a line of words (space-separated).
#  Output: each word and its count, alphabetically.
#  Print results twice (manual loop and dictionary).
#
#  EXAMPLE
#     Input:  data data is fun fun
#     Output:
#        data 2
#        fun 2
#        is 1
#        data 2
#        fun 2
#        is 1
# ================================================================

words = input("Enter words: ").split()

# TODO 1 – Manual counting (no dicts): build lists of unique words and counts.
freq_manual_words = []
freq_manual_counts = []
# HINT: search for the word; if found increment, else append new with count 1

# TODO 2 – Use dict.get() for counting.
freq_builtin = {}
# HINT: for w in words: freq_builtin[w] = freq_builtin.get(w, 0) + 1

# TODO 3 – Print sorted results for both.
# HINT: build pairs and sort by word before printing
