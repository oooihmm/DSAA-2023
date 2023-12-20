import sys
from PyQt5.QtWidgets import QApplication
from src.gui import GraphGUI
import json
import networkx as nx

def main():
    # Load the graph data
    with open('./src/dataset/congress_network_data.json', 'r') as file:
        data = json.load(file)

    inList = data[0]['inList']
    inWeight = data[0]['inWeight']
    outList = data[0]['outList']
    outWeight = data[0]['outWeight']
    usernameList = data[0]['usernameList']

    # Create the graph
    G = nx.DiGraph()

    for i, username in enumerate(usernameList):
        G.add_node(username)

    for i, in_list in enumerate(inList):
        for j, in_node in enumerate(in_list):
            weight = inWeight[i][j]
            G.add_edge(usernameList[in_node], usernameList[i], weight=weight)

    for i, out_list in enumerate(outList):
        for j, out_node in enumerate(out_list):
            weight = outWeight[i][j]
            G.add_edge(usernameList[i], usernameList[out_node], weight=weight)

    # Create and run the GUI
    app = QApplication([])
    gui = GraphGUI(G)
    gui.run()
    app.exec_()

if __name__ == "__main__":
    main()
