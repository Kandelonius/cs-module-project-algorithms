'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # create a dictionary
    dict = {}
    # iterate through the array and once I see a number check to see if
    for elem in arr:
        if dict.__contains__(elem):
            dict[elem] += 1
        else:
            dict[elem] = 1
    for key in dict:
        if dict[key] == 1:
            return key


    # it already exists in the dictionary and if it doesn't add it to the dictionary
    # if it does exist increment a counter associated with that dictionary entry.

    # pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")