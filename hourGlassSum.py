# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def hourglassSum(arr):
    maxNum = 'null'
    row = 0
    col = 0

    intArray = []
    for round in range(1,17,1):
        # Row Loop
        for x in range(0,3,2):
            # Column loop
            for y in range(3):
                intArray.append(arr[row+x][col+y])
        
        intArray.append(arr[row+1][col+1])
        print(intArray)
        
        if maxNum=='null':
            maxNum = sum(intArray)

        elif maxNum<sum(intArray):
            maxNum = sum(intArray)
        intArray = []
        if(round>0 and round%4 == 0):
            row = row + 1
            col=0
        else:
            col = col+1
    return maxNum


arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]]

print(hourglassSum(arr))


arr = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]
print(hourglassSum(arr))