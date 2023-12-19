import networkx as nx
import json

class Graph(nx.Graph):
    def __init__(self):
        super(Graph, self).__init__()

    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data_list = json.load(file)

            if not data_list:
                raise ValueError("Empty data list in the JSON file.")

            # Assuming data_list is a list of graphs
            graph_data = data_list[0]

            graph = cls()

            for user_id in graph_data.get('usernameList', []):
                graph.add_node(user_id)

            for i, user_id in enumerate(graph_data.get('usernameList', [])):
                for neighbor_id in graph_data.get('outList', [])[i]:
                    graph.add_edge(user_id, neighbor_id)

            return graph
