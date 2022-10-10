def run(a):
    max_sum = None
    cur_sum = 0
    for i in range(len(a)):
        cur_sum += a[i]
        if cur_sum > max_sum or max_sum is None:
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0

    return max_sum
