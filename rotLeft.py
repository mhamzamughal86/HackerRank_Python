# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

def rotLeft(a, d):
    arr1 = arr[0:rot]
    arr2 = arr[rot:]
    return arr2+arr1



arr = [1, 2, 3, 4, 5]
rot = 4
print(rotLeft(arr,rot))