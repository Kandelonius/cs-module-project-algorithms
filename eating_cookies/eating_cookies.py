'''
Input: an integer
Returns: an integer
'''
dict = {0: 1, 1: 1, 2: 2}
def eating_cookies(n):
    # global count
    # create a dictionary to hold values that I know so I don't need to move down
    # each tree if I've already been down a tree of that number.
    ## contains then add that number to count
    # if dict.__contains__(n):
    #     return dict[n]
    # ## if n is 0
    # else:
    #     count = 1
    #     count += eating_cookies(n - 1)
    #     dict[n] = count
    #     return dict[n]
    ### trying something based on pattern recognition and not figuring out the process
    ### it appears eating_cookies(n) is a summation of the previous 3 options
    index = 3
    for thing in range(index, n + 1):
        dict[thing] = dict[index - 1] + dict[index - 2] + dict[index - 3]
        index += 1
    return dict[n]

        # Use the main function here to test out your implementation


if __name__ == "__main__":
    num_cookies = 6
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
