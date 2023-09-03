# Array Initialization:

# Create an empty list in Python and add elements to it to create an array of integers. Demonstrate how to append, insert, and remove elements from the array.
# Array Operations:

# Write a Python function that takes an array of integers as input and returns the sum of all the elements in the array. Optimize the function for large arrays.
# Linked List Creation:

# Implement a basic singly linked list class in Python. Include methods for appending nodes, inserting nodes at specific positions, and printing the linked list.
# Linked List Operations:

# Write a Python function to reverse a singly linked list in-place. Provide both iterative and recursive solutions.
# Array Searching:

# Given an array of integers and a target value, write a Python function to find the index of the target value in the array using binary search. Ensure that the array is sorted before applying binary search.
# Linked List Cycle Detection:

# # Create a Python function to detect if a given linked list contains a cycle. Implement Floyd's Tortoise and Hare algorithm to solve this problem efficiently.

# Solution

# Array Initialization and Operations:
# Create an empty list (array)
my_array = []

# Append elements to the array
my_array.append(1)
my_array.append(2)
my_array.append(3)

# Insert an element at a specific position (e.g., index 1)
my_array.insert(1, 4)

# Remove an element from the array
my_array.remove(2)

# Print the modified array
print(my_array)

# Write a function to sum the elements of an array
def sum_array(arr):
    return sum(arr)

# Test the sum_array function
result = sum_array(my_array)
print("Sum of array elements:", result)


# Linked List Creation and Operations:
# Define a basic singly linked list node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a singly linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next:
                    current = current.next
                else:
                    break
            new_node.next = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list and perform operations
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.insert(4, 1)
my_linked_list.print_list()

# Linked List Reverse (Iterative and Recursive):
# Iterative solution to reverse a linked list
def reverse_linked_list_iterative(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Recursive solution to reverse a linked list
def reverse_linked_list_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Example usage
reversed_head = reverse_linked_list_iterative(my_linked_list.head)
my_linked_list.head = reversed_head
my_linked_list.print_list()

# Array Binary Search:
# Binary search in a sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Element not found

# Test binary_search
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 6
index = binary_search(sorted_array, target_value)
if index != -1:
    print(f"{target_value} found at index {index}")
else:
    print(f"{target_value} not found in the array")


# Linked List Cycle Detection (Floyd's Algorithm):
# Detect a cycle in a linked list using Floyd's Tortoise and Hare algorithm
def has_cycle(head):
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage
has_cycle_result = has_cycle(my_linked_list.head)
print("Has cycle:", has_cycle_result)
