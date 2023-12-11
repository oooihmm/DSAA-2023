from .node import ImageNode


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, image_name, image_path):
        new_node = ImageNode(image_name, image_path)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
        self.print_list()  # 값이 추가될 때마다 연결 리스트 출력

    def remove(self, image_name):
        current = self.head
        while current:
            if current.image_name == image_name:
                if current.prev_node:
                    current.prev_node.set_next(current.next_node)
                else:
                    self.head = current.next_node

                if current.next_node:
                    current.next_node.set_prev(current.prev_node)
                else:
                    self.tail = current.prev_node
                self.print_list()  # 값이 제거될 때마다 연결 리스트 출력
                return True
            current = current.next_node
        return False

    def print_list(self):  # 연결 리스트 내용을 출력하는 함수
        current = self.head
        while current:
            print(f"[ {current.image_name} ({current.image_path}) ]", end=" -> ")
            current = current.next_node
        print("None\n")
