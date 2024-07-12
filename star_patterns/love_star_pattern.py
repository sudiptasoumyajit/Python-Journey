def love_star_pattern(size):
    for i in range(size//2, size, 2):
        for j in range(1, size-i, 2):
            print(" ", end="")
        for j in range(1, i+1, 1):
            print("*", end="")
        for j in range(1, size-i+1, 1):
            print(" ", end="")
        for j in range(1, i+1, 1):
            print("*", end="")
        print()

    for i in range(size,0,-1):
        for j in range(i, size, 1):
            print(" ", end="")
        for j in range(1, i*2, 1):
            print("*", end="")
        print()

# Example usage:
love_star_pattern(6)