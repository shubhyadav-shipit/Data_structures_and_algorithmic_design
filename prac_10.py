#Python program to demonstrate column major order

def demonstrate_column_major():
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

    # Column major traversal
    for j in range(cols):
        for i in range(rows):
            flat_memory.append(matrix[i][j])

    print("\nColumn Major Order (Flat Memory):")
    print(flat_memory)

print("Demonstrating Column Major Order:")
demonstrate_column_major()