# Que 1
# problem statement 2
'''
Write a Javascript, Python, or OCaml program that:
-accepts a list of integers
-emits an error message if the list is not a multiple of 10 in length
-returns or prints a list of integers based on the input list, but with items at positions which are a multiple of 2 or 3 removed
Host your program at a public git-based repository and include robust testing for your program. 
'''

def get_input_integer_list():
    """
    Get a list of integers from user input.
    """
    try:
        user_input = input().split()
        int_list = [int(i) for i in user_input]
        return int_list
    except ValueError as ve:
        print("Invalid Input. Please enter integers only.")
        print(ve)

def is_length_divisible_by_10(lst):
    """
    Check if the length of the list is divisible by 10.
    """
    if len(lst) % 10 == 0:
        return True
    return False

def get_values_at_indices_divisible_by_2_3(lst):
    """
    Get a list of values at positions divisible by 2 or 3.
    This function follows 0 based indexing
    """
    return [value for idx, value in enumerate(lst) if idx % 2 == 0 or idx % 3 == 0]

def main():
    """
    Main function to execute the program.
    """
    try:
        input_list = get_input_integer_list()
        if not is_length_divisible_by_10(input_list):
            raise ValueError("List length is not divisible by 10")
            return
        result = get_values_at_indices_divisible_by_2_3(input_list)
        print(result)
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()
