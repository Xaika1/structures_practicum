from collections import deque
def count_islands_dfs(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        while stack:
            cr, cc = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                dfs(r, c)
    return count


def count_islands_bfs(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited[r][c] = True
        while q:
            cr, cc = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if not visited[nr][nc] and grid[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                bfs(r, c)
    return count


def test_islands():
    g1 = [
        [1, 1, 0, 0],
        [1, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ]
    assert count_islands_dfs(g1) == 3
    assert count_islands_bfs(g1) == 3

    g2 = [
        [1, 1],
        [1, 1],
    ]
    assert count_islands_dfs(g2) == 1
    assert count_islands_bfs(g2) == 1

    g3 = [
        [0, 0],
        [0, 0],
    ]
    assert count_islands_dfs(g3) == 0
    assert count_islands_bfs(g3) == 0

    g4 = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]
    assert count_islands_dfs(g4) == 5
    assert count_islands_bfs(g4) == 5

    g5 = []
    assert count_islands_dfs(g5) == 0
    assert count_islands_bfs(g5) == 0

    g6 = [[1]]
    assert count_islands_dfs(g6) == 1
    assert count_islands_bfs(g6) == 1

    print("Все тесты задачи 'Острова' пройдены успешно!")


if __name__ == "__main__":
    test_islands()
