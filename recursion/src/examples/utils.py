#sum_to_one()
def sum_to_one(n):
  if n == 1:
    return n
  else:
    print("Recursing with input: {0}".format(n))
    return n + sum_to_one(n-1)
#test sum_to_one()
print(sum_to_one(7))

#factorial()
def factorial(n):
  if n == 1:
    return n
  return n*factorial(n-1)
#test factorial()
print(factorial(12))

#flatten()
def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result
###for testing
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

#binary tree
def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"

    middle_index = len(my_list) // 2
    middle_value = my_list[middle_index]

    print("Middle index: {0}".format(middle_index))
    print("Middle value: {0}".format(middle_value))

    tree_node = {"data": middle_value}
    tree_node["left_child"] = build_bst(my_list[: middle_index])
    tree_node["right_child"] = build_bst(my_list[middle_index + 1:])

    return tree_node
#test
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)