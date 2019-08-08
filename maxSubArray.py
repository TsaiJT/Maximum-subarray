def maxSubArray(nums):

    max_here_ending, max_so_far = 0, 0

    for x in nums:
        max_here_ending += x
        if(max_here_ending < 0):
            max_here_ending = 0
        
        if(max_so_far < max_here_ending):
            max_so_far = max_here_ending

    if max_so_far > 0:
        return max_so_far
    else:
        return max(nums)


def main():

    s = [-3, -2]
    result = maxSubArray(s)
    print(result)
    

if __name__ == '__main__':
    main()