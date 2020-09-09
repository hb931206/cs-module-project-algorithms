'''
Input: a List of integers
Returns: a List of integers
'''
# https://www.w3resource.com/python-exercises/
# challenges/1/python-challenges-1-exercise-27.php <---- Ref


def moving_zeroes(arr):
    # Your code here

    a = [0 for i in range(arr.count(0))]
    x = [i for i in arr if i != 0]
    x.extend(a)
    return(x)


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
