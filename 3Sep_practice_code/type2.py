# Array Manipulation:

# Given an array of integers, write a Python function to find the maximum subarray sum (the sum of a contiguous subarray) using the Kadane's algorithm. Provide the start and end indices of the subarray as well.
# Array Sorting:

# Implement a Python function to sort an array of integers using the quicksort algorithm. Include both the recursive and iterative versions of the algorithm.
# Linked List Intersection:

# Write a Python function that finds the intersection point of two singly linked lists. If the lists do not intersect, return None. Optimize for time and space complexity.
# Circular Linked List:

# Create a Python class for a circular linked list and include methods for insertion, deletion, and traversal. Demonstrate how to add elements to and remove elements from a circular linked list.
# Array Rotation:

# Given an array of integers, write a Python function to rotate the array to the right by a given number of positions. Optimize the algorithm to have a time complexity of O(n).
# Linked List Palindrome:

# Implement a Python function to determine if a singly linked list is a palindrome. You can't use additional data structures; solve it in O(n) time and O(1) space


# Solutions:
# Maximum Subarray Sum (Kadane's Algorithm):
def max_subarray_sum(arr):
    if not arr:
        return 0
    
    max_sum = current_sum = arr[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        if arr[i] > (current_sum + arr[i]):
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

# Example usage
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start_index, end_index = max_subarray_sum(array)
print("Maximum Subarray Sum:", max_sum)
print("Start Index:", start_index)
print("End Index:", end_index)

# Quicksort (Recursive and Iterative):
# Recursive Quicksort
def quicksort_recursive(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_recursive(left) + middle + quicksort_recursive(right)

# Iterative Quicksort
def quicksort_iterative(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        if i - 1 > left:
            stack.append((left, i - 1))
        if i + 1 < right:
            stack.append((i + 1, right))
    
    return arr

# Example usage
array = [3, 6, 8, 10, 1, 2, 1]
print("Recursive Quicksort:", quicksort_recursive(array))
print("Iterative Quicksort:", quicksort_iterative(array))


# Linked List Intersection:
# Node definition for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_intersection(headA, headB):
    if not headA or not headB:
        return None
    
    ptrA, ptrB = headA, headB
    while ptrA != ptrB:
        ptrA = headB if not ptrA else ptrA.next
        ptrB = headA if not ptrB else ptrB.next
    
    return ptrA  # Intersection node or None if no intersection

# Example usage
# Create two linked lists with an intersection point
common_node = ListNode(4)
list1 = ListNode(1, ListNode(2, common_node))
list2 = ListNode(3, common_node)
intersection = get_intersection(list1, list2)
if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")

# Create two linked lists with no intersection
list3 = ListNode(5, ListNode(6, ListNode(7)))
list4 = ListNode(8, ListNode(9, ListNode(10)))
intersection = get_intersection(list3, list4)
if intersection:
    print("Intersection at node with value:", intersection.val)
else:
    print("No intersection")


# Circular Linked List:
# Node definition for circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            if current == self.head:
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                if current.data == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next

    def display(self):
        current = self.head
        if not current:
            return
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

# Example usage
clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.display()
clist.delete(2)
clist.display()

# Array Rotation:
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    arr[:] = arr[-k:] + arr[:-k]  # Rotate the array in-place

# Example usage
array = [1, 2, 3, 4, 5]
rotate_array(array, 2)
print("Rotated Array:", array)


# Linked List Palindrome:
# Node definition for singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    # Helper function to reverse a linked list
    def reverse_linked_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next  # For odd-length lists

    slow = reverse_linked_list(slow)

    while slow:
        if head.val != slow.val:
            return False
        head = head.next
        slow = slow.next

    return True

# Example usage
list1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print("Is list1 a palindrome?", is_palindrome(list1))  # Should return True
print("Is list2 a palindrome?", is_palindrome(list2))  # Should return False

