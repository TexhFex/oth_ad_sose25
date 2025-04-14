def mergesort(a): # mergesort hat O(n log n)
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def gibt_es_zwei_elemente_fuer_summe(a, s):
    sorted_a = mergesort(a)

    left = 0
    right = len(sorted_a) - 1

    while left < right:
        current_sum = sorted_a[left] + sorted_a[right]
        if current_sum == s:
            return True # Paar gefundn
        elif current_sum < s:
            left += 1
        else:
            right -= 1

    return False  # Kein Paar gefunden


if __name__ == "__main__":
    test_liste = [0, 1, 6, 8, 9, 18] # True: 0+6
    #test_liste = [0, 1, 2, 3, 8, 9] # False
    s = 6
    if gibt_es_zwei_elemente_fuer_summe(test_liste, s):
        print("true")
    else:
        print("false")
