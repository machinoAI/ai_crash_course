
num = [1,3,6,4,6,8,7,0,9]
maximum_product_pair = (8,9) #==> 72

def max_product(arr):
    array_length = len(arr)

    if array_length <2:
        print("No such pair found in the give array!")
        return

    a= arr[0]
    b= arr[1]

    for i in range(0, array_length):
        for j in range(i+1, array_length):
            if (num[i]*num[j]) > a*b:
                a = arr[i]
                b = arr[j]
    return a, b

print("Maximum product pair:", max_product(num))

