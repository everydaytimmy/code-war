# In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))


###------ Over The Road ------###

#  You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:

def over_the_road(address, n):
    distance = (2*n) + 1
    return distance - address
