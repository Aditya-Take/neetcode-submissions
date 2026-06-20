class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque

        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        m,n = len(heights), len(heights[0])

        for j in range(n):
            p_que.append((0,j))
            p_seen.add((0,j))
        
        for i in range(1,m):
            p_que.append((i,0))
            p_seen.add((i,0))
        
        for i in range(m):
            a_que.append((i,n-1))
            a_seen.add((i,n-1))
        
        for j in range(n-1):
            a_que.append((m-1,j))
            a_seen.add((m-1,j))

        def ans(que,seen):
            while que:
                x,y = que.popleft()
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    r,c = x + i, y + j
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[x][y] and (r,c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))
        ans(p_que,p_seen)
        ans(a_que,a_seen)

        return list((p_seen.intersection(a_seen)))