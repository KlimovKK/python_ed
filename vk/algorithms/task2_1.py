def counts_unequal_elements(sample_array, element):
    count = 0
    for el in sample_array:
        if element != el:
            count += 1

    return count


size = int(input())
sample_array = [int(num) for num in input().split()]
element = int(input())

print(counts_unequal_elements(sample_array, element))
