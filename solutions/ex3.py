n = int(input())

product_table = [[(i+1)*(j+1) for i in range(n)] for j in range(n)]
diagonal = [product_table[i][i] for i in range(n)]
odd_count = len([product_table[i][j] for i in range(n) for j in range(n) if not product_table[i][j] % 2 == 0])

f_diagonal = " ".join(list(map(str,diagonal)))

print("\n".join([" ".join(list(map(str,product_table[i]))) for i in range(n)]))
print(f"diagonal: {f_diagonal}")
print(f"odd_count: {odd_count}")