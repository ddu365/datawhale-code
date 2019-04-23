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
        self._val = val
        self._adjacent = {}
        self.visited = False
        # self.previous = None
        # In_degree Count
        self._in_degree = 0
        # Out_degree Count
        self._out_degree = 0

    def add_neighbor(self, nbr, weight=0):
        self._adjacent[nbr] = weight

    def get_connections(self):
        return self._adjacent.keys()

    def get_vertex_val(self):
        return self._val

    def get_weight(self, nbr):
        return self._adjacent[nbr]

    # def set_previous(self, pre):
    #     self.previous = pre

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def get_in_degree(self):
        return self._in_degree

    def set_in_degree(self, in_degree):
        self._in_degree = in_degree

    def get_out_degree(self):
        return self._out_degree

    def set_out_degree(self, out_degree):
        self._out_degree = out_degree

    def __str__(self):
        return str(self._val) + ' adjacent: ' + str([v.get_vertex_val() for v in self._adjacent.keys()])


class Graph:
    def __init__(self, is_directed=False):
        self.vertex_dict = {}
        self.num_vertex = 0
        self.is_directed = is_directed

    def __iter__(self):
        return iter(self.vertex_dict.values())

    def add_vertex(self, val):
        self.num_vertex += 1
        new_vertex = Vertex(val)
        self.vertex_dict[val] = new_vertex
        return new_vertex

    def get_vertex(self, val):
        if val in self.vertex_dict:
            return self.vertex_dict[val]
        else:
            return None

    def add_edge(self, source, target, weight=0):
        if source not in self.vertex_dict:
            self.add_vertex(source)
        if target not in self.vertex_dict:
            self.add_vertex(target)

        self.vertex_dict[source].add_neighbor(self.vertex_dict[target], weight)
        if not self.is_directed:  # 无向图
            self.vertex_dict[target].add_neighbor(self.vertex_dict[source], weight)

        if self.is_directed:  # 只有有向图才记录顶点的入度与出度
            self.get_vertex(source).set_out_degree(self.get_vertex(source).get_out_degree() + 1)
            self.get_vertex(target).set_in_degree(self.get_vertex(target).get_in_degree() + 1)

    def get_vertices(self):
        return self.vertex_dict.keys()

    def get_edges(self):
        edges = []
        for u in self:
            for v in u.get_connections():
                u_val = u.get_vertex_val()
                v_val = v.get_vertex_val()
                edges.append((u_val, v_val, u.get_weight(v)))  # 无向图时(u,v,w)与(v,u,w)表示同一条边
        return edges

    # 参考图示 https://www.jianshu.com/p/70952b51f0c8
    def dfs_traverse(self, start):
        stack = [start]
        res = []
        while stack:
            v_node = stack.pop()
            if not v_node.get_visited():
                v_node.set_visited()
                res.append(v_node.get_vertex_val())
                for next_v_node in v_node.get_connections():
                    if not next_v_node.get_visited():
                        stack.append(next_v_node)
        return res

    # 参考图示 https://www.jianshu.com/p/70952b51f0c8
    def bfs_traverse(self, start):
        queue = [start]
        res = []
        while queue:
            v_node = queue.pop(0)
            if not v_node.get_visited():
                v_node.set_visited()
                res.append(v_node.get_vertex_val())
                for next_v_node in v_node.get_connections():
                    if not next_v_node.get_visited():
                        queue.append(next_v_node)
        return res

    # 拓扑排序是针对有向无环图(DAG)的一种排序
    # Kahn思想:
    # 不断的寻找有向图中没有前驱(入度为0)的顶点，将之输出。
    # 然后从有向图中删除所有以此顶点为尾的弧。
    # 重复操作，直至图空，或者找不到没有前驱的顶点为止
    def topo_kahn(self):
        kahn_out = []
        in_0 = []  # 入度为0的顶点
        for v_val in self.get_vertices():
            v_obj = self.get_vertex(v_val)
            if v_obj.get_in_degree() == 0:
                in_0.append(v_obj)
        while in_0:
            u_obj = in_0.pop()
            kahn_out.append(u_obj.get_vertex_val())
            for v_obj in u_obj.get_connections():
                v_obj.set_in_degree(v_obj.get_in_degree() - 1)
                if v_obj.get_in_degree() == 0:
                    in_0.append(v_obj)
        return kahn_out

    # 参考链接: https://blog.csdn.net/pandora_madara/article/details/26478385
    def topo_dfs(self):
        dfs_out = []

        def dfs(u_obj):
            for v_obj in u_obj.get_connections():
                if not v_obj.get_visited():
                    v_obj.set_visited()
                    dfs(v_obj)
            dfs_out.append(u_obj.get_vertex_val())

        for u_val in self.get_vertices():
            u_obj = self.get_vertex(u_val)
            if not u_obj.get_visited():
                u_obj.set_visited()
                dfs(u_obj)

        dfs_out.reverse()
        return dfs_out

    # 求给定源顶点src到各顶点的最短路径，也叫单源最短路径
    # 参考链接：
    # https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
    # https://wiki.jikexueyuan.com/project/easy-learn-algorithm/dijkstra.html
    def dijkstra(self, src):  # src  顶点对象
        pq = queue.PriorityQueue()
        dis = {v_val: float('inf') for v_val in self.get_vertices() if v_val != src.get_vertex_val()}
        dis[src.get_vertex_val()] = 0
        entry_lookup = {}
        for v, d in dis.items():
            entry = [d, v]
            entry_lookup[v] = entry
            pq.put(entry)

        while not pq.empty():
            u_val = pq.get()[1]
            u = self.get_vertex(u_val)
            for v in u.get_connections():
                v_val = v.get_vertex_val()
                if v_val in entry_lookup:
                    if dis[u_val] + u.get_weight(v) < dis[v_val]:
                        dis[v_val] = dis[u_val] + u.get_weight(v)
                        entry_lookup[v_val][0] = dis[v_val]
        return dis


if __name__ == '__main__':
    g = Graph(is_directed=True)  # is_directed=True
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'b', 2)
    g.add_edge('b', 'e', 4)
    g.add_edge('c', 'd', 4)
    g.add_edge('d', 'e', 4)


    # g.add_vertex('v1')
    # g.add_vertex('v2')
    # g.add_vertex('v3')
    # g.add_vertex('v4')
    # g.add_vertex('v5')
    # g.add_edge('v2', 'v1')
    # g.add_edge('v1', 'v5')
    # g.add_edge('v4', 'v2')
    # g.add_edge('v4', 'v5')
    # g.add_edge('v3', 'v1')
    # g.add_edge('v3', 'v5')

    # dfs时g的所有顶点已被访问过
    cp_bfs = copy.deepcopy(g)
    cp_dfs = copy.deepcopy(g)

    print(g.get_vertices())
    print(g.get_edges())

    print('[dfs]', g.dfs_traverse(g.get_vertex('a')))
    print('[bfs]', cp_bfs.bfs_traverse(cp_bfs.get_vertex('a')))
    print('[dijkstra]', g.dijkstra(g.get_vertex('a')))
    print('[topo_kahn]', g.topo_kahn())
    print('[topo_dfs]', cp_dfs.topo_dfs())
