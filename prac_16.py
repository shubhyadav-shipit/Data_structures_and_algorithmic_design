# Program to compare Insertion Sort and Merge Sort based on execution time

import time

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

arr1 = arr.copy()
arr2 = arr.copy()

# Measure Insertion Sort time
start = time.time()
insertion_sort(arr1)
end = time.time()

print("\nInsertion Sort Result:", arr1)
print("Execution Time:", end - start, "seconds")

# Measure Merge Sort time
start = time.time()
merge_sort(arr2)
end = time.time()

print("\nMerge Sort Result:", arr2)
print("Execution Time:", end - start, "seconds")