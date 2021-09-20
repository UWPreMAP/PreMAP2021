import numpy as np

def only_evens_numpy(list_of_numbers):
    """Take a list of numbers, and return a list of only the even numbers"""

    array_of_numbers = np.array(list_of_numbers)
    evens = array_of_numbers % 2 == 0
    even_numbers = array_of_numbers[evens]
    
    # Then return the number
    return even_numbers

def only_evens(list_of_numbers):
    """Take a list of numbers, and return a list of only the even numbers"""

    # This is an empty list that we'll append the even numbers onto
    even_numbers = []

    # Go through each number in the list of numbers
    for number in list_of_numbers:

        # If this number is an even number:
        if number % 2 == 0:

            # Append it to the list of even numbers
            even_numbers.append(number)

    # Then return the number
    return even_numbers