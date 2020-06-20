from math import log10

def counting_sort(arr, place, max_place):
    
    sorted_arr = [0]*len(arr)
    count_bucket = [0]* 10
    
    for i  in range(len(arr)-1, -1,-1):
      num = arr[i]
      num_zfill = int(str(num).ljust(max_place,'0'))
      place_num = num_zfill//place % 10
      count_bucket[place_num] += 1
    
    for i in range(1, 10):
      count_bucket[i] += count_bucket[i-1]
    
    for i in range(len(arr)-1, -1, -1):
      num = arr[i]
      num_zfill = int(str(num).ljust(max_place, '0'))
      place_num = num_zfill//place % 10
      sorted_index = count_bucket[place_num] -1
      count_bucket[place_num] -= 1
      sorted_arr[sorted_index] = num
    return sorted_arr
        

def largestNumber(A):
    # using radix sort.
    place = 1
    max_num = max(A)
    max_place = int(log10(max_num))+1
    arr = A
    
    while(max_num/place > 0):
        arr = counting_sort(A, place, max_place)
        place *= 10
    print(arr)
    largest_num = ""
    for i in range(len(A)-1,-1,-1):
        largest_num +=str(arr[i])
    
    return largest_num

f = [8, 89]
A = [3, 30, 34, 5, 9]
print(largestNumber(f))


def largestNumberOneLine(self, A):
  return str(int(’’.join(sorted(map(str, A), key=lambda s: s*9)[::-1])))

def check_prime(a):
          for i in range(2, int(a**0.5)+1):
              if a % i == 0:
                  return False
          return True


def solve(self, A, B, C):
    
    if len(str(C)) > B:
        return len(A)**B
    elif len(str(C)) < B:
        return 0
    else:
        start_char = int(str(C)[0])
        count = 0
        for num in A:
            if num < start_char and num != 0:
                count += 1
        return count*((len(A))**(B-1))
A = [0]
B = 1
C = 5
