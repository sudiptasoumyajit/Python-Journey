
def hollow_mirrored_right_triangle_star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == n or j == n - i + 1 or i == n:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

hollow_mirrored_right_triangle_star_pattern(5)
