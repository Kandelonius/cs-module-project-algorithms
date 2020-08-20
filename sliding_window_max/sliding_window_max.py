'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def find_max(arr):
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max

def sliding_window_max(nums, k):
    length = len(nums) - k
    # create the output array
    output = [0] * (length + 1)
    # create an array to fill when calling a get max method
    max_finder = []
    # create variable n to keep track of the bottom of the range for the window
    n = 0
    # create max holder to be adjusted as needed
    # max = 0
    # create boolean to be set to false after the first evaluation to account for negative max
    first = True
    # iterate through nums array using range n through k
    for items in nums[n:length + 1]:
        # if first == True:
        max_finder = nums[n:n + k]
        output[n] = (find_max(max_finder))
        n += 1
    return output

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
