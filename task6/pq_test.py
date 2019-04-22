import queue

d = {'a': 0, 'b': 2, 'c': 5, 'd': 1}

pq = queue.PriorityQueue()

entry_lookup = {}

for v, d in d.items():
    entry = [d, v]
    entry_lookup[v] = entry
    pq.put(entry)

entry_lookup['d'][0] = 4

# pq.put([0, 'a'])
# pq.put([5, 'c'])
# pq.put([1, 'd'])
# pq.put([2, 'b'])


while not pq.empty():
    print(pq.get())

# for e in pq:
#     print(e)
