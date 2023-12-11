import os

class MergeSort:
    @staticmethod
    def sort_files(items, path, order):
        steps_info = []
        if len(items) > 1:
            mid = len(items) // 2
            left_arr = items[:mid]
            right_arr = items[mid:]

            MergeSort.sort_files(left_arr, path, order)
            MergeSort.sort_files(right_arr, path, order)

            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                if order == "오름차순":
                    if left_arr[i] <= right_arr[j]:
                        items[k] = left_arr[i]
                        steps_info.append(f"{left_arr[i]} <= {right_arr[j]}: {left_arr[i]}")
                        i += 1
                    else:
                        items[k] = right_arr[j]
                        steps_info.append(f"{left_arr[i]} > {right_arr[j]}: {right_arr[j]}")
                        j += 1
                else:
                    if left_arr[i] >= right_arr[j]:
                        items[k] = left_arr[i]
                        steps_info.append(f"{left_arr[i]} >= {right_arr[j]}: {left_arr[i]}")
                        i += 1
                    else:
                        items[k] = right_arr[j]
                        steps_info.append(f"{left_arr[i]} <= {right_arr[j]}: {left_arr[i]}")
                        j += 1
                k += 1

            while i < len(left_arr):
                items[k] = left_arr[i]
                steps_info.append(f"Left remaining: {left_arr[i]}")
                i += 1
                k += 1

            while j < len(right_arr):
                items[k] = right_arr[j]
                steps_info.append(f"Right remaining: {right_arr[j]}")
                j += 1
                k += 1
        return items, steps_info

    @staticmethod
    def sort_sizes(items, path, order):
        steps_info = []
        if len(items) > 1:
            mid = len(items) // 2
            left_arr = items[:mid]
            right_arr = items[mid:]

            MergeSort.sort_sizes(left_arr, path, order)
            MergeSort.sort_sizes(right_arr, path, order)

            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                file1 = os.path.join(path, left_arr[i])
                file2 = os.path.join(path, right_arr[j])
                size1 = os.path.getsize(file1)
                size2 = os.path.getsize(file2)

                if order == "오름차순":
                    if size1 <= size2:
                        items[k] = left_arr[i]
                        steps_info.append(f"{left_arr[i]} <= {right_arr[j]}: {left_arr[i]}")
                        i += 1
                    else:
                        items[k] = right_arr[j]
                        steps_info.append(f"{left_arr[i]} > {right_arr[j]}: {left_arr[i]}")
                        j += 1
                else:
                    if size1 >= size2:
                        items[k] = left_arr[i]
                        steps_info.append(f"{left_arr[i]} >= {right_arr[j]}: {left_arr[i]}")
                        i += 1
                    else:
                        items[k] = right_arr[j]
                        steps_info.append(f"{left_arr[i]} < {right_arr[j]}: {left_arr[i]}")
                        j += 1
                k += 1

            while i < len(left_arr):
                items[k] = left_arr[i]
                steps_info.append(f"Left remaining: {left_arr[i]}")
                i += 1
                k += 1

            while j < len(right_arr):
                items[k] = right_arr[j]
                steps_info.append(f"Right remaining: {right_arr[j]}")
                j += 1
                k += 1
        return items, steps_info

    @staticmethod
    def sort_dates(items, path, order):
        steps_info = []
        if len(items) > 1:
            mid = len(items) // 2
            left_arr = items[:mid]
            right_arr = items[mid:]

            MergeSort.sort_dates(left_arr, path, order)
            MergeSort.sort_dates(right_arr, path, order)

            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                file1 = os.path.join(path, left_arr[i])
                file2 = os.path.join(path, right_arr[j])
                date1 = os.path.getctime(file1)
                date2 = os.path.getctime(file2)

                if order == "오름차순":
                    if date1 <= date2:
                        items[k] = left_arr[i]
                        steps_info.append(f"{left_arr[i]} <= {right_arr[j]}: {left_arr[i]}")
                        i += 1
                    else:
                        items[k] = right_arr[j]
                        steps_info.append(f"{left_arr[i]} > {right_arr[j]}: {left_arr[i]}")
                        j += 1
                else:
                    if date1 >= date2:
                        items[k] = left_arr[i]
                        steps_info.append(f"{left_arr[i]} >= {right_arr[j]}: {left_arr[i]}")
                        i += 1
                    else:
                        items[k] = right_arr[j]
                        steps_info.append(f"{left_arr[i]} < {right_arr[j]}: {left_arr[i]}")
                        j += 1
                k += 1

            while i < len(left_arr):
                items[k] = left_arr[i]
                steps_info.append(f"Left remaining: {left_arr[i]}")
                i += 1
                k += 1

            while j < len(right_arr):
                items[k] = right_arr[j]
                steps_info.append(f"Right remaining: {right_arr[j]}")
                j += 1
                k += 1
        return items, steps_info
