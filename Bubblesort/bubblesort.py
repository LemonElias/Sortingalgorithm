class Bubblesort:
    # Creates a class named Bubblesort
    def __init__(self, array):
        self.array = array
        self.length = len(array)

    def sort(self): # Function to sort the array
        for i in range(self.length):  # Traverse through all elements in the array
            swapped = False # Initialize swapped to False (Flag to check if the elements are swapped or not)
            for j in range(0, self.length - i - 1): # Traverse through the array from 0 to length - i - 1 to prevent the traversal of the sorted elements
                if self.array[j] > self.array[j + 1]: # If the current element is greater than the next element the algorithm swaps the elements
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True # Set swapped to True
            if not swapped:
                break
        return self.array

# Instantiate the Bubblesort class with an unsorted list
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = Bubblesort(unsorted_list)

# Sort the list using the Bubblesort class
sorted_list = bubble_sort.sort()

# Manually sort the list for comparison
manually_sorted_list = sorted(unsorted_list)

# Print both lists
print("Bubblesort sorted list: ", sorted_list)
print("Manually sorted list: ", manually_sorted_list)

# Check if the sorted list from the Bubblesort class is equal to the manually sorted list
if sorted_list == manually_sorted_list:
    print("Test passed: Bubblesort correctly sorted the list.")
else:
    print("Test failed: Bubblesort did not correctly sort the list.")