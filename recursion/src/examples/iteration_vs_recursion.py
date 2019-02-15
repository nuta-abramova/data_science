def factorial(n):
  result = 1
  while n > 0:
    result = result * n
    n = n - 1
  return result

def fibonacci(n):
  fibs = [0, 1]
  if(n <= len(fibs) - 1):
    return fibs[n]
  else:
    while n > len(fibs)-1:
      next_fib = fibs[-1] + fibs[-2]
      fibs.append(next_fib)
    return fibs[n]

def sum_digits(n):
  if n <=0:
    return 0
  while n > 0:
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)

def find_min(my_list, min=None):
  if len(my_list) == 0:
    return min
  else:
    if min == None or my_list[0] < min:
      min = my_list[0]
  return find_min(my_list[1:], min)

def is_palindrome(input_string):
  if len(input_string) < 2:
    return True
  if input_string[0] != input_string[-1]:
    return False
  return is_palindrome(input_string[1:-1])

def multiplication(n, m):
  if n == 0 or m == 0:
    return 0
  return n + multiplication(n, m-1)

def depth(tree):
  if not tree:
    return 0

  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])

  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1

# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node
