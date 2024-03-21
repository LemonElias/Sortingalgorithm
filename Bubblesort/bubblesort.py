class Bubblesort:
    # Creating class named Bubblesort
    def __init__(self, array):
        self.array = array
        self.lenght = len(array)

    def sort(self): # Function to sort the array
        for i in range(self.lenght):  # Traverse through all elements in the array
            swapped = False # Initialize swapped to False (Flag to check if the elements are swapped or not)
            for j in range(0, self.length, - i - 1): # Traverse through the array from 0 to length - i - 1 to prevent the traversal of the sorted elements
                if self.array[j] > self.array[j + 1]: # If the current element is greater than the next element the algorithm swaps the elements
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True # Set swapped to True
            if not swapped:
                break
        return self.array

    def printArray(self):
        for i in range(self.lenght):
            print(self.array[i], end=" ")
        print()#