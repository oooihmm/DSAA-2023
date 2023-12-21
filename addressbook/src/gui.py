from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTreeView, QFileSystemModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from src.tree import AVLTree
import sys
import csv
import os

class AddressBookGUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Address Book Management System")
        self.setGeometry(100, 100, 800, 1000)

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
        self.tree_structure_display = QTextEdit(self)
        self.tree_structure_display.setReadOnly(True)

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
        
        main_layout.addWidget(QLabel("AVL Tree Structure"))
        main_layout.addWidget(self.tree_structure_display)

        self.setLayout(main_layout)

        # Initialize Tree View
        self.tree_model.setHorizontalHeaderLabels(["Name"])
        self.tree_view.setModel(self.tree_model)

        # Connect Signals
        self.add_button.clicked.connect(self.add_contact)
        self.search_button.clicked.connect(self.search_contact)

        # Load Contacts on startup
        self.load_contacts()

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
                  self.avl_tree.insert_data(name, email, phone)
                  self.add_contact_to_tree({"이름": name, "이메일": email, "전화번호": phone})

      except FileNotFoundError:
          print(f"CSV file not found at {csv_file_path}")

      except Exception as e:
          print(f"Error loading contacts from CSV: {e}")
    
    def update_tree_structure_display(self):
        tree_structure = self.avl_tree.visualize_tree(self.avl_tree.root)
        self.tree_structure_display.setPlainText(tree_structure)

    def add_contact_to_tree(self, contact):
        item = QStandardItem(f"{contact['이름']} | {contact['이메일']} | {contact['전화번호']}")
        self.tree_model.appendRow(item)
        self.update_tree_structure_display()

    def add_contact(self):
        # Get user input
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        phone = self.phone_input.text().strip()

        if not name or not email or not phone:
            self.display_area.setText("Please fill in all fields.")
            return

        # Add contact to the AVL tree
        self.avl_tree.insert_data(name, email, phone)

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
        self.add_contact_to_tree({"이름": name, "이메일": email, "전화번호": phone})

    def save_contacts_to_csv(self):
        # Get all contacts from AVL tree
        contacts = list(self.avl_tree.inorder_traversal(self.avl_tree.root))

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
        results = self.avl_tree.search_data(search_query)

        # Update tree view with search result
        if results:
            if search_query == "":
                self.display_area.setText(f"No search terms entered")
            else:
                for result in results:
                    # Assuming result is a node, create a dictionary for add_contact_to_tree
                    contact_dict = {
                        "이름": result.name,
                        "이메일": result.email,
                        "전화번호": result.phone
                    }
                    self.display_area.setText(f"Search success")
                    self.add_contact_to_tree(contact_dict)
        else:
            self.display_area.setText(f"No contacts found matching: {search_query}")

def run_gui():
    app = QApplication(sys.argv)
    window = AddressBookGUI()
    window.show()
    sys.exit(app.exec_())
