# The set of links already visited
visited = {"http :// example .com ", "http :// google . com ", "http :// test . com "}
# The list of links found on the current page
new_links = ["http :// google . com ", "http :// python .org ", "http :// example .com/about", "http :// test .com "]
a=set(new_links)
updated_links=visited.intersection(a)
print(updated_links)
