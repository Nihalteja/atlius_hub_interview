
def solution(root,start):
    from collections import defaultdict
    graph=defaultdict(list)
    def build(root,par):
        if not root:
            return
        if par:
            graph[root.val].append(par.val)
            graph[par.val].append(root.val)
        build(root.left,root)
        build(root.right,root)
    build(root,None)
    def bfs():
        from collections import deque
        queue=deque([start])
        visited=set()
        count=0
        while queue:
            for i in range(len(queue)):
                node=queue.popleft()
                visited.add(node)
                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            count+=1
        return count
    return bfs()-1