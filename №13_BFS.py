from collections import deque


class GraphAdjMatrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v, undirected=True):
        self.matrix[u][v] = 1
        if undirected:
            self.matrix[v][u] = 1

    def neighbors(self, u):
        return [v for v in range(self.n) if self.matrix[u][v] == 1]


class GraphAdjList:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v, undirected=True):
        self.adj[u].append(v)
        if undirected:
            self.adj[v].append(u)

    def neighbors(self, u):
        return self.adj[u]


def bfs(graph, start):
    n = graph.n
    visited = [False] * n
    order = []
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.neighbors(u):
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return order


def dfs(graph, start):
    n = graph.n
    visited = [False] * n
    order = []

    def _dfs(u):
        visited[u] = True
        order.append(u)
        for v in graph.neighbors(u):
            if not visited[v]:
                _dfs(v)

    _dfs(start)
    return order


def shortest_path_unweighted(graph, start, target):
    n = graph.n
    visited = [False] * n
    parent = [-1] * n
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        u = q.popleft()
        if u == target:
            break
        for v in graph.neighbors(u):
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    if not visited[target]:
        return None

    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


def test_graphs():
    n = 6
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 3),
        (3, 4),
        (4, 5),
    ]

    g_mat = GraphAdjMatrix(n)
    g_list = GraphAdjList(n)

    for u, v in edges:
        g_mat.add_edge(u, v)
        g_list.add_edge(u, v)

    bfs_mat = bfs(g_mat, 0)
    bfs_list = bfs(g_list, 0)
    assert bfs_mat == bfs_list

    dfs_mat = dfs(g_mat, 0)
    dfs_list = dfs(g_list, 0)
    assert dfs_mat == dfs_list

    path_mat = shortest_path_unweighted(g_mat, 0, 5)
    path_list = shortest_path_unweighted(g_list, 0, 5)
    assert path_mat == path_list
    assert path_mat in ([0, 1, 3, 4, 5], [0, 2, 3, 4, 5])

    assert shortest_path_unweighted(g_mat, 5, 0) in ([5, 4, 3, 1, 0], [5, 4, 3, 2, 0])
    assert shortest_path_unweighted(g_list, 5, 0) in ([5, 4, 3, 1, 0], [5, 4, 3, 2, 0])

    g_disconnected = GraphAdjList(4)
    g_disconnected.add_edge(0, 1)
    assert shortest_path_unweighted(g_disconnected, 0, 3) is None

    print("Все тесты графов пройдены успешно!")


if __name__ == "__main__":
    test_graphs()
