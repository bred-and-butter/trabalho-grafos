from interfaces import VertexInterface, EdgeInterface
from dijkstra import Dijkstra

VertexInterface.interface_loop()
VertexInterface.print_vertexes()
EdgeInterface.interface_loop()
VertexInterface.print_adjacency_list()

print("Rodando dijkstra")

Dijkstra.run()
