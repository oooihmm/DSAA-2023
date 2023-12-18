import os

class SelectionSort:
    @staticmethod
    def sort_files(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if order == "오름차순":
                    if items[j] < items[min_idx]:
                        steps_info.append(f"min_idx Swapped: from {min_idx} to {j}")
                        min_idx = j
                else:
                    if items[j] > items[min_idx]:
                        steps_info.append(f"min_idx Swapped: from {min_idx} to {j}")
                        min_idx = j
            items[i], items[min_idx] = items[min_idx], items[i]
            steps_info.append(f"Swapped: {items[i]} and {items[min_idx]}")
        return items, steps_info

    @staticmethod
    def sort_sizes(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                file1 = os.path.join(path, items[j])
                file2 = os.path.join(path, items[min_idx])
                size1 = os.path.getsize(file1)
                size2 = os.path.getsize(file2)
                if order == "오름차순":
                    if size1 < size2:
                        steps_info.append(f"min_idx Swapped: from {min_idx} to {j}")
                        min_idx = j
                else:
                    if size1 > size2:
                        steps_info.append(f"min_idx Swapped: from {min_idx} to {j}")
                        min_idx = j
            items[i], items[min_idx] = items[min_idx], items[i]
            steps_info.append(f"Swapped: {items[i]} and {items[min_idx]}")
        return items, steps_info

    @staticmethod
    def sort_dates(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                file1 = os.path.join(path, items[j])
                file2 = os.path.join(path, items[min_idx])
                date1 = os.path.getctime(file1)
                date2 = os.path.getctime(file2)
                if order == "오름차순":
                    if date1 < date2:
                        steps_info.append(f"min_idx Swapped: from {min_idx} to {j}")
                        min_idx = j
                else:
                    if date1 > date2:
                        steps_info.append(f"min_idx Swapped: from {min_idx} to {j}")
                        min_idx = j
            items[i], items[min_idx] = items[min_idx], items[i]
            steps_info.append(f"Swapped: {items[i]} and {items[min_idx]}")
        return items, steps_info
