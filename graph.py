import pygame

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def remove_node(self, node):
        # Remove node and connected edges
        self.nodes.remove(node)
        self.edges = [edge for edge in self.edges if node not in edge]

    def remove_edge(self, node1, node2):
        self.edges = [edge for edge in self.edges if edge != (node1, node2) and edge != (node2, node1)]

    def draw_edges(self, screen):
        for edge in self.edges:
            pygame.draw.line(screen, (255, 255, 255), 
                             (edge[0].x, edge[0].y), 
                             (edge[1].x, edge[1].y), 2)

    def get_node_at_pos(self, pos):
        for node in self.nodes:
            if node.is_clicked(pos):
                return node
        return None