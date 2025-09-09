def left_rotate(arr, d):
    n = len(arr)
    d = d % n
    arr1=arr[d:] + arr[:d]
    print(f"After {d} rotations")
    print(arr1)

left_rotate([1,2,3,4],1)