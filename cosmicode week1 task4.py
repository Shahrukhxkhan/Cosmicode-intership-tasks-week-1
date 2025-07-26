# Task 4: Area of Complex Shapes (Improved Interactive Version)
import math

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

# Ask user which shape to calculate
print("Select a shape to calculate area:")
print("1. Trapezoid")
print("2. Ellipse")
choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    # Get trapezoid dimensions
    print("\nEnter trapezoid dimensions:")
    base1 = float(input("First base length: "))
    base2 = float(input("Second base length: "))
    height = float(input("Height: "))
    area = trapezoid_area(base1, base2, height)
    print(f"\nArea of trapezoid: {area:.2f}")
    
elif choice == '2':
    # Get ellipse dimensions
    print("\nEnter ellipse dimensions:")
    major_axis = float(input("Major axis length: "))
    minor_axis = float(input("Minor axis length: "))
    area = ellipse_area(major_axis, minor_axis)
    print(f"\nArea of ellipse: {area:.2f}")
    
else:
    print("Invalid choice! Please select either 1 or 2.")