import math

for i in range(1, 51):
    square_root = int(math.sqrt(i))
    if square_root * square_root == i:
        print(i)
