from definitions import Vertex, Edge


class VertexInterface:
    vertex_list: list[Vertex] = []

    def interface_loop():
        while True:
            print("Deseja inserir um vértice?(s/n)(max 20):")
            print(f"Quantidade já criada: {Vertex.get_total_ammount()}")
            letter = input()

            if letter == "s":
                print("Insira o nome do vértice")
                value = input()
                VertexInterface.create_vertex(value)

            elif letter == "n":
                return

    def create_vertex(value):
        if Vertex.is_value_free(value):
            VertexInterface.vertex_list.append(Vertex(value=value, edges=[]))
        else:
            print("Nome já pertence a outro vértice")

    def get_vertex(value):
        if not Vertex.is_value_free(value):
            for vertex in VertexInterface.vertex_list:
                if vertex.value == value:
                    return vertex

        raise Exception("Vertice não encontrado")

    def uncheck_vertexes():
        for vertex in VertexInterface.vertex_list:
            vertex.checked = False

    def print_vertexes():
        print("Imprimindo vértices criados:")
        for vertex in VertexInterface.vertex_list:
            print(vertex)

    def print_adjacency_list():
        print("Imprimindo lista de adjacência:")
        for vertex in VertexInterface.vertex_list:
            print(vertex)
            for edge in vertex.edges:
                print("   ", edge)


class EdgeInterface:
    def interface_loop():
        while True:
            VertexInterface.print_adjacency_list()

            print("Deseja inserir uma aresta?(s/n)")
            letter = input()

            if letter == "s":
                try:
                    print("Insira o peso da aresta")
                    weight = int(input())

                    print("Insira o nome do vértice fonte")
                    vertex1 = EdgeInterface.handle_vertex_input()

                    print("Insira o nome do vértice destino")
                    vertex2 = EdgeInterface.handle_vertex_input()

                    print("Direcionado?(s/n)")
                    directed = input()

                except ValueError:
                    print("Insira somente números inteiros")
                    continue
                except Exception as e:
                    print(e)
                    continue

                EdgeInterface.connect_vertexes(
                    weight=weight, vertex1=vertex1, vertex2=vertex2, directed=directed
                )

            elif letter == "n":
                return

    def handle_vertex_input():
        value = input()
        return VertexInterface.get_vertex(value)

    def connect_vertexes(weight: int, vertex1: Vertex, vertex2: Vertex, directed: str):
        if directed == "s":
            vertex1.edges.append(
                Edge(weight=weight, destination=vertex2)
            )

        elif directed == "n":
            vertex1.edges.append(
                Edge(weight=weight, destination=vertex2)
            )

            vertex2.edges.append(
                Edge(weight=weight, destination=vertex1)
            )
