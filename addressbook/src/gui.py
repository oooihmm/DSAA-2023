# src/gui.py
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTreeView, QFileSystemModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QTimer
from src.tree import AVLTree, AVLTreeVisualizer
import sys
import csv
import os

class AddressBookGUI(QWidget):
    def __init__(self, visualizer=None):
        super().__init__()
        
        self.setWindowTitle("Address Book Management System")
        self.setGeometry(100, 100, 800, 600)

        self.avl_visualizer = AVLTreeVisualizer()
        self.avl_tree = AVLTree(visualizer=self.avl_visualizer)

        # Components
        self.name_input = QLineEdit(self)
        self.email_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)
        self.add_button = QPushButton("Add Contact", self)
        self.search_input = QLineEdit(self)
        self.search_button = QPushButton("Search", self)
        self.display_area = QTextEdit(self)
        self.tree_view = QTreeView(self)
        self.tree_model = QStandardItemModel()

        # AVL Tree
        self.avl_tree = AVLTree()

        # Layout
        main_layout = QVBoxLayout()

        # Input Form
        input_layout = QVBoxLayout()
        input_layout.addWidget(QLabel("Name:"))
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(QLabel("Email:"))
        input_layout.addWidget(self.email_input)
        input_layout.addWidget(QLabel("Phone:"))
        input_layout.addWidget(self.phone_input)
        input_layout.addWidget(self.add_button)
        main_layout.addLayout(input_layout)

        # Search
        search_layout = QVBoxLayout()
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        main_layout.addLayout(search_layout)

        # Display Area
        main_layout.addWidget(self.display_area)

        # Tree View
        main_layout.addWidget(QLabel("Contacts"))
        main_layout.addWidget(self.tree_view)

        self.setLayout(main_layout)

        # Initialize Tree View
        self.tree_model.setHorizontalHeaderLabels(["Name"])
        self.tree_view.setModel(self.tree_model)

        # Connect Signals
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)
        self.avl_visualizer.update_visualization.connect(self.update_visualization_text)

        # Load Contacts on startup
        self.load_contacts()

        # Initialize last_modification_time
        self.last_modification_time = 0

        # Timer for periodically checking CSV file changes
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_csv_changes)
        self.timer.start(5000)  # 5 seconds interval (adjust as needed)

    def check_csv_changes(self):
        # Check if the CSV file has been modified
        if self.is_csv_modified():
            # Reload contacts from the updated CSV file
            self.load_contacts()

    def is_csv_modified(self):
        # Compare the current modification time with the stored one
        current_modification_time = os.path.getmtime("data/contacts.csv")
        if current_modification_time != self.last_modification_time:
            self.last_modification_time = current_modification_time
            return True
        return False

    def update_visualization_text(self, text):
        # Update the display area with AVL tree visualization
        self.display_area.clear()
        self.display_area.append(text)

    def load_contacts(self):
    # Define the CSV file path
      csv_file_path = "data/contacts.csv"

    # Check if the CSV file exists
      try:
          with open(csv_file_path, mode="r", newline="", encoding="utf-8") as csv_file:
              csv_reader = csv.reader(csv_file)
              next(csv_reader)  # Skip the header row
              for row in csv_reader:
                  name, email, phone = row
                  new_contact = {"이름": name, "이메일": email, "전화번호": phone}
                  self.avl_tree.insert_contact(name, new_contact)
                  self.add_contact_to_tree(new_contact)

      except FileNotFoundError:
          print(f"CSV file not found at {csv_file_path}")

      except Exception as e:
          print(f"Error loading contacts from CSV: {e}")

    def add_contact_to_tree(self, contact):
        item = QStandardItem(f"{contact['이름']} | {contact['이메일']} | {contact['전화번호']}")
        self.tree_model.appendRow(item)

    def add_contact(self):
        # Get user input
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not email or not phone:
            self.display_area.setText("Please fill in all fields.")
            return

        # Create contact dictionary
        new_contact = {"이름": name, "이메일": email, "전화번호": phone}

        # Add contact to the AVL tree
        self.avl_tree.insert_contact(name, new_contact)

        # Update the display area
        self.display_area.clear()
        self.display_area.append(f"Contact added:\nName: {name}\nEmail: {email}\nPhone: {phone}")

        # Clear input fields
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()

        # Save updated contacts to the CSV file
        self.save_contacts_to_csv()

        # Update tree view with the new contact
        self.add_contact_to_tree(new_contact)

    def save_contacts_to_csv(self):
        # Get all contacts from AVL tree
        contacts = list(self.avl_tree.avl_tree_in_order(self.avl_tree.root))

        # Define the CSV file path
        csv_file_path = "data/contacts.csv"

        # Write contacts to CSV file
        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["이름", "이메일", "전화번호"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write contacts
            for contact in contacts:
                writer.writerow(contact)

    def search_contact(self):
        # Get user input for search
        search_query = self.search_input.text().strip()

        # Clear existing items in the tree view
        self.tree_model.clear()

        # Search contacts
        results = self.avl_tree.search_contact_all(search_query)

        # Update tree view with search result
        if results:
            for result in results:
                self.add_contact_to_tree(result.data)
        else:
            self.display_area.setText("Contact not found.")

def run_gui():
    app = QApplication(sys.argv)
    window = AddressBookGUI()
    window.show()
    sys.exit(app.exec_())
