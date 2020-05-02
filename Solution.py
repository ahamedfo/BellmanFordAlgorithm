class Solution:
    def __init__(self, origin, incoming_edges, outgoing_edges):
        self.origin = origin
        self.incoming_edges = incoming_edges
        self.outgoing_edges = outgoing_edges

    def output(self):
        ############### YOUR CODE GOES HERE ##################
        distance = {}
        predecessor = {}
        print(self.outgoing_edges)
        for vertex in range(0, self.outgoing_edges):
            distance[vertex] = float("inf")
            predecessor[vertex] = None

        distance[self.origin] = 0
        print(self.outgoing_edges)
        for i in range(1, len(self.outgoing_edges_edges) - 1):
            curNode = self.outgoing_edges[i]
            for edges in curNode:
                if distance[i] + curNode[edges] < distance[edges]:
                    distance[edges] := distance[i] + curNode[edges]
                # if distance[i] +

        return [] #Return empty
