# 15. Multiple Exceptions:
# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not
def list_and_index(list_1,index):
    try:
        element = list_1[index]
        print(f"Element of index {index}: {element}")
    except IndexError:
        print(f"IndexError: Index {index} is out of range.")
    finally:
        print("Task completed")
list_and_index([1,2,3,4,5,6],2)
