from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        
        for _ in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
    
    def add_edge(self, source, destination):
        if source < self.vertices and destination < self. vertices:
            self.array[source].insert_at_head(destination)
    
    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        print
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while(temp is not None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")
