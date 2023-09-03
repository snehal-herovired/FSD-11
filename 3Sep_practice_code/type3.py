# Array Initialization:

# Create an empty Python list and populate it with integers from 1 to 10 using a loop. Print the resulting array.
# Array Slicing:

# Given an array of integers, write Python code to extract a subarray containing elements from index 2 to 5 (inclusive). Print the subarray.
# Array Sum:

# Write a Python function that calculates the sum of all the elements in an array of integers. Test it with an example array.
# Array Maximum:

# Find the maximum value in an array of integers using Python. Print both the maximum value and its index.
# Array Reversal:

# Write Python code to reverse an array of integers in-place, without using any additional data structures.
# Array Sorting:

# Sort an array of integers in ascending order using Python's built-in sorting function. Print the sorted array.
# Array Search:

# Write a Python function to search for a specific integer in an array. Return the index if found, or -1 if not found.
# Array Concatenation:

# Create two arrays of integers and concatenate them into a single array using Python. Print the concatenated array.
# Array Removal:

# Given an array of integers, remove all occurrences of a specific value using Python. Print the modified array.
# Array Unique Elements:

# Write Python code to remove duplicate elements from an array of integers while preserving the order of the remaining elements. Print the modified array 

# Array Initialization
my_array = []
for i in range(1, 11):
    my_array.append(i)
print("Initialized Array:", my_array)

# Array Slicing
original_array = [10, 20, 30, 40, 50, 60, 70, 80]
subarray = original_array[2:6]
print("Subarray:", subarray)

# Array Sum
def array_sum(arr):
    return sum(arr)

example_array = [1, 2, 3, 4, 5]
sum_result = array_sum(example_array)
print("Sum of Array Elements:", sum_result)

# Array Maximum
def find_max(arr):
    if not arr:
        return None
    max_value = max(arr)
    max_index = arr.index(max_value)
    return max_value, max_index

max_value, max_index = find_max(example_array)
print(f"Maximum Value: {max_value}, Index: {max_index}")

# Array Reversal
def reverse_array(arr):
    arr.reverse()

reverse_array(example_array)
print("Reversed Array:", example_array)

# Array Sorting
unsorted_array = [4, 2, 7, 1, 9, 5]
sorted_array = sorted(unsorted_array)
print("Sorted Array:", sorted_array)

# Array Search
def search_element(arr, target):
    if target in arr:
        return arr.index(target)
    return -1

target_value = 7
index = search_element(sorted_array, target_value)
print(f"Index of {target_value}:", index)

# Array Concatenation
array1 = [1, 2, 3]
array2 = [4, 5, 6]
concatenated_array = array1 + array2
print("Concatenated Array:", concatenated_array)

# Array Removal
def remove_element(arr, target):
    return [x for x in arr if x != target]

array_to_remove_from = [1, 2, 2, 3, 4, 2, 5]
value_to_remove = 2
filtered_array = remove_element(array_to_remove_from, value_to_remove)
print("Filtered Array:", filtered_array)

# Array Unique Elements
def remove_duplicates(arr):
    unique_list = []
    for item in arr:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

array_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_elements = remove_duplicates(array_with_duplicates)
print("Unique Elements:", unique_elements)
