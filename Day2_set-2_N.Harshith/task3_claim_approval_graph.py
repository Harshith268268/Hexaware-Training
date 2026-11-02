"""SET 2 TASK 3: Directed approval graph, BFS shortest path and DFS cycle detection."""
from collections import deque
GRAPH={"Registration":["Assessment"],"Assessment":["Surveyor","Settlement"],
       "Surveyor":["Settlement"],"Settlement":[]}

def bfs(graph,start,end):
    if start not in graph or end not in graph: return None
    q=deque([[start]]); visited={start}
    while q:
        path=q.popleft(); node=path[-1]
        if node==end: return path
        for nxt in graph.get(node,[]):
            if nxt not in visited:
                visited.add(nxt); q.append(path+[nxt])
    return None

def directed_cycle(graph):
    state={node:0 for node in graph}; stack=[]
    def visit(node):
        state[node]=1; stack.append(node)
        for nxt in graph.get(node,[]):
            if nxt not in state: state[nxt]=0
            if state[nxt]==1:
                i=stack.index(nxt); return stack[i:]+[nxt]
            if state[nxt]==0:
                found=visit(nxt)
                if found: return found
        stack.pop(); state[node]=2
        return None
    for node in graph:
        if state[node]==0:
            found=visit(node)
            if found: return found
    return None

if __name__=="__main__":
    print("SET 2 - TASK 3: CLAIM APPROVAL GRAPH")
    for stage,edges in GRAPH.items(): print(stage,"->",", ".join(edges) if edges else "END")
    path=bfs(GRAPH,"Registration","Settlement")
    print("BFS shortest path:", " -> ".join(path) if path else "No path")
    print("Transitions:",len(path)-1 if path else 0)
    print("Cycle in approval graph:",directed_cycle(GRAPH) or "NO CYCLE")
    print("Cycle test A-B-C-A:",directed_cycle({"A":["B"],"B":["C"],"C":["A"]}))
    print("Empty graph test:",directed_cycle({}))
