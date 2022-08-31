from interfaces import VertexInterface, EdgeInterface
from definitions import Vertex, Edge


class Dijkstra:
    def run():
        print("Escolha o vértice de partida:")
        value = input()

        start = VertexInterface.get_vertex(value)

        PathTable.init_SPD(start)
        UnvisitedList.init_checked_list()

        #Dijkstra.begin_recursion(start)
        print(Dijkstra.find_smallest_edge(start))

    def recurse_through_vertexes(vertex: Vertex):
        pass

    def find_smallest_edge(vertex: Vertex) -> Edge | None:
        smallest: Edge = None

        for edge in vertex.edges:
            if smallest == None or edge.weight < smallest.weight:
                if UnvisitedList.is_unvisited(edge.destination):
                    smallest = edge

        return smallest


class PathTable:
    __shortest_path_dict: dict = {}

    def init_SPD(start: Vertex):
        for vertex in VertexInterface.vertex_list:
            if vertex == start:
                PathTable.__shortest_path_dict[vertex] = 0
            else:
                PathTable.__shortest_path_dict[vertex] = None

    def show_paths():
        for path in PathTable.__shortest_path_dict:
            print(path)

    def update_path(vertex: Vertex):
        pass


class UnvisitedList:
    __checked_list: list = []

    def init_checked_list():
        for vertex in VertexInterface.vertex_list:
            UnvisitedList.__checked_list.append(vertex)

    def is_unvisited(vertex: Vertex):
        if vertex in UnvisitedList.__checked_list:
            return True

        return False
