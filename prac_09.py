# Python program to demonstrate row major order

def demonstrate_row_major():
    matrix = [
        [8, 9, 10],
        [11, 12, 13],
        [14, 15, 16]
    ]

    rows = 3
    cols = 3

    flat_memory = []

    print("Logical 2D Matrix View:")
    for row in matrix:
        print(row)

    # Row major traversal
    for i in range(rows):
        for j in range(cols):
            flat_memory.append(matrix[i][j])

    print("\nRow Major Order (Flat Memory):")
    print(flat_memory)

print("Demonstrating Row Major Order:")
demonstrate_row_major()

