# Part B: Bug Hunt - Fixed version

total = 0
count = 1

# BUG 1: Missing colon after while condition - original was 'while count < 5' without colon
# BUG 2: Wrong loop condition - original was 'count < 5' which only sums 1-4. Must be '<= 5' to get 15
while count <= 5:
    total = total + count
    count = count + 1

# BUG 3: Print was inside loop and showed wrong intermediate total. Must be outside loop.
print(f"Sum of 1 to 5 is: {total}")
