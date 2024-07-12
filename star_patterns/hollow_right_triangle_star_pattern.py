
def hollow_right_triangle_star_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i == n or j == 1 or j == i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

hollow_right_triangle_star_pattern(5)
