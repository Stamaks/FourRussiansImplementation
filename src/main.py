from lib.matrices_multiplication import run_four_russians


# TODO: Add README
# TODO: проверить на асимптотику


def get_matrix(size_n):
    matrix = [list(map(int, input().split())) for _ in range(size_n)]
    check_boolean = all(i == 0 or i == 1 for row in matrix for i in row)
    check_size = all(len(row) == size_n for row in matrix)
    return matrix if check_boolean and check_size else None


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    print('Welcome to the 4 Russians algorithm implementation!')
    print('NOTE: The algorithm works only with boolean square matrices!')

    while(True):
        size_n = 0
        while size_n <= 0:
            print('Each matrix size is n x n, enter n (just one integer number):')
            try:
                size_n = int(input())
            except Exception:
                pass

        matrix_a = None
        while not matrix_a:
            print(f'Please, enter the first boolean matrix, size {size_n} x {size_n}:')
            try:
                matrix_a = get_matrix(size_n)
            except Exception:
                pass

        print('The first matrix is:')
        print_matrix(matrix_a)

        matrix_b = None
        while not matrix_b:
            print(f'Enter the second boolean matrix, size {size_n} x {size_n}:')
            try:
                matrix_b = get_matrix(size_n)
            except Exception:
                pass

        print('The second matrix is:')
        print_matrix(matrix_b)

        final_matrix = run_four_russians(matrix_a, matrix_b, size_n)
        print('The final matrix is:')
        print_matrix(final_matrix)

        answer = None
        while answer != 'y':
            print('Want to run the algorithm again? Enter y/n')
            try:
                answer = input()
                if answer == 'n':
                    exit(0)
            except Exception:
                pass

