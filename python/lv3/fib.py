def mul(a, b):
  r = [[0, 0], [0, 0]]
  r[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
  r[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1];
  r[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0];
  r[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1];
  return r;

# 递归加速计算斐波那契数列 O(n^2) -> O(logn)
def fib(n):
  if n == 0:
    return [[1, 0], [0, 1]]
  if n == 1:
    return [[1, 1], [1, 0]]
  if n % 2 == 0 :
    return mul(fib(int(n / 2)), fib(int(n / 2)))
  else:
    return mul(mul(fib(int(n / 2)), fib(int(n / 2))), [[1, 1], [1, 0]])
