'''
Input: an integer
Returns: an integer
'''
dict = {0: 1, 1: 1}

def eating_cookies(n):
    global count
    pass
    # create a dictionary to hold values that I know so I don't need to move down
    # each tree if I've already been down a tree of that number.
    ## contains then add that number to count
    if dict.__contains__(n):
        return dict[n]
    ## if n is 0
    else:
        count = 1
        count += eating_cookies(n - 1)
        dict[n] = count
        return dict[n]
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
