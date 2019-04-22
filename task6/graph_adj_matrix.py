"""
图的分类:
按边是否有方向可分为有向图和无向图
按边是否有权重可分为有权图和无权图
图的表示:
邻接表: 将所有与图中某个顶点u相连的顶点依此表示出来 [无需事先指定顶点数]
邻接矩阵: 一维数组存储图的顶点信息，二维数组(邻接矩阵)存储顶点间边的信息 [需事先指定顶点数]
"""
import copy
import queue

class Vertex:
    def __init__(self, val):
        self.val = val
        # Mark all nodes unvisited
        self.visited = False

    def get_vertex_val(self):
        return self.val

    def set_vertex_val(self, val):
        self.val = val

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def __str__(self):
        return str(self.val)


class Graph:
    def __init__(self, num_vertex, is_directed=False):
        self.is_directed = is_directed
        self.adj_matrix = [[-1] * num_vertex for _ in range(num_vertex)]
        self.num_vertex = num_vertex
        self.vertices = []
        for i in range(0, self.num_vertex):
            self.vertices.append(Vertex(i))

    def set_vertex(self, v_idx, v_val):
        if 0 <= v_idx < self.num_vertex:
            self.vertices[v_idx].set_vertex_val(v_val)
        else:
            raise IndexError('index out of the range')

    def get_vertex_idx(self, v_val):
        for v_idx in range(0, self.num_vertex):
            if v_val == self.vertices[v_idx].get_vertex_val():
                return v_idx
        return -1

    def get_vertex(self, v_idx):
        if not 0 <= v_idx < self.num_vertex:
            raise IndexError('index out of the range')
        return self.vertices[v_idx]

    def add_edge(self, source, target, weight=0):
        if self.get_vertex_idx(source) != -1 and self.get_vertex_idx(target) != -1:
            self.adj_matrix[self.get_vertex_idx(source)][self.get_vertex_idx(target)] = weight
            if not self.is_directed:  # 无向图
                self.adj_matrix[self.get_vertex_idx(target)][self.get_vertex_idx(source)] = weight

    def get_edges(self):
        edges = []
        for u_idx in range(0, self.num_vertex):
            for v_idx in range(0, self.num_vertex):
                if self.adj_matrix[u_idx][v_idx] != -1:
                    u_val = self.vertices[u_idx].get_vertex_val()
                    v_val = self.vertices[v_idx].get_vertex_val()
                    edges.append((u_val, v_val, self.adj_matrix[u_idx][v_idx]))
        return edges

    def get_vertices(self):
        vertices = []
        for v_idx in range(0, self.num_vertex):
            vertices.append(self.vertices[v_idx].get_vertex_val())
        return vertices

    def print_matrix(self):
        for u_idx in range(0, self.num_vertex):
            row = []
            for v_idx in range(0, self.num_vertex):
                row.append(self.adj_matrix[u_idx][v_idx])
            print(row)

    def dfs_traverse(self, start):
        stack = [start]
        res = []
        while stack:
            v_node = stack.pop()
            if not v_node.get_visited():
                v_node.set_visited()
                res.append(v_node.get_vertex_val())
                v_node_idx = self.get_vertex_idx(v_node.get_vertex_val())
                for target_idx in range(0, self.num_vertex):
                    if self.adj_matrix[v_node_idx][target_idx] != -1 and v_node_idx != target_idx:
                        stack.append(self.get_vertex(target_idx))
        return res

    def bfs_traverse(self, start):
        queue = [start]
        res = []
        while queue:
            v_node = queue.pop(0)
            if not v_node.get_visited():
                v_node.set_visited()
                res.append(v_node.get_vertex_val())
                v_node_idx = self.get_vertex_idx(v_node.get_vertex_val())
                for target_idx in range(0, self.num_vertex):
                    if self.adj_matrix[v_node_idx][target_idx] != -1 and v_node_idx != target_idx:
                        queue.append(self.get_vertex(target_idx))
        return res

    # 求给定源顶点src到各顶点的最短路径，也叫单源最短路径
    # 参考链接：
    # https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
    # https://wiki.jikexueyuan.com/project/easy-learn-algorithm/dijkstra.html
    def dijkstra(self, src):  # src  顶点对象
        pq = queue.PriorityQueue()
        dis = {self.get_vertex(idx).get_vertex_val(): float('inf') for idx in range(0, self.num_vertex) \
               if self.get_vertex(idx).get_vertex_val() != src.get_vertex_val()}
        dis[src.get_vertex_val()] = 0
        entry_lookup = {}
        for v, d in dis.items():
            entry = [d, v]
            entry_lookup[v] = entry
            pq.put(entry)

        while not pq.empty():
            u_val = pq.get()[1]
            u_idx = self.get_vertex_idx(u_val)
            for target_idx in range(0, self.num_vertex):
                target_val = self.get_vertex(target_idx).get_vertex_val()
                if self.adj_matrix[u_idx][target_idx] != -1 and target_val in entry_lookup:
                    if dis[u_val] + self.adj_matrix[u_idx][target_idx] < dis[target_val]:
                        dis[target_val] = dis[u_val] + self.adj_matrix[u_idx][target_idx]
                        entry_lookup[target_val][0] = dis[target_val]
        return dis


if __name__ == '__main__':
    g = Graph(5)  # , is_directed=True
    g.set_vertex(0, 'a')
    g.set_vertex(1, 'b')
    g.set_vertex(2, 'c')
    g.set_vertex(3, 'd')
    g.set_vertex(4, 'e')
    print(g.get_vertices()) 
    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'b', 2)
    g.add_edge('b', 'e', 4)
    g.add_edge('c', 'd', 4)
    g.add_edge('d', 'e', 4)

    # dfs时g的所有顶点已被访问过
    cp_g = copy.deepcopy(g)

    g.print_matrix()
    print(g.get_edges())

    print('[dfs]', g.dfs_traverse(g.get_vertex(0)))
    print('[bfs]', cp_g.bfs_traverse(cp_g.get_vertex(0)))
    print('[dijkstra]', g.dijkstra(g.get_vertex(0)))


