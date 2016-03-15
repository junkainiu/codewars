def exp_sum(n,n):
    if n == 1:
        return 1
    if start > n:
        return exp_sum(n,n)
    sum = 0
    for i in xrange(1,start):
        sum += exp_sum(n-i, i)
    print sum
    return sum
exp_sum(3,1)
