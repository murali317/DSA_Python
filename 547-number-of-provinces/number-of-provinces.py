class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # time 
        c = 0
        n = len(isConnected)
        visited = [False] * n
        
        def dfs(i):
            visited[i] = True
            for neighbour in range(n):
                if isConnected[i][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                c += 1
        return c