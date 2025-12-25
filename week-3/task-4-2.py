# (x - a)^2 + (y - b)^2 <= R^2
# dots inside the circle


def is_inside(x, y, a, b, R):
    return (x - a) ** 2 + (y - b) ** 2 <= R ** 2

#circle
a = float(input("Circle x point: "))
b = float(input("Circle y point: "))
R = float(input("Circle radius: "))

points = []

for name in ["P", "F", "L"]:
    coords = input(name + " cords: ").split()
    x = float(coords[0])
    y = float(coords[1])
    points.append((x, y))


count = 0

for x, y in points:
    if is_inside(x, y, a, b, R):
        count += 1

print("Points inside:", count)
