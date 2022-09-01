from interfaces import VertexInterface
from definitions import Vertex, Edge

from copy import deepcopy


class Dijkstra:
    __result_graph: list

    def run():
        print("Escolha o vértice de partida:")
        value = input()

        try:
            start = VertexInterface.get_vertex(value)
        except Exception as e:
            print(e)
            return

        PathTable.init_SPD(start)
        UnvisitedList.init_list()

        Dijkstra.__result_graph = Dijkstra.search_next_vertex(start, 0)


    def search_next_vertex(vertex: Vertex, current_path_weight: int) -> list:  # recursivo
        PathTable.update_paths(vertex, current_path_weight)

        edge = Dijkstra.find_smallest_edge(vertex)
        if edge:
            Dijkstra.search_next_vertex(edge.destination, edge.weight + current_path_weight)
            UnvisitedList.mark_as_visited(vertex)
            return []

        return []


    def find_smallest_edge(vertex: Vertex) -> Edge | None:
        smallest: Edge = None

        for edge in vertex.edges:
            if smallest == None or edge.weight < smallest.weight:
                if UnvisitedList.is_unvisited(edge.destination):
                    smallest = edge

        return smallest


class PathTable:
    __shortest_paths: dict = {}

    def init_SPD(start: Vertex):
        for vertex in VertexInterface.vertex_list:
            if vertex == start:
                PathTable.__shortest_paths[vertex] = 0
            else:
                PathTable.__shortest_paths[vertex] = None

    def show_paths():
        for path in PathTable.__shortest_paths:
            print(path)

    def update_paths(vertex: Vertex, current_path_weight: int):
        for edge in vertex.edges:
            total_weight_to_vertex = current_path_weight + edge.weight
            try:
                if (
                    PathTable.__shortest_paths[edge.destination] == None
                    or total_weight_to_vertex
                    < PathTable.__shortest_paths[edge.destination]
                ):
                    PathTable.__shortest_paths[edge.destination] = edge.weight
            except KeyError as e:
                print("Erro! Tentativa de atualizar vértice que não existe na tabela")
                exit()


class UnvisitedList:
    __vertexes: list = []

    def init_list():
        for vertex in VertexInterface.vertex_list:
            UnvisitedList.__vertexes.append(vertex)

    def is_unvisited(vertex: Vertex):
        if vertex in UnvisitedList.__vertexes:
            return True

        return False

    def mark_as_visited(vertex: Vertex):
        UnvisitedList.__vertexes.remove(vertex)

    def is_empty():
        if UnvisitedList.__vertexes:
            return True

        return False
