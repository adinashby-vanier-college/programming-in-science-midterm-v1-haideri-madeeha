import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    import math

    area = math.pi * (radius ** 2)
    result = round(area, 2)

    return result

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""

    if n < 4:
        result = "The triangle height should be at least 4."

    else:
        for i in range(n):
            if i == 0 or i == n - 1:
                result += (i + 1) * "*"
                result += "\n"

            else:
                result += "*" + " " * (i - 1) + "*"
                result += "\n"

    return result.rstrip()

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    
    if n < 3:
        result = "The pyramid height should be at least 3."

    else:
        for i in range(n):
            for j in range(i):
                result += " "

            for k in range(((5 + 2 * (n - 3)) - (2 * i))):
                result += "*"
        
            result += "\n"

    return result.rstrip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()