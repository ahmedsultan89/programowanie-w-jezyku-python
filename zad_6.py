def merge_and_cube(list1: list[int], list2: list[int]) -> list[int]:
    combined = list(set(list1 + list2))  # remove duplicates
    return [x**3 for x in combined]


result = merge_and_cube([1, 2, 3], [2, 3, 4])
print(result)
