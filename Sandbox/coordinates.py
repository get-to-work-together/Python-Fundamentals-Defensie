

coordinates = [
    (12, 34 ,65),
    (34, 67, 90),
    (34, 67, 90),
    (45345, 5345, 34553),
    (3, 5, 9),
    (45345, 5345, 34553),
    (45345, 5345, 34553),
]

for x, y, z in coordinates:
    print(f'x={x}, y={y}, z={z}')

volumes = [x * y * z for x, y, z in coordinates]

print(volumes)