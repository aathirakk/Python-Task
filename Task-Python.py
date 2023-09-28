rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
print("Enter the matrix content row by row:")
for _ in range(rows):
    row = input()
    matrix.append(row)

result = ' '.join([''.join([char if char.isalnum() else ' ' for char in col]) for col in zip(*matrix)])

print("Processed Matrix:")
print(result)