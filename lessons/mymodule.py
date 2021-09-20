# Import numpy once at the start!
import numpy as np

# Define the function here
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

def only_evens_numpy(list_of_numbers):
    """Take a numpy array of numbers and return a numpy array of the even values."""
    
    # Make sure the list of numbers is an array
    array_of_numbers = np.array(list_of_numbers)
    
    # Find the even numbers in the array
    evens_mask = array_of_numbers % 2 == 0
    
    # Apply mask to list of numbers to get only evens
    even_numbers_array = array_of_numbers[evens_mask]
    
    # Then return array of even numbers
    return even_numbers_array