class Vertex:
    __total_ammount: int = 0
    
    def __init__(self, value, edges: list) -> None:
        if Vertex.__total_ammount > 20:
            raise Exception("Instance ammount limit reached")

        self.value = value
        self.edges = edges
        self.checked = False

        Vertex.__total_ammount += 1

    def __str__(self) -> str:
        return self.value


    def get_total_ammount():
        return Vertex.__total_ammount

class Edge:
    def __init__(self, weight: int, vertex1: Vertex, vertex2: Vertex) -> None:
        self.weight = weight
        self.vertex1 = vertex1
        self.vertex2 = vertex2

        self.vertex1.edges.append(self)
        self.vertex2.edges.append(self)

    def __str__(self) -> str:
        return f"{self.vertex1} --- {self.weight} --- {self.vertex2}"