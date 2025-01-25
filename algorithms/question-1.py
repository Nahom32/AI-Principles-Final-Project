class UnweightedSearch:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
    def iterator(self, strategy='BFS'):
        queue = [(self.start, [self.start])]
        visited = set()
        while queue:
            curr_node, curr_path = queue.pop(0) if strategy == 'BFS' else queue.pop()
            if curr_node == self.end:
                return curr_path
            else:
                for i in self.graph[curr_node]:
                    if i not in visited:
                        queue.append((i, curr_path + [i]))
        return []
    

        

        