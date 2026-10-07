"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining

def preparation_time_in_minutes(layer_count):
    """Calculates the preparation time for layering the cake.

    Parameters:
        layer_count (int): The amount of layers to be made

    Returns:
        int: The amount of minutes to prepare the layers

    Function that takes the amount of layers to be done on the cake, and returns how
    many minutes does it take to prepare these layers.
    """

    layer_minutes = layer_count * PREPARATION_TIME
    return layer_minutes


#TODO (student): define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layer_count, elapsed_bake_time):
    """ Calculates for the time (in minutes) that the lasagna had been
    in the oven and the time it took to prepare the layers.

    Parameters:
        layer_count (int): The amount of layers to be made
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total amount of time (in minutes) that the lasagna has been in the oven and the time it took to prepare the layers.

    Function that takes the amount of layers to be done on the cake,
    and the actual minuntes the lasagna had been baking, and returns
    the total amount of time in minutes that the lasagna has been in
    the oven for.
    """

    total_time = elapsed_bake_time + (layer_count * PREPARATION_TIME)
    return total_time