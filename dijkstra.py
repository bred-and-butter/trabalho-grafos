from interfaces import VertexInterface
from definitions import Vertex, Edge


class Dijkstra:
    def run():
        print("Escolha o vértice de partida:")
        value = input()

        try:
            start = VertexInterface.get_vertex(value)
        except Exception as e:
            print(e)
            return

        PathTable.init_table(start)
        UnvisitedList.init_list()

        Dijkstra.search_next_vertex(start, 0)

        PathDiagram.show_paths()
        PathTable.show_table()

    def search_next_vertex(vertex: Vertex, current_path_weight: int):  # recursivo
        PathTable.update_table(vertex, current_path_weight)
        UnvisitedList.mark_as_visited(vertex)

        while Dijkstra.has_remaining_paths(vertex):
            edge = Dijkstra.find_smallest_edge(vertex)
            Dijkstra.search_next_vertex(
                edge.destination, edge.weight + current_path_weight)

    def find_smallest_edge(vertex: Vertex) -> Edge | None:
        smallest: Edge = None

        for edge in vertex.edges:
            if smallest == None or edge.weight < smallest.weight:
                if UnvisitedList.is_unvisited(edge.destination):
                    smallest = edge

        return smallest

    def has_remaining_paths(vertex: Vertex) -> bool:
        for edge in vertex.edges:
            if UnvisitedList.is_unvisited(edge.destination):
                return True

        return False


class PathTable:
    __values_from_start: dict = {}

    def init_table(start: Vertex):
        for vertex in VertexInterface.vertex_list:
            if vertex == start:
                PathTable.__values_from_start[vertex] = 0
            else:
                PathTable.__values_from_start[vertex] = None

    def show_table():
        for vertex, value in PathTable.__values_from_start.items():
            print(vertex, ' : ', value)

    def update_table(vertex: Vertex, current_path_weight: int):
        for edge in vertex.edges:
            total_weight_to_vertex = current_path_weight + edge.weight
            try:
                if (
                    PathTable.__values_from_start[edge.destination] == None
                    or total_weight_to_vertex
                    < PathTable.__values_from_start[edge.destination]
                ):
                    PathTable.__values_from_start[edge.destination] = total_weight_to_vertex
                    PathDiagram.update_path(vertex, edge)
            except KeyError:
                print("Erro! Tentativa de atualizar vértice que não existe na tabela")
                exit()


class PathDiagram:
    __shortest_paths: dict = {}

    def init_diagram(start: Vertex):
        for vertex in VertexInterface.vertex_list:
            if vertex == start:
                PathDiagram.__shortest_paths[vertex] = 0
            else:
                PathDiagram.__shortest_paths[vertex] = None

    def update_path(vertex: Vertex, edge: Edge):
        PathDiagram.__shortest_paths[edge.destination] = f"{vertex}--{edge}"

    def show_paths():
        for vertex, path in PathDiagram.__shortest_paths.items():
            print(vertex, ' : ', path)


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
