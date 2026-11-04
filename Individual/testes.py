List1 = [1, 2, 3, 4, 5, 6]
List2 = [7, 8, 9, 10, 11, 12]

def zipper_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]
def zipper_product(list1, list2):
    return [x * y for x, y in zip(list1, list2)]

i = 0
for item in zipper_sum(List1, List2):
    print(f'the sum of {List1[i]} and {List2[i]} is {item}')
    i += 1


