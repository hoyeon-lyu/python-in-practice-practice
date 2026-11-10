n = int(input())

dots = []
for _ in range(n):
    name, x, y = input().split(" ")
    x, y = int(x), int(y)
    distance_square = x**2 + y**2
    dots.append((distance_square, name, x, y))

dots.sort()

for rank, (distance_square, name, x, y) in enumerate(dots, start=1):
    print(f"{rank}. {name} ({x}, {y}) d2={distance_square}")
    if rank == n:
        farthest_name = name

print(f"farthest: {farthest_name}")

x_list = []
y_list = []
for _, _, x, y in dots:
    x_list.append(x)
    y_list.append(y)

print(f"box: ({min(x_list)}, {min(y_list)}) ~ ({max(x_list)}, {max(y_list)})")