'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # create an array to hold the multiplied numbers
    multiplied = []
    total = 1
    iterations = 0
    # move through the original array and multiply all of the numbers together
    for item in arr:
        print(f"item is {item} and total is {total} arr[iterations] is {arr[iterations]}")
        total *= arr[iterations]
        iterations += 1
    # fill the new array with numbers dividing by the element in that position of the first array
    for item in arr:
        multiplied.append(total / item)
    return multiplied



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
