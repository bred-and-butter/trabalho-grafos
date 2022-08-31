class Edge:
    def __init__(self, weight: int, destination) -> None:
        self.weight = weight
        self.destination = destination

    def __str__(self) -> str:
        return f"{self.weight}---> {self.destination}"


class Vertex:
    __total_ammount: int = 0
    __unique_value_list: list = []

    def __init__(self, value, edges: list[Edge]) -> None:
        if Vertex.__total_ammount > 20:
            raise Exception("Limite de vértices alcançado")

        self.value = value
        self.edges = edges
        self.checked = False

        Vertex.__total_ammount += 1
        Vertex.__unique_value_list.append(self.value)

    def __str__(self) -> str:
        return self.value

    def get_total_ammount():
        return Vertex.__total_ammount

    def is_value_free(value):
        if value in Vertex.__unique_value_list:
            return False

        return True
