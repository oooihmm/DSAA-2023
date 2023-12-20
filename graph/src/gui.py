from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QComboBox, QTextEdit

import networkx as nx
import matplotlib.pyplot as plt

class GraphGUI(QMainWindow):
    def __init__(self, graph):
        super(GraphGUI, self).__init__()

        self.graph = graph
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.start_node_combo = QComboBox(self)
        self.end_node_combo = QComboBox(self)

        self.shortest_path_label = QLabel(self)
        self.shortest_path_label.setText("Shortest Path: ")

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.create_gui_elements()
        self.setup_layout()

    def create_gui_elements(self):
        self.start_label = QLabel("Start Node:", self)
        self.end_label = QLabel("End Node:", self)

        self.find_path_button = QPushButton("Find Shortest Path", self)
        self.find_path_button.clicked.connect(self.find_shortest_path)

        self.bfs_button = QPushButton("BFS", self)
        self.bfs_button.clicked.connect(self.run_bfs)

        self.dfs_button = QPushButton("DFS", self)
        self.dfs_button.clicked.connect(self.run_dfs)

        # Populate the dropdowns with node names
        self.start_node_combo.addItems(self.graph.nodes)
        self.end_node_combo.addItems(self.graph.nodes)

    def setup_layout(self):
        layout = QVBoxLayout()

        # Add widgets to the layout
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_node_combo)
        layout.addWidget(self.end_label)
        layout.addWidget(self.end_node_combo)
        layout.addWidget(self.find_path_button)
        layout.addWidget(self.shortest_path_label)
        layout.addWidget(self.bfs_button)
        layout.addWidget(self.dfs_button)
        layout.addWidget(self.text_edit)

        # Set the layout for the central widget

        self.central_widget.setLayout(layout)
        self.setFixedWidth(800)

    def find_shortest_path(self):
        start_node = self.start_node_combo.currentText()
        end_node = self.end_node_combo.currentText()

        self.shortest_path_label.clear()

        # Check if the start and end nodes exist in the graph
        if start_node not in self.graph.nodes or end_node not in self.graph.nodes:
            self.shortest_path_label.setText("Invalid start or end node. Please enter existing nodes.")
            return

        # Check if there is a path between the start and end nodes
        if not nx.has_path(self.graph, source=start_node, target=end_node):
            self.shortest_path_label.setText(f"No path between {start_node} and {end_node}.")
            return

        # Implement BFS to find the shortest path
        shortest_path = nx.shortest_path(self.graph, source=start_node, target=end_node)

        # Update the label with the shortest path
        self.shortest_path_label.setText("Shortest Path: " + " -> ".join(shortest_path))

    def run_bfs(self):
        self.text_edit.clear()

        start_node = self.start_node_combo.currentText()
        end_node = self.end_node_combo.currentText()

        # Check if start and end nodes are the same
        if start_node == end_node:
            self.text_edit.append("Start and end nodes are the same. No traversal needed.")
            return

        # Initialize the queue, visited set, and path dictionary
        queue = [(start_node, [start_node])]  # Each element in the queue is a tuple (node, path)
        visited = set()

        while queue:
            current_node, path = queue.pop(0)
            visited.add(current_node)

            # Display current state
            self.text_edit.append(f"Current Node: {current_node}\nPath: {path}\nVisited: {visited}\n")

            if current_node == end_node:
                self.text_edit.append(f"End node reached in BFS.\nPath: {' -> '.join(path)}")
                return

            neighbors = list(self.graph.neighbors(current_node))

            for neighbor in neighbors:
                if neighbor not in visited:
                    # Move to the next unvisited neighbor
                    queue.append((neighbor, path + [neighbor]))

        # If no path is found
        self.text_edit.append(f"No path found between {start_node} and {end_node}.")


    def run_dfs(self):
        self.text_edit.clear()

        start_node = self.start_node_combo.currentText()
        end_node = self.end_node_combo.currentText()

        # Check if start and end nodes are the same
        if start_node == end_node:
            self.text_edit.append("Start and end nodes are the same. No traversal needed.")
            return

        # Initialize the stack, visited set, and path dictionary
        stack = [(start_node, [start_node])]  # Each element in the stack is a tuple (node, path)
        visited = set()

        while stack:
            current_node, path = stack.pop()
            visited.add(current_node)

            # Display current state
            self.text_edit.append(f"Current Node: {current_node}\nPath: {path}\nVisited: {visited}\n")

            if current_node == end_node:
                self.text_edit.append(f"End node reached in DFS.\nPath: {' -> '.join(path)}")
                return

            neighbors = list(self.graph.neighbors(current_node))
            for neighbor in neighbors:
                if neighbor not in visited:
                    # Move to the next unvisited neighbor
                    stack.append((neighbor, path + [neighbor]))

        # If no path is found
        self.text_edit.append(f"No path found between {start_node} and {end_node}.")


    def update_bfs_state(self, queue, visited):
        current_state = f"Queue: {queue}\nVisited: {visited}\n"
        self.text_edit.append(current_state)

    def update_dfs_state(self, queue, visited):
        current_state = f"Stack: {queue}\nVisited: {visited}\n"
        self.text_edit.append(current_state)

    def run(self):
        self.show()