import os

class BubbleSort:
    @staticmethod
    def sort_files(items, path, order):
        steps_info = []
        comparisons = 0
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                comparisons += 1
                if order == "오름차순":
                    if items[j] > items[j + 1]:
                        items[j], items[j + 1] = items[j + 1], items[j]
                        steps_info.append(f"{items[j]}, {items[j + 1]} => {items[j + 1]}, {items[j]}")
                    else:
                        steps_info.append(f"{items[j]}, {items[j + 1]}")
                else:
                    if items[j] < items[j + 1]:
                        items[j], items[j + 1] = items[j + 1], items[j]
                        steps_info.append(f"{items[j]}, {items[j + 1]} => {items[j + 1]}, {items[j]}")
                    else:
                        steps_info.append(f"{items[j]}, {items[j + 1]}")
        print(comparisons)
        return items, steps_info

    @staticmethod
    def sort_sizes(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                file1 = os.path.join(path, items[j])
                file2 = os.path.join(path, items[j + 1])
                size1 = os.path.getsize(file1)
                size2 = os.path.getsize(file2)
                if order == "오름차순":
                    if size1 > size2:
                        items[j], items[j + 1] = items[j + 1], items[j]
                        steps_info.append(f"{items[j]}, {items[j + 1]} => {items[j + 1]}, {items[j]}")
                    else:
                        steps_info.append(f"{items[j]}, {items[j + 1]}")
                else:
                    if size1 < size2:
                        items[j], items[j + 1] = items[j + 1], items[j]
                        steps_info.append(f"{items[j]}, {items[j + 1]} => {items[j + 1]}, {items[j]}")
                    else:
                        steps_info.append(f"{items[j]}, {items[j + 1]}")
        return items, steps_info

    @staticmethod
    def sort_dates(items, path, order):
        steps_info = []
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                file1 = os.path.join(path, items[j])
                file2 = os.path.join(path, items[j + 1])
                date1 = os.path.getctime(file1)
                date2 = os.path.getctime(file2)
                if order == "오름차순":
                    if date1 > date2:
                        items[j], items[j + 1] = items[j + 1], items[j]
                        steps_info.append(f"{items[j]}, {items[j + 1]} => {items[j + 1]}, {items[j]}")
                    else:
                        steps_info.append(f"{items[j]}, {items[j + 1]}")
                else:
                    if date1 < date2:
                        items[j], items[j + 1] = items[j + 1], items[j]
                        steps_info.append(f"{items[j]}, {items[j + 1]} => {items[j + 1]}, {items[j]}")
                    else:
                        steps_info.append(f"{items[j]}, {items[j + 1]}")
        return items, steps_info
