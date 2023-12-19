class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
       self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        return y

    def insert(self, root, key, data):
        if not root:
            return TreeNode(key, data)

        if key < root.key:
            root.left = self.insert(root.left, key, data)
        elif key > root.key:
            root.right = self.insert(root.right, key, data)
        else:
            # Duplicate keys are not allowed
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_contact(self, key, data):
        self.root = self.insert(self.root, key, data)

    def search_all(self, root, key, results):
        if not root:
            return

        # 부분 일치를 처리하기 위해 key, 이메일, 전화번호를 대소문자 구분 없이 비교
        if (
            key.lower() in root.key.lower()
            or key.lower() in root.data["이메일"].lower()
            or key.lower() in root.data["전화번호"].lower()
        ):
            results.append(root)

        self.search_all(root.left, key, results)
        self.search_all(root.right, key, results)

    def search_contact_all(self, key):
        results = []
        self.search_all(self.root, key, results)
        return results

    def avl_tree_in_order(self, root):  # 추가: AVL 트리의 중위 순회 구현
        if root is not None:
            yield from self.avl_tree_in_order(root.left)
            yield root.data
            yield from self.avl_tree_in_order(root.right)

    def insert_contact_from_csv(self, csv_data):
        for entry in csv_data:
            name, email, phone = entry.split(",")
            contact = {"이름": name, "이메일": email, "전화번호": phone}
            self.insert_contact(name, contact)

    def search_contact(self, key):
        return self.search(self.root, key)

    def visualize_tree(self):
        return self._visualize_tree(self.root)

    def _visualize_tree(self, node, level=0, prefix="Root:"):
        if node is None:
            return ""
        
        res = "  " * level + prefix + f" {node.key}\n"
        
        if node.left is not None or node.right is not None:
            res += self._visualize_tree(node.left, level + 1, "├── Left:")
            res += self._visualize_tree(node.right, level + 1, "└── Right:")
        
        return res