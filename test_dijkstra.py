from interfaces import VertexInterface, EdgeInterface
from dijkstra import Dijkstra

VertexInterface.create_vertex(value="a")
VertexInterface.create_vertex(value="b")
VertexInterface.create_vertex(value="c")
VertexInterface.create_vertex(value="d")
VertexInterface.create_vertex(value="e")


a = VertexInterface.get_vertex(value="a")
b = VertexInterface.get_vertex(value="b")
c = VertexInterface.get_vertex(value="c")
d = VertexInterface.get_vertex(value="d")
e = VertexInterface.get_vertex(value="e")


EdgeInterface.connect_vertexes(weight=10, vertex1=a, vertex2=b, directed="s")
EdgeInterface.connect_vertexes(weight=4, vertex1=a, vertex2=c, directed="s")
EdgeInterface.connect_vertexes(weight=6, vertex1=a, vertex2=e, directed="s")
EdgeInterface.connect_vertexes(weight=7, vertex1=b, vertex2=d, directed="s")
EdgeInterface.connect_vertexes(weight=9, vertex1=b, vertex2=e, directed="s")
EdgeInterface.connect_vertexes(weight=1, vertex1=c, vertex2=e, directed="s")
EdgeInterface.connect_vertexes(weight=6, vertex1=c, vertex2=d, directed="s")
EdgeInterface.connect_vertexes(weight=3, vertex1=c, vertex2=b, directed="s")
EdgeInterface.connect_vertexes(weight=8, vertex1=d, vertex2=a, directed="s")


while True:
    Dijkstra.run()
