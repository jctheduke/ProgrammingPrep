from Stack import MyStack
# do a depth first search  if you visit same node agian that indicates a cycle.

def detect_cycle(g):
    num_vertices = g.vertices
    visited = [False]*num_vertices

    result = detect_cycle_helper(g, 0, visited)
    if result:
        return True
    for i in range(num_vertices):
        if not visited[i]:
            result = detect_cycle_helper(g, i, visited)
            if result:
                return True
    return False


def detect_cycle_helper(g, source, visited):
    stack = MyStack()
    stack.push(source)
    visited[source] = True

    while(not stack.is_empty()):
        current_node = stack.pop()
        temp_node = g.array[current_node].head_node
        while(temp_node):
            print(temp_node.data, visited)
            if visited[temp_node.data]:
                return True
            else:
                stack.push(temp_node.data)
                visited[temp_node.data] = True
                temp_node = temp_node.next_element
    return False
