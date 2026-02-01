1️⃣ Find Maximum & Minimum
🔹 Brute Force
arr = [3, 5, 1, 9, 2]

max_val = arr[0]
min_val = arr[0]

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]

print(max_val, min_val)
Time: O(n) Space: O(1)

⚡ Optimized (Built-in)
arr = [3, 5, 1, 9, 2]
print(max(arr), min(arr))
Time: O(n) Space: O(1)

Interview line:

“I traverse the array once to track max and min.”

2️⃣ Second Largest Element
🔹 Brute Force (Sorting)
arr = [10, 20, 4, 45, 99]

arr = list(set(arr))
arr.sort()

print(arr[-2])
Time: O(n log n) Space: O(n)

⚡ Optimized (Single Pass)
arr = [10, 20, 4, 45, 99]

largest = second = -1

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)
Time: O(n) Space: O(1)

Edge case: all elements same → no second largest.

3️⃣ Frequency of Elements
🔹 Brute Force
arr = [1, 2, 2, 3, 1]

freq = {}

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1
    freq[arr[i]] = count

print(freq)
Time: O(n²) Space: O(n)

⚡ Optimized (HashMap)
arr = [1, 2, 2, 3, 1]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)
Time: O(n) Space: O(n)

Interview line:

“I use a hash map to count frequencies in one traversal.”

4️⃣ Check if Array is Sorted
🔹 Brute Force
arr = [1, 2, 3, 4]

sorted_arr = sorted(arr)

if arr == sorted_arr:
    print("Sorted")
else:
    print("Not Sorted")
Time: O(n log n) Space: O(n)

⚡ Optimized
arr = [1, 2, 3, 4]

is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print("Sorted" if is_sorted else "Not Sorted")
Time: O(n) Space: O(1)

5️⃣ Reverse an Array
🔹 Brute Force
arr = [1, 2, 3, 4]

rev = arr[::-1]
print(rev)
Time: O(n) Space: O(n)

⚡ Optimized (Two Pointers)
arr = [1, 2, 3, 4]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
Time: O(n) Space: O(1)

6️⃣ Find Duplicate Elements
🔹 Brute Force
arr = [1, 2, 3, 2, 4, 1]

duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print(duplicates)
Time: O(n²) Space: O(n)

⚡ Optimized (Set)
arr = [1, 2, 3, 2, 4, 1]

seen = set()
duplicates = []

for num in arr:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

print(duplicates)
Time: O(n) Space: O(n)

7️⃣ Count Even and Odd Numbers
🔹 Brute Force
arr = [1, 2, 3, 4, 5]

even = odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(even, odd)
Time: O(n) Space: O(1)

⚡ Optimized (Same – already optimal)
✔ This is already optimal.

8️⃣ Sum & Average
🔹 Brute Force
arr = [1, 2, 3, 4]

sum_val = 0
for num in arr:
    sum_val += num

avg = sum_val / len(arr)
print(sum_val, avg)
Time: O(n) Space: O(1)

⚡ Optimized
arr = [1, 2, 3, 4]

print(sum(arr), sum(arr)/len(arr))
Time: O(n) Space: O(1)

