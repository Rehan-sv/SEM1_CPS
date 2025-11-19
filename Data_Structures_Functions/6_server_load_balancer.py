def distribute_tasks(server_loads, new_tasks):
    for _ in range(new_tasks):
        min_index = server_loads.index(min(server_loads))
        server_loads[min_index] += 1
    return server_loads

server_loads = [10, 5, 2, 8]
new_tasks = 5
print(distribute_tasks(server_loads, new_tasks))
# Expected: [10, 6, 6, 8]