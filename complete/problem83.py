import sys
import heapq
import time

def dijkstra(G, start, end, start_cost = 0):
    q = [(start_cost, start, ())]  
    visited = set()      
    while True:
        cost, v1, path = heapq.heappop(q)
        if v1 not in visited:
            visited.add(v1)
            if v1 == end:
                return cost
            path = (v1, path)
            for (v2, cost2) in G[v1].iteritems():
                if v2 not in visited:
                    heapq.heappush(q, (cost + cost2, v2, path))

def matrix_to_graph(m):
    G = {}
    max_len = len(m)
    for x in range(max_len):
        for y in range(max_len):
            positions = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
            for px, py in positions:
                if px >= 0 and px < max_len and py >= 0 and py < max_len:
                    src = '%d_%d' % (x, y)
                    dst = '%d_%d' % (px, py)
                    cost = m[px][py]
                    G.setdefault(src, {})[dst] = cost
    return G

def main():
    s = time.time()
    matrix = [[int(i) for i in j.split(',')] for j in open(sys.argv[1])]
    g = matrix_to_graph(matrix)
    d = len(matrix) - 1
    last_vertex = '%d_%d' % (d, d)
    cost = dijkstra(g, '0_0', last_vertex, matrix[0][0])
    print('Shortest path len = %d Time (s) = %f' % (cost, time.time()-s))

if __name__ == '__main__':
    main()
