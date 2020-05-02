class Solution:
    def __init__(self, origin, incoming_edges, outgoing_edges):
        self.origin = origin
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges

    def output(self):
        ############### YOUR CODE GOES HERE ##################
        distance = {}
        predecessor = {}
        #print(self.outgoing_edges)
        for vertex in range(0, len(self.outgoing_edges)):
            distance[vertex] = float("inf")
            predecessor[vertex] = None

        distance[self.origin] = 0

        #print(self.outgoing_edges)
        for i in range(1, len(self.outgoing_edges) - 1):
            for node in range(len(self.outgoing_edges)):
                for edges in self.outgoing_edges[node]:
                    if distance[node] + self.outgoing_edges[node][edges] < distance[edges]:
                        distance[edges] = distance[node] + self.outgoing_edges[node][edges]
                        predecessor[edges] = node



        return list(distance.values())
