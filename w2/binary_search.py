def binary_search(needle, haystack):
    lo = 0
    hi = len(haystack)

    # so 'hi - lo' is how many numbers we still have to check

    while lo < hi:
        mid = ((hi - lo) // 2) + lo
        print(lo, hi , mid, haystack[mid])

        if needle == haystack[mid]:
            return mid
        elif needle < haystack[mid]:    # go left
            hi = mid
        else:
            lo = mid + 1
    return None

