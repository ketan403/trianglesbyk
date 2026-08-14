import math

def get_integer_input(prompt):
    """Get a valid integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("❌ Side length must be a positive integer. Try again.")
            else:
                return value
        except ValueError:
            print("❌ Invalid input. Please enter an integer. Try again.")

def is_valid_triangle(a, b, c):
    """Check if three sides form a valid triangle."""
    return (a + b > c) and (b + c > a) and (a + c > b)

def classify_by_sides(a, b, c):
    """Classify triangle based on sides."""
    if a == b == c:
        return "Equilateral Triangle 🔺"
    elif a == b or b == c or a == c:
        return "Isosceles Triangle 🔷"
    else:
        return "Scalene Triangle 🔸"

def classify_by_angles(a, b, c):
    """Classify triangle based on angles using cosine rule."""
    # Square of sides
    a2, b2, c2 = a**2, b**2, c**2

    # Find the largest side to check the largest angle
    sides_squared = sorted([a2, b2, c2])
    sum_of_two = sides_squared[0] + sides_squared[1]
    largest = sides_squared[2]

    if sum_of_two == largest:
        return "Right-Angled Triangle 📐 (90°)"
    elif sum_of_two < largest:
        return "Obtuse Triangle 📏 (one angle > 90°)"
    else:
        return "Acute Triangle ✅ (all angles < 90°)"

def calculate_angles(a, b, c):
    """Calculate all three angles in degrees."""
    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_C = 180 - angle_A - angle_B
    return angle_A, angle_B, angle_C

def calculate_area(a, b, c):
    """Calculate area using Heron's formula."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# ─────────────────────────────────────────────
#               MAIN PROGRAM
# ─────────────────────────────────────────────

print("=" * 45)
print("        🔺 TRIANGLE CHECKER 🔺")
print("=" * 45)

# Take input
a = get_integer_input("Enter side 1: ")
b = get_integer_input("Enter side 2: ")
c = get_integer_input("Enter side 3: ")

print("-" * 45)
print(f"📥 Input Sides: a = {a}, b = {b}, c = {c}")
print("-" * 45)

# Validate triangle
if not is_valid_triangle(a, b, c):
    print("❌ INVALID TRIANGLE!")
    print("   The sum of any two sides must be greater")
    print("   than the third side.")
    print(f"   {a} + {b} > {c} : {a + b > c}")
    print(f"   {b} + {c} > {a} : {b + c > a}")
    print(f"   {a} + {c} > {b} : {a + c > b}")
else:
    print("✅ VALID TRIANGLE!")
    print()

    # Classification
    side_type  = classify_by_sides(a, b, c)
    angle_type = classify_by_angles(a, b, c)

    print(f"📐 Type by Sides  : {side_type}")
    print(f"📏 Type by Angles : {angle_type}")
    print()

    # Angles
    A, B, C = calculate_angles(a, b, c)
    print(f"📊 Angles:")
    print(f"   Angle A (opposite to side {a}) = {A:.2f}°")
    print(f"   Angle B (opposite to side {b}) = {B:.2f}°")
    print(f"   Angle C (opposite to side {c}) = {C:.2f}°")
    print()

    # Area & Perimeter
    area      = calculate_area(a, b, c)
    perimeter = a + b + c
    print(f"📐 Perimeter : {perimeter}")
    print(f"📐 Area      : {area:.2f} square units")

print("=" * 45)
