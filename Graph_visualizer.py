# -*- coding: utf-8 -*-

import pygame

pygame.init()
window = pygame.display.set_mode((700, 500))
window.fill((0, 0, 0))



red=(255, 0, 0)
white=(255,255,255)

edge_color=white

class Edge:
    def __init__(self, node1, node2):
        self.node1=node1
        self.node2=node2
    def pos1(self):
        return self.node1.pos
    def pos2(self):
        return self.node2.pos


class Node:
    def __init__(self, x, y, color, radius):
        self.pos = (x, y)
        self.x_boundary = (x - radius, x + radius)
        self.y_boundary = (y - radius, y + radius)
        self.color = color
        self.radius = radius
        self.edges=[]

    def recalc_boundary(self):
        self.x_boundary = (
            self.pos[0] - self.radius, self.pos[0] + self.radius
        )
        self.y_boundary = (
            self.pos[1] - self.radius, self.pos[1] + self.radius
        )
    def add_edge(self):
        
        return
        
def mouse_in_node():
    pos = pygame.mouse.get_pos()
    selected_node=None
    index=None
    for i,node in enumerate(nodes):
        if (within(pos[0], *node.x_boundary) and within(pos[1], *node.y_boundary)):
            selected_node=node
            index=i
    return selected_node,index


nodes = []



within = lambda x, low, high: low <= x <= high


selected = False
i=-1
selected_node=None

last_pos=None
drawing_edge=False

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not selected_node and event.button == 1:
            pos = pygame.mouse.get_pos()
            selected_node,index=mouse_in_node()
                        
            if not selected_node:
                nodes.append(Node(pos[0], pos[1], red, 10))
            
        elif event.type==pygame.KEYDOWN:
            pos = pygame.mouse.get_pos()                
            node1,index=mouse_in_node()
            if node1:
                last_pos=pos
                    
        elif event.type==pygame.MOUSEMOTION and last_pos:
            current_pos = pygame.mouse.get_pos()                
            drawing_edge=True

        elif event.type==pygame.KEYUP:
            node2,index=mouse_in_node()
            if node1 and node2:
                new_edge=Edge(node1,node2)
                node1.edges.append(new_edge)
                node2.edges.append(new_edge)
            last_pos=None
            drawing_edge=False
            
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_node=None
            
        
            
    if selected_node:
        selected_node.pos = pygame.mouse.get_pos()
        selected_node.recalc_boundary()
        
    window.fill((0, 0, 0))
    if drawing_edge:
        pygame.draw.line(window, red, last_pos, current_pos, 1)

    for i,node in enumerate(nodes):
        pygame.draw.circle(
            window, node.color,
            node.pos,
            node.radius
        )
        for e,edge in enumerate(node.edges):
            pygame.draw.line(window, edge_color, edge.pos1(), edge.pos2(), 1)
    
    
    pygame.display.update()