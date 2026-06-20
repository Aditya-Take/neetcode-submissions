class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        if not grid or not grid[0]:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        goodfruits = 0

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    goodfruits += 1
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        time = 0
        while q:
            r,c,minute = q.popleft()
            time = minute
            for dr,dc in directions:
                nr,nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc,minute + 1))
                    goodfruits -= 1
        
        return time if goodfruits == 0 else -1

        