import heapq

# Heap queue algorithm (a.k.a. priority queue).
# Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k, counting elements from 0. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that a[0] is always its smallest element.

# Usage:

# heap = [] creates an empty heap 
# heappush(heap, item) pushes a new item on the heap 
# item = heappop(heap) pops the smallest item from the heap 
# item = heap[0] smallest item on the heap without popping it 
# heapify(x) transforms list into a heap, in-place, in linear time 
# item = heapreplace(heap, item) pops and returns smallest item, and adds new item; 
# the heap size is unchanged

# Our API differs from textbook heap algorithms as follows:

# We use 0-based indexing. This makes the relationship between the index for a node and the indexes for its children slightly less obvious, but is more suitable since Python uses 0-based indexing.
# Our heappop() method returns the smallest item, not the largest.
# These two make it possible to view the heap as a regular Python list
# without surprises: heap[0] is the smallest item, and heap.sort() maintains the heap invariant!


def djikstra(graph, start):
    
    NeighborsDist={}
    for Router in graph:            
        NeighborsDist[Router]=float('inf')                 
    
    NeighborsDist[start] = 0
    temp = [(0, start)]

    while len(temp) > 0:
        distance, router = heapq.heappop(temp)
        if distance > NeighborsDist[router]:
            continue

        for neighbor, weight in graph[router]:
            new_dist = distance + weight
            
            if new_dist < NeighborsDist[neighbor]:
                NeighborsDist[neighbor] = new_dist
                heapq.heappush(temp, (new_dist, neighbor))

    return NeighborsDist

if __name__=="__main__":
    graph = {
            'R1': [('R2', 2), ('R3', 5), ('R4', 1)],
            'R2': [('R1', 2), ('R4', 2), ('R3', 3)],
            'R3': [('R2', 3), ('R1', 5), ('R4', 3), ('R5', 1), ('R6', 5)],
            'R4': [('R1', 1), ('R2', 2), ('R3', 3), ('R5', 1)],
            'R5': [('R4', 1), ('R3', 1), ('R6', 1)],
            'R6': [('R3', 5), ('R5', 1)],
        }

    actual = djikstra(graph, 'R4')
    print(actual)