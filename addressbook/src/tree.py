import csv

class Node:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert_data_from_csv(self, csv_filename):
        with open(csv_filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                name, email, phone = row
                self.insert_data(name, email, phone)

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, name, email, phone):
        if not node:
            return Node(name, email, phone)

        if name < node.name:
            node.left = self.insert(node.left, name, email, phone)
        else:
            node.right = self.insert(node.right, name, email, phone)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

        if balance > 1:
            if name < node.left.name:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if name > node.right.name:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def insert_data(self, name, email, phone):
        self.root = self.insert(self.root, name, email, phone)

    def inorder_traversal(self, node, result=[]):
        if node:
            self.inorder_traversal(node.left, result)
            result.append({"이름": node.name, "이메일": node.email, "전화번호": node.phone})
            self.inorder_traversal(node.right, result)
        return result

    def search_data(self, criteria):
        results = []

        def _search_recursive(node):
            if not node:
                return

            # Check if the criteria is found in any of the contact details
            if (
                criteria.lower() in node.name.lower()
                or (node.phone and criteria in node.phone)
                or (node.email and criteria.lower() in node.email.lower())
            ):
                results.append(node)

            # Continue searching in left and right subtrees
            _search_recursive(node.left)
            _search_recursive(node.right)

        # Start the search from the root
        _search_recursive(self.root)

        return results

    def visualize_tree(self, node, level=0, prefix="Root:"):
        if node is None:
            return ""

        res = "  " * level + prefix + f" {node.name}\n"

        if node.left is not None or node.right is not None:
            res += self.visualize_tree(node.left, level + 1, "├── Left:")
            res += self.visualize_tree(node.right, level + 1, "└── Right:")

        return res
    
if __name__ == "__main__": 

    # CSV 파일에서 데이터 읽기
    csv_filename = '../data/contacts.csv'

    avl_tree = AVLTree()

    # CSV 파일 데이터 삽입
    avl_tree.insert_data_from_csv(csv_filename)

    # 중위 순회로 데이터 출력
    print("AVL Tree 내 데이터:")
    avl_tree.inorder_traversal(avl_tree.root)

    # 트리 구조 출력
    tree_structure = avl_tree.visualize_tree(avl_tree.root)
    print("\nAVL Tree 구조:")
    print(tree_structure)