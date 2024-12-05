def is_magic_square(square):
    size = int(len(square) ** 0.5)
    if size * size != len(square):
        return False  # Not a perfect square

    def get_row(square, row):
        return square[row * size:(row + 1) * size]

    def get_column(square, col):
        return [square[col + size * i] for i in range(size)]

    def get_diagonals(square):
        main_diagonal = [square[i * (size + 1)] for i in range(size)]
        anti_diagonal = [square[(i + 1) * (size - 1)] for i in range(size)]
        return main_diagonal, anti_diagonal

    def all_sums_equal(lst):
        return all(x == lst[0] for x in lst)

    rows_sums = [sum(get_row(square, i)) for i in range(size)]
    cols_sums = [sum(get_column(square, i)) for i in range(size)]
    main_diagonal, anti_diagonal = get_diagonals(square)
    diagonals_sums = [sum(main_diagonal), sum(anti_diagonal)]

    all_sums = rows_sums + cols_sums + diagonals_sums

    return all_sums_equal(all_sums)

# Example usage:
square = list(map(int, input("Enter the elements of the square: ").split(", ")))
print(is_magic_square(square))  # Output: True