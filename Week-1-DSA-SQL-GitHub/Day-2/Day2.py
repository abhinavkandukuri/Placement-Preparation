🔹 String Interview Questions (Reverse & Palindrome) — Python
🔸 Basic Level
1️⃣ What is string reversal?
String reversal means rearranging characters so the last character becomes first.

s = "hello"
# reversed -> "olleh"
2️⃣ What is a palindrome string?
A palindrome string reads the same forward and backward.

"madam" == "madam"[::-1]   # True
3️⃣ Examples of palindrome strings
["madam", "level", "racecar", "noon", "civic"]
4️⃣ Is a single character a palindrome?
✅ Yes, because forward and backward are the same.

s = "a"
print(s == s[::-1])   # True
5️⃣ Difference between string and character array
String	Character Array
Immutable	Mutable
Cannot change characters	Characters can be changed
"hello"	['h','e','l','l','o']
# string (immutable)
s = "hello"
# s[0] = 'H' ❌ error

# character array (list)
arr = list("hello")
arr[0] = 'H'   # ✅
🔸 Coding Logic Questions ⭐
6️⃣ Reverse a string without built-in functions
s = "hello"
rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print(rev)
7️⃣ Reverse a string using loop
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(reverse_string("hello"))
8️⃣ Reverse a string using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
9️⃣ How do you check if a string is palindrome?
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
🔟 Check palindrome without reversing (Two-pointer method)
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("madam"))
1️⃣1️⃣ Case-insensitive palindrome check
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Madam"))  # True
1️⃣2️⃣ Ignore spaces & special characters
import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
1️⃣3️⃣ Time complexity of string reversal
Time Complexity: O(n)
Space Complexity: O(n)
1️⃣4️⃣ Loop vs Recursion
Loop	Recursion
Faster	Slower
Less memory	More memory (stack)
Preferred	Rarely used
1️⃣5️⃣ Why strings are immutable? (Java concept)
Improves security
Enables memory optimization (string pool)
Makes strings thread-safe
🔸 Tricky / Conceptual Questions ⚠️
1️⃣6️⃣ Is "Madam" a palindrome?
❌ Case-sensitive → No ✅ Case-insensitive → Yes

"Madam".lower() == "madam"[::-1]
1️⃣7️⃣ Is "A man a plan a canal Panama" a palindrome?
✅ Yes, if spaces and symbols are ignored.

1️⃣8️⃣ Can numbers be palindromes?
✅ Yes

n = 121
print(str(n) == str(n)[::-1])  # True
1️⃣9️⃣ What happens if input string is empty?
✅ Considered a palindrome

s = ""
print(s == s[::-1])  # True
2️⃣0️⃣ Optimized palindrome checking
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
