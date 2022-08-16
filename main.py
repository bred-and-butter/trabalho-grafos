from defs import Vertex, Edge

print("criando vertices")
joao = Vertex(value="Joao", edges=[])
maria = Vertex(value="Maria", edges=[])
print(f"criados vertices {joao} e {maria}")

aresta_joao_maria = Edge(weight=1, vertex1=joao, vertex2=maria)
print(f"aresta criada:\n{aresta_joao_maria}")
