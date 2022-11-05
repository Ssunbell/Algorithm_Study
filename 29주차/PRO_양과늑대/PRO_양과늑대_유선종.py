'''
아이디어 : dfs는 한번 정해진 길은 다시 되돌아오지 않으므로 되돌아오는 방법이 필요함
           이때, dfs 파라미터로 노드들을 담은 리스트(node)를 넣어줘서
           현재 자식 노드뿐만 아니라 방문해야하는 다른 노드들도 추가
'''

def dfs(idx, sheep, wolf, node, info):
    global answer, graph
    if info[idx] == 0:
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1
        
    if wolf >= sheep:
        return 
    
    node.extend(graph[idx])
    for n in node:
        dfs(n, sheep, wolf, [i for i in node if i != n], info)
    
def solution(info, edges):
    global answer, graph
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
    
    answer = 0
    dfs(0, 0, 0, [], info)
    
    return answer