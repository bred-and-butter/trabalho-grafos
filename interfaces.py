from defs import Vertex, Edge


class VertexInterface:
    __vertex_list: list[Vertex] = []

    def interface_loop():
        while True:
            print("Deseja inserir um vértice?(s/n)(max 20):")
            letter = input()

            if letter == "s":
                print("Insira o nome do vértice")
                value = input()
                VertexInterface.create_vertex(value)

            elif letter == "n":
                return

    def create_vertex(value):
        if Vertex.is_value_free(value):
            VertexInterface.__vertex_list.append(Vertex(value=value, edges=[]))
        else:
            print("Nome já pertence a outro vértice")

    def get_vertex(value):
        if not Vertex.is_value_free(value):
            for vertex in VertexInterface.__vertex_list:
                if vertex.value == value:
                    return vertex

        raise Exception("Vertice não encontrado")

    def print_vertexes():
        print("Imprimindo vértices criados:")
        for vertex in VertexInterface.__vertex_list:
            print(vertex)


class EdgeInterface:
    __edge_list: list[Edge] = []

    def interface_loop():
        while True:
            print("Deseja inserir uma aresta?(s/n)")
            letter = input()

            if letter == "s":
                print("Insira o peso da aresta")
                weight = input()

                print("Insira o nome de um dos vértices")
                try:
                    vertex1 = EdgeInterface.handle_vertex_input()
                except Exception as e:
                    print(e)
                    continue

                print("Insira o nome de outro vértice")
                try:
                    vertex2 = EdgeInterface.handle_vertex_input()
                except Exception as e:
                    print(e)
                    continue

                EdgeInterface.__edge_list.append(
                    Edge(weight=weight, vertex1=vertex1, vertex2=vertex2)
                )

            elif letter == "n":
                return

    def handle_vertex_input():
        value = input()
        return VertexInterface.get_vertex(value)

    def print_edges():
        print("Imprimindo arestas criadas:")
        for edge in EdgeInterface.__edge_list:
            print(edge)
