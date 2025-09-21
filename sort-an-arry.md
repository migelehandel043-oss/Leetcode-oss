def heapify(nums, n, i):
    largest = i       # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2 # Right child index

    # If left child is larger than root
    if left < n and nums[left] > nums[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and nums[right] > nums[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]  # Swap
        heapify(nums, n, largest)  # Recursively heapify affected sub-tree

def heapSort(nums):
    n = len(nums)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]  # Swap
        heapify(nums, i, 0)

    return nums

# Example usage
nums = [5, 2, 3, 1]
print(heapSort(nums))  # Output: [1, 2, 3, 5]
