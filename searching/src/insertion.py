import os

class InsertionSort:
    @staticmethod
    def sort_files(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(1, n):
            key = items[i]
            j = i - 1
            if order == "오름차순":
                while j >= 0 and key < items[j]:
                    items[j + 1] = items[j]
                    steps_info.append(f"Insert {key} between {items[:j]} and {items[j+1:]}")
                    j -= 1
                items[j + 1] = key
            else:
                while j >= 0 and key > items[j]:
                    items[j + 1] = items[j]
                    steps_info.append(f"Insert {key} between {items[:j]} and {items[j+1:]}")
                    j -= 1
                items[j + 1] = key
        return items, steps_info

    @staticmethod
    def sort_sizes(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(1, n):
            key = items[i]
            j = i - 1
            file_key = os.path.join(path, key)
            size_key = os.path.getsize(file_key)
            if order == "오름차순":
                while j >= 0 and size_key < os.path.getsize(os.path.join(path, items[j])):
                    items[j + 1] = items[j]
                    steps_info.append(f"Insert {key} between {items[:j]} and {items[j+1:]}")
                    j -= 1
                items[j + 1] = key
            else:
                while j >= 0 and size_key > os.path.getsize(os.path.join(path, items[j])):
                    items[j + 1] = items[j]
                    steps_info.append(f"Insert {key} between {items[:j]} and {items[j+1:]}")
                    j -= 1
                items[j + 1] = key
        return items, steps_info

    @staticmethod
    def sort_dates(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(1, n):
            key = items[i]
            j = i - 1
            file_key = os.path.join(path, key)
            date_key = os.path.getctime(file_key)
            if order == "오름차순":
                while j >= 0 and date_key < os.path.getctime(os.path.join(path, items[j])):
                    items[j + 1] = items[j]
                    steps_info.append(f"Insert {key} between {items[:j]} and {items[j+1:]}")
                    j -= 1
                items[j + 1] = key
            else:
                while j >= 0 and date_key > os.path.getctime(os.path.join(path, items[j])):
                    items[j + 1] = items[j]
                    steps_info.append(f"Insert {key} between {items[:j]} and {items[j+1:]}")
                    j -= 1
                items[j + 1] = key
        return items, steps_info
