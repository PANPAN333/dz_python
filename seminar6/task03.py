def print_operation_table(operation, rows = 21, cols = 20):
    for i in range(1, rows + 5):
        for j in range(1, cols + 7):
            print(operation(i, j), end='\t')
        print()            

print_operation_table(lambda x, y: x * y, 5, 3)