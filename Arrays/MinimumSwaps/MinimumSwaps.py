# not an optimized solution, will fail some test cases

def minimumSwaps(arr):
    swaps = 0
    for i in range(int(len(arr))-1,-1,-1):
        if arr[i] != i+1:
            for itemR in range(i,-1,-1):
                if arr[itemR] == i+1:
                    arr[itemR],arr[i] = arr[i],arr[itemR]
                    swaps += 1
                    break
    return swaps
