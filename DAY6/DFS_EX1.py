
def dfs(graph, v, visited): # graph는 연결 정보, visited는 방문 노드
    visited[v] = True # 현재 노드를 방문 처리
    print('DFS 탐색 순서', [v], v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            print('방문 하지 않은 노드 발견 : ', graph[i])
            dfs(graph, i, visited)
graph =[
    [],
    [2,3],
    [1,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7,8],
    [6,8],
    [2,6,7]
    
]

visited = [False] * 9 # 초기  이후 체크된 부분 TRUE

# 정의된 DFS 함수 호출, 시작 노드 1
dfs(graph, 1, visited)