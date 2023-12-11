import os

class QuickSort:
    @staticmethod
    def sort_files(items, path, order):
        steps_info = []
        if order == "오름차순":
            QuickSort.quick_sort(items, 0, len(items) - 1, steps_info)
        else:
            QuickSort.quick_sort_descending(items, 0, len(items) - 1, steps_info)
        return items, steps_info

    @staticmethod
    def sort_sizes(items, path, order):
        steps_info = []
        if order == "오름차순":
            QuickSort.quick_sort_sizes(items, path, 0, len(items) - 1, steps_info)
        else:
            QuickSort.quick_sort_sizes_descending(items, path, 0, len(items) - 1, steps_info)
        return items, steps_info

    @staticmethod
    def sort_dates(items, path, order):
        steps_info = []
        if order == "오름차순":
            QuickSort.quick_sort_dates(items, path, 0, len(items) - 1, steps_info)
        else:
            QuickSort.quick_sort_dates_descending(items, path, 0, len(items) - 1, steps_info)
        return items, steps_info

    @staticmethod
    def quick_sort(items, low, high, steps_info):
        if low < high:
            pi = QuickSort.partition(items, low, high, steps_info)
            QuickSort.quick_sort(items, low, pi - 1, steps_info)
            QuickSort.quick_sort(items, pi + 1, high, steps_info)

    @staticmethod
    def quick_sort_descending(items, low, high, steps_info):
        if low < high:
            pi = QuickSort.partition_descending(items, low, high, steps_info)
            QuickSort.quick_sort_descending(items, low, pi - 1, steps_info)
            QuickSort.quick_sort_descending(items, pi + 1, high, steps_info)

    @staticmethod
    def quick_sort_sizes(items, path, low, high, steps_info):
        if low < high:
            pi = QuickSort.partition_sizes(items, path, low, high, steps_info)
            QuickSort.quick_sort_sizes(items, path, low, pi - 1, steps_info)
            QuickSort.quick_sort_sizes(items, path, pi + 1, high, steps_info)

    @staticmethod
    def quick_sort_sizes_descending(items, path, low, high, steps_info):
        if low < high:
            pi = QuickSort.partition_sizes_descending(items, path, low, high, steps_info)
            QuickSort.quick_sort_sizes_descending(items, path, low, pi - 1, steps_info)
            QuickSort.quick_sort_sizes_descending(items, path, pi + 1, high, steps_info)

    @staticmethod
    def quick_sort_dates(items, path, low, high, steps_info):
        if low < high:
            pi = QuickSort.partition_dates(items, path, low, high, steps_info)
            QuickSort.quick_sort_dates(items, path, low, pi - 1, steps_info)
            QuickSort.quick_sort_dates(items, path, pi + 1, high, steps_info)

    @staticmethod
    def quick_sort_dates_descending(items, path, low, high, steps_info):
        if low < high:
            pi = QuickSort.partition_dates_descending(items, path, low, high, steps_info)
            QuickSort.quick_sort_dates_descending(items, path, low, pi - 1, steps_info)
            QuickSort.quick_sort_dates_descending(items, path, pi + 1, high, steps_info)

    @staticmethod
    def partition(items, low, high, steps_info):
        pivot = items[high]
        i = low - 1

        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                steps_info.append(f"Swapped: {items[i]} and {items[j]}") 

        items[i + 1], items[high] = items[high], items[i + 1]
        steps_info.append(f"Pivot Swapped: {items[i + 1]} and {items[high]}")
        return i + 1

    @staticmethod
    def partition_descending(items, low, high, steps_info):
        pivot = items[high]
        i = low - 1

        for j in range(low, high):
            if items[j] >= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                steps_info.append(f"Swapped: {items[i]} and {items[j]}") 

        items[i + 1], items[high] = items[high], items[i + 1]
        steps_info.append(f"Pivot Swapped: {items[i + 1]} and {items[high]}")
        return i + 1

    @staticmethod
    def partition_sizes(items, path, low, high, steps_info):
        pivot = os.path.getsize(os.path.join(path, items[high]))
        i = low - 1

        for j in range(low, high):
            if os.path.getsize(os.path.join(path, items[j])) <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                steps_info.append(f"Swapped: {items[i]} and {items[j]}") 

        items[i + 1], items[high] = items[high], items[i + 1]
        steps_info.append(f"Pivot Swapped: {items[i + 1]} and {items[high]}")
        return i + 1

    @staticmethod
    def partition_sizes_descending(items, path, low, high, steps_info):
        pivot = os.path.getsize(os.path.join(path, items[high]))
        i = low - 1

        for j in range(low, high):
            if os.path.getsize(os.path.join(path, items[j])) >= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                steps_info.append(f"Swapped: {items[i]} and {items[j]}") 

        items[i + 1], items[high] = items[high], items[i + 1]
        steps_info.append(f"Pivot Swapped: {items[i + 1]} and {items[high]}")
        return i + 1

    @staticmethod
    def partition_dates(items, path, low, high, steps_info):
        pivot = os.path.getctime(os.path.join(path, items[high]))
        i = low - 1

        for j in range(low, high):
            if os.path.getctime(os.path.join(path, items[j])) <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                steps_info.append(f"Swapped: {items[i]} and {items[j]}") 

        items[i + 1], items[high] = items[high], items[i + 1]
        steps_info.append(f"Pivot Swapped: {items[i + 1]} and {items[high]}")
        return i + 1

    @staticmethod
    def partition_dates_descending(items, path, low, high, steps_info):
        pivot = os.path.getctime(os.path.join(path, items[high]))
        i = low - 1

        for j in range(low, high):
            if os.path.getctime(os.path.join(path, items[j])) >= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                steps_info.append(f"Swapped: {items[i]} and {items[j]}") 

        items[i + 1], items[high] = items[high], items[i + 1]
        steps_info.append(f"Pivot Swapped: {items[i + 1]} and {items[high]}")
        return i + 1
