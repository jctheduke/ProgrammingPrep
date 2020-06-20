import heapq

# quick sort
def quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = quick_partition(arr,low,high)
        quick_sort_helper(arr,low,pivot_index-1)
        quick_sort_helper(arr,pivot_index+1, high)
def quick_partition(arr, low, high):

    i = low -1

    for j in range(low, high):
        # arr[high] is the pivot
        if arr[j] < arr[high]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1 # pivot index
def quick_sort(arr):
    low=0
    high = len(arr)-1
    quick_sort_helper(arr, low, high)
    return arr

# bubble sort
def bubble_sort(arr):
    for j in range(len(arr)-1,0,-1):
        for i in range(0,j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
# Merge sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        a = merge_sort(arr[0:len(arr)//2])
        b = merge_sort(arr[len(arr)//2:])
    
    return merge_sort_helper(a,b)

def merge_sort_helper(a,b):
    # merges two arrays in sorted order
    i = 0
    j = 0
    merged_array = []
    while( i < len(a) and j < len(b)):
        if a[i] <= b[j]:
            merged_array.append(a[i])
            i += 1
        else:
            merged_array.append(b[j])
            j += 1
    merged_array += a[i:] + b[j:]
    return merged_array

# Insertion Sort
def insertion_sort(arr):
    for j in range(len(arr)):
        for i in range(j):
            if arr[j] < arr[i]:
                x =  arr.pop(j)
                arr.insert(i,x)
    return arr

# Selection Sort
def selection_sort(arr):
    for j in range(len(arr)-1):
        current_min_val = arr[j]
        current_min_index= j
        for i in range(j,len(arr)):
            if arr[i] < current_min_val:
                current_min_val = arr[i]
                current_min_index = i
        arr[j], arr[current_min_index] = arr[current_min_index], arr[j]
    return arr

# Heap Sort
def heap_sort(arr):
    sorted_heap = arr.copy()
    heapq.heapify(sorted_heap)
    m = []
    while(sorted_heap):
        m.append(heapq.heappop(sorted_heap))
    return m

# Bucket Sort
# Bucket sort is used to sort elements which have distribution over a range.

def bucket_sort(arr):

    num_slots = 10
    
    buckets = []
    for i in range(num_slots):
        buckets.append([])

    # Assuming numbers are in range 0 to 1
    for num in arr:
        bucket_index = int(10*num)
        buckets[bucket_index].append(num)

    # sorting individual buckets
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    sorted_arr = []
    for bucket in buckets:
        for num in bucket:
            sorted_arr.append(num)
    
    return sorted_arr


# Counting sort
# assuming only non-negative are provided
# use this when there are lot of duplicated and densly populated numbers
def counting_sort(arr):
    max_arr = max(arr)
    count_arr = [0]*(max_arr+1)
    sorted_array = [0]*len(arr)
    for num in arr:
        count_arr[num] += 1

    cumulative_counts = []
    cumulative_count = 0

    for num_count in count_arr:
        cumulative_count += num_count
        cumulative_counts.append(cumulative_count)
    
    for num in arr:
        sorted_array[cumulative_counts[num]-1] = num
        cumulative_counts[num] -= 1

    return sorted_array

# Radix Sort
def counting_sort_helper(arr, place):
    count_bucket = [0]*10
    sorted_arr = [0]*len(arr)

    for num in arr:
        place_num = num % (10*place)//place
        count_bucket[place_num] += 1
    
    cum_count = 0
    for i in range(10):
        cum_count += count_bucket[i]
        count_bucket[i] = cum_count
    
    for i in range(len(arr)-1,-1, -1):
        place_num = arr[i] % (10*place)//place
        sorted_index = count_bucket[place_num]-1
        count_bucket[place_num] = sorted_index
        sorted_arr[sorted_index] = arr[i]
    
    return sorted_arr

def radix_sort(arr):
    max_arr = max(arr)
    place = 1
    while(max_arr / 10):
        arr = counting_sort_helper(arr, place)
        max_arr /= 10
        place *= 10
    return arr

# Shell sort
def shell_sort(arr):

    # Using the normal sequences
    arr_size = len(arr)
    gap = len(arr)//2

    while(gap > 0):
        for i in range(gap, arr_size):
            temp = arr[i]
            j=i
            while (j >= gap) and (arr[j-gap] > temp):
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = temp
        
        gap //= 2
    return arr