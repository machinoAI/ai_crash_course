def merge_arrays(arr1, arr2):

    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0

    result = []

    while i < m and j < n:

        if arr1[i] < arr2[j]:

            result.append(arr1[i])
            i +=1

        else:
            result.append(arr2[j])
            j +=1

    while i < m:
        result.append(arr1[i])
        i +=1

    while j < n:
        result.append(arr2[j])
        j +=1

    return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

print(merge_arrays(arr1, arr2))
