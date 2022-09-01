from interfaces import VertexInterface, EdgeInterface
from dijkstra import Dijkstra

VertexInterface.interface_loop()
VertexInterface.print_vertexes()
EdgeInterface.interface_loop()
VertexInterface.print_adjacency_list()

choice = "s"

while choice == "s":
    print("Rodar Dijkstra?(s/n)")
    choice = input()

    Dijkstra.run()
