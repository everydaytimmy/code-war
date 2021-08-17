# MOVING ZEROS TO THE END

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    new = []
    zeros = []
    
    for i in range(len(array)):
        if array[i] == 0:
            zeros.append(array[i])
        else:
            new.append(array[i])
    
    return new + zeros


# Original attempt - Did not work I believe because of the way .remove() works

# def move_zeros(array):
#     zeros = []
    
#     for i in array:
#         if i == 0:
#             array.remove(i)
#             zeros.append(i)
    
#     return array + zeros