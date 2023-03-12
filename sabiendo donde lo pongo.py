import networkx as nx
import matplotlib.pyplot as plt
# Creamos un grafo vacío
G = nx.Graph()

# Agregamos nodos al grafo con atributos de posición
G.add_node(1, pos=(0, 0))
G.add_node(2, pos=(1, 1))
G.add_node(3, pos=(2, 0))
G.add_node(4, pos=(1, -1))

# Agregamos aristas al grafo
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Dibujamos el grafo con posiciones geográficas
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True)

# Calculamos el camino más corto entre los nodos 1 y 4
camino = nx.shortest_path(G, source=1, target=4)

# Dibujamos el camino más corto en color rojo
nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v in zip(camino[:-1], camino[1:])], edge_color='r', width=5)

# Mostramos el dibujo en pantalla
plt.show()
