import sys
from PyQt5.QtWidgets import QApplication
from src.graph import Graph
from src.gui import GraphGUI

def main():
    # Load graph data from file
    graph = Graph.load_from_json("src/dataset/congress_network_data.json")

    # Create PyQt5 application
    app = QApplication(sys.argv)

    # Create and show the GUI
    gui = GraphGUI(graph)
    gui.show()

    # Run the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
