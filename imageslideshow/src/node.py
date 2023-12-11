class ImageNode:
    def __init__(self, image_name, image_path):
        self.image_name = image_name
        self.image_path = image_path
        self.next_node = None
        self.prev_node = None

    def set_next(self, next_node):
        self.next_node = next_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node
