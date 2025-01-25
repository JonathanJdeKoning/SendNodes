import pygame
import sys
from node import Node
from graph import Graph
from ui import Sidebar

# Screen dimensions
WIDTH = 1200
HEIGHT = 800
SIDEBAR_WIDTH = 200

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Draggable Node Graph")
    clock = pygame.time.Clock()

    graph = Graph()
    sidebar = Sidebar(WIDTH - SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, HEIGHT)

    selected_node = None
    edge_start_node = None
    edge_mode = False

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Node/Edge Creation via Sidebar
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if sidebar.is_clicked(mouse_pos):
                    button = sidebar.get_button(mouse_pos)
                    if button == "Add Node":
                        new_node = Node(mouse_pos[0], mouse_pos[1])
                        graph.add_node(new_node)
                    elif button == "Add Edge":
                        edge_mode = not edge_mode

            # Node Selection and Dragging
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not sidebar.is_clicked(mouse_pos):
                clicked_node = graph.get_node_at_pos(mouse_pos)
                
                # Edge Creation
                if edge_mode and clicked_node:
                    if not edge_start_node:
                        edge_start_node = clicked_node
                    else:
                        graph.add_edge(edge_start_node, clicked_node)
                        edge_start_node = None
                        edge_mode = False
                
                # Node Selection
                elif clicked_node:
                    selected_node = clicked_node
                    selected_node.selected = True

            # Node Dragging
            if event.type == pygame.MOUSEMOTION and selected_node:
                selected_node.move(event.rel[0], event.rel[1])

            # Node/Edge Deselection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if selected_node:
                    selected_node.selected = False
                selected_node = None

            # Node/Edge Deletion
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                clicked_node = graph.get_node_at_pos(mouse_pos)
                if clicked_node:
                    graph.remove_node(clicked_node)

        # Hover Detection
        for node in graph.nodes:
            node.hover = node.is_clicked(mouse_pos)

        # Drawing
        screen.fill((50, 50, 50))
        graph.draw_edges(screen)
        
        for node in graph.nodes:
            node.draw(screen)
        
        sidebar.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()