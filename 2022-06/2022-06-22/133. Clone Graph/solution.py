# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None

        if len(node.neighbors) == 0:
            return Node(node.val)

        visited = {node: Node(node.val, [])}
        dfs = [node]

        while len(dfs) > 0:
            peek = dfs[-1]
            peek_copy = visited[peek]

            if len(peek_copy.neighbors) == 0:
                for neighbor in peek.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val, [])
                        dfs.append(neighbor)

                    peek_copy.neighbors.append(visited[neighbor])
            else:
                dfs.pop()

        return visited[node]
