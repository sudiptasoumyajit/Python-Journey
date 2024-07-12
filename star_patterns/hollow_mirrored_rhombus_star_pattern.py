
def hollow_mirrored_rhombus_star_pattern(n):
    for i in range(n):
        for j in range(i):
            print(' ', end=' ')
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

hollow_mirrored_rhombus_star_pattern(5)
