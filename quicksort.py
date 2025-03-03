def partition(arr, low, high):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1  # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        # pi is partitioning index
        pi = partition(arr, low, high)
        
        # Separately sort elements before and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Example usage
if __name__ == "__main__":
    # Test array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    
    # Call quicksort
    quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr) 