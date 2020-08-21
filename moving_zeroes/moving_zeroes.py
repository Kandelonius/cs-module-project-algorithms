'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # create a second array and put the non zero number at the front
    # and the zeroes at the back
    moving = [0] * len(arr)
    num = 0
    # moving[num] = [elem for elem in arr if elem != 0]
    for elem in arr: # .o4s
        if elem != 0:
            moving[num] = elem
            num += 1
    return moving


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")