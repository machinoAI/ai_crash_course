"""
Given two sorted arrays a[] and b[] of size n and m respectively,
    the task is to merge them in sorted order without using any extra space.
    Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements.

    Input: a[] = [2, 4, 7, 10], b[] = [2, 3] Output: a[] = [2, 2, 3, 4], b[] = [7, 10]

"""

def merge_sorted_array(a, b):

    n = len(a)
    m = len(b)

    i = n-1
    j = 0


    while i >= 0 and j < m:

        if a[i] > b[j]:

            a[i] , b[j] = b[j], a[i]

            i -=1
            j +=1

        else:
            break

    a.sort()
    b.sort()
    return a, b
a= [2, 4, 7, 10]
b = [2, 3]

print(merge_sorted_array(a, b))


# Gap Method:

def merge_sorted_arrays(a, b):

    n = len(a)
    m = len(b)

    total = n + m

    # Initial gap
    gap = (total + 1) // 2

    while gap > 0:

        i = 0

        while i + gap < total:

            j = i + gap

            # Case 1: both elements are in a
            if i < n and j < n:

                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

            # Case 2: i in a, j in b
            elif i < n and j >= n:

                j_b = j - n

                if a[i] > b[j_b]:
                    a[i], b[j_b] = b[j_b], a[i]

            # Case 3: both elements are in b
            else:

                i_b = i - n
                j_b = j - n

                if b[i_b] > b[j_b]:
                    b[i_b], b[j_b] = b[j_b], b[i_b]

            i += 1

        # Reduce gap
        if gap == 1:
            break

        gap = (gap + 1) // 2


a = [2, 4, 7, 10]
b = [2, 3]

merge_sorted_arrays(a, b)

print(a)
print(b)