y_values = [3, 4, 5, 6, 7, 8]
dx = 1

total_area = 0

# add first point
y_values.insert(0, 0)
for i in range(1, len(y_values)):
    # a trapezoid is formed with B = y_values[i - 1] and b = y_values[i]
    trapezoid_area = (1/2) * (y_values[i] + y_values[i-1]) * dx

    # add all trapezoids
    total_area += trapezoid_area

print("Area: ", total_area)
