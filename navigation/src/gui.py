from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QSizePolicy
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class GraphGUI(QMainWindow):
    def __init__(self, graph):
        super(GraphGUI, self).__init__()

        self.graph = graph
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.start_node_input = QLineEdit(self)
        self.end_node_input = QLineEdit(self)

        self.shortest_path_label = QLabel(self)
        self.shortest_path_label.setText("Shortest Path: ")

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Corrected

        self.create_gui_elements()
        self.setup_layout()

    def create_gui_elements(self):
        self.start_label = QLabel("Start Node:", self)
        self.end_label = QLabel("End Node:", self)

        self.find_path_button = QPushButton("Find Shortest Path", self)
        self.find_path_button.clicked.connect(self.find_shortest_path)

    def setup_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_node_input)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_node_input)
        layout.addWidget(self.find_path_button)
        layout.addWidget(self.shortest_path_label)
        layout.addWidget(self.canvas)

        self.central_widget.setLayout(layout)

    def find_shortest_path(self):
        start_node = self.start_node_input.text()
        end_node = self.end_node_input.text()

        # Implement BFS or DFS to find the shortest path
        shortest_path = nx.shortest_path(self.graph, source=start_node, target=end_node)

        # Update the label with the shortest path
        self.shortest_path_label.setText("Shortest Path: " + " -> ".join(shortest_path))

        # Visualize the graph with the shortest path
        self.visualize_graph(shortest_path)

    def visualize_graph(self, path):
        # Implement code to visualize the graph using matplotlib and networkx
        # You can customize this method based on your specific requirements
        pass

    def run(self):
        self.show()
