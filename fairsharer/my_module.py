"""Documentation about the fairsharer module."""


# FIXME: put actual code here
def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.

    -In each iteration the largest value in the list gives 
    a part of its value to its left and right neighbor
    -The list is circular so the first and last elements are also neighbors 
    

    Examples:
        fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
        fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Args:
        values:
            list of numeric values
        num_iterations:
            number of times the redistribution is repeated
        share:
            fraction of the max value given to each neighbor

    Returns:
        list of values after redistribution
    """
    values = list(values)

    if len(values) == 0:
        return values

    for _ in range(num_iterations):
        values_new = values.copy()

        max_index = values.index(max(values))
        max_value = values[max_index]

        amount = share * max_value

        left_index = (max_index - 1) % len(values)
        right_index = (max_index + 1) % len(values)

        values_new[max_index] -= 2 * amount
        values_new[left_index] += amount
        values_new[right_index] += amount

        values = values_new

    return values
