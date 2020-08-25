from Graph import Graph
from Queue import MyQueue
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.print_graph()


def bfs_traversal_helper(g, source, visited):
    result = ""
    queue = MyQueue()
    queue.enqueue(source)
    visited[source] = True

    while(not queue.is_empty()):
        current_node = queue.dequeue()
        result += str(current_node)
        temp = g.array[current_node].head_node
        while(temp is not None):
            if not visited[temp.data]:
                queue.enqueue(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited


def bfs_traversal(g, source):
    num_of_verices = g.vertices
    if num_of_verices == 0:
        return ""

    visited = [False]*num_of_verices
    result, visited = bfs_traversal_helper(g, source, visited)

    for i in range(num_of_verices):
        if not visited[i]:
            s_result, visited = bfs_traversal_helper(g, i, visited)
            result += s_result

    return result


print(bfs_traversal(g, 0))
