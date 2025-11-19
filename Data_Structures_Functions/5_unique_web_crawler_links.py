def update_visited_links(visited_links_set, new_links_list):
    initial_size = len(visited_links_set)
    for link in new_links_list:
        visited_links_set.add(link)
    new_links_count = len(visited_links_set) - initial_size
    return visited_links_set, new_links_count

visited = {'http://example.com', 'http://google.com',
           'http://example.com/about'}
new_links = ['http://google.com', 'http://python.org',
             'http://test.com']

# Sample Output
print(update_visited_links(visited, new_links))
# Expected Output:
# ({'http://google.com', 'http://python.org', 'http://example.com', 'http://example.com/about', 'http://test.com'}, 2) or any variant with the same set and count