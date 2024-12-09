def largest_rectangle_area(heights):
    stack = []  # To store indices
    max_area = 0
    n = len(heights)

    for i in range(n):
        # Maintain ascending order in stack
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    # Compute area for remaining bars in stack
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# Test
histogram = [2, 1, 5, 6, 2, 3]
print("Largest Rectangle Area:", largest_rectangle_area(histogram))
