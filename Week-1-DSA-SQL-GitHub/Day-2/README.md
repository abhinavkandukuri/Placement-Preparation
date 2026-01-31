

## 🔹 String Interview Questions (Reverse & Palindrome) — Python

### 🔸 Basic Level

### 1️⃣ What is string reversal?

String reversal means rearranging characters so the **last character becomes first**.

```python
s = "hello"
# reversed -> "olleh"
```

---

### 2️⃣ What is a palindrome string?

A palindrome string reads the **same forward and backward**.

```python
"madam" == "madam"[::-1]   # True
```

---

### 3️⃣ Examples of palindrome strings

```python
["madam", "level", "racecar", "noon", "civic"]
```

---

### 4️⃣ Is a single character a palindrome?

✅ Yes, because forward and backward are the same.

```python
s = "a"
print(s == s[::-1])   # True
```

---

### 5️⃣ Difference between string and character array

| String                   | Character Array           |
| ------------------------ | ------------------------- |
| Immutable                | Mutable                   |
| Cannot change characters | Characters can be changed |
| `"hello"`                | `['h','e','l','l','o']`   |

```python
# string (immutable)
s = "hello"
# s[0] = 'H' ❌ error

# character array (list)
arr = list("hello")
arr[0] = 'H'   # ✅
```

---

## 🔸 Coding Logic Questions ⭐

### 6️⃣ Reverse a string without built-in functions

```python
s = "hello"
rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print(rev)
```

---

### 7️⃣ Reverse a string using loop

```python
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

print(reverse_string("hello"))
```

---

### 8️⃣ Reverse a string using recursion

```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))
```

---

### 9️⃣ How do you check if a string is palindrome?

```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # True
```

---

### 🔟 Check palindrome without reversing (Two-pointer method)

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("madam"))
```

---

### 1️⃣1️⃣ Case-insensitive palindrome check

```python
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("Madam"))  # True
```

---

### 1️⃣2️⃣ Ignore spaces & special characters

```python
import re

def is_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man a plan a canal Panama"))  # True
```

---

### 1️⃣3️⃣ Time complexity of string reversal

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

### 1️⃣4️⃣ Loop vs Recursion

| Loop        | Recursion           |
| ----------- | ------------------- |
| Faster      | Slower              |
| Less memory | More memory (stack) |
| Preferred   | Rarely used         |

---

### 1️⃣5️⃣ Why strings are immutable? (Java concept)

* Improves security
* Enables memory optimization (string pool)
* Makes strings thread-safe

---

## 🔸 Tricky / Conceptual Questions ⚠️

### 1️⃣6️⃣ Is `"Madam"` a palindrome?

❌ Case-sensitive → No
✅ Case-insensitive → Yes

```python
"Madam".lower() == "madam"[::-1]
```

---

### 1️⃣7️⃣ Is `"A man a plan a canal Panama"` a palindrome?

✅ Yes, if spaces and symbols are ignored.

---

### 1️⃣8️⃣ Can numbers be palindromes?

✅ Yes

```python
n = 121
print(str(n) == str(n)[::-1])  # True
```

---

### 1️⃣9️⃣ What happens if input string is empty?

✅ Considered a palindrome

```python
s = ""
print(s == s[::-1])  # True
```

---

### 2️⃣0️⃣ Optimized palindrome checking

```python
def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
```

---

# 🔹 SQL Interview Questions

## (ORDER BY, LIMIT, AND, OR, LIKE)

### 🔸 Basic Level (Must-Know)

### 1️⃣ Use of ORDER BY

Used to **sort the result set**.

```sql
SELECT * FROM students
ORDER BY marks;
```

---

### 2️⃣ Default sorting order

✅ Ascending (`ASC`)

```sql
ORDER BY marks;
```

---

### ⭐ ORDER BY vs WHERE

| WHERE         | ORDER BY      |
| ------------- | ------------- |
| Filters rows  | Sorts rows    |
| Applied first | Applied later |

---

### ⭐ LIMIT with ORDER BY

```sql
SELECT * FROM students
ORDER BY marks DESC
LIMIT 5;
```

---

### 3️⃣ ASC vs DESC

| ASC           | DESC          |
| ------------- | ------------- |
| Small → Large | Large → Small |

---

### 4️⃣ ORDER BY multiple columns

```sql
ORDER BY marks DESC, age ASC;
```

---

### 5️⃣ Purpose of LIMIT

Restricts number of rows returned.

---

### 6️⃣ LIMIT vs WHERE

| LIMIT         | WHERE        |
| ------------- | ------------ |
| Limits output | Filters data |

---

### 7️⃣ LIMIT without ORDER BY

✅ Allowed, but order not guaranteed.

---

### 8️⃣ Execution order

```text
FROM → WHERE → SELECT → ORDER BY → LIMIT
```

---

### 9️⃣ AND operator

All conditions must be true.

---

### 🔟 OR operator

Any one condition must be true.

---

## 🔸 Intermediate Level ⭐

### Operator precedence

1. `()`
2. `AND`
3. `OR`

---

### LIKE operator

Used for pattern matching.

| Pattern | Meaning                  |
| ------- | ------------------------ |
| `%`     | Any number of characters |
| `_`     | Exactly one character    |

---

### Examples

```sql
LIKE 'A%'      -- starts with A
LIKE '%a%'     -- contains a
LIKE '_____'   -- exactly 5 characters
```

---

### Top queries

```sql
-- Top 5 salaries
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;

-- Second highest salary
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

---

## 🔸 Scenario-Based Queries 💡

```sql
-- Top 3 students
ORDER BY marks DESC LIMIT 3;

-- Name ends with n
WHERE name LIKE '%n';

-- Hyderabad or Bangalore
WHERE city = 'Hyderabad' OR city = 'Bangalore';
```

---

### WHERE vs HAVING

| WHERE           | HAVING         |
| --------------- | -------------- |
| Filters rows    | Filters groups |
| Before GROUP BY | After GROUP BY |

---

### AND / OR best practice

Always use **parentheses** to avoid logical errors.

```sql
WHERE age > 18 AND (city = 'Hyd' OR city = 'Blr');
```

---

## ✅ Final Note

This README is designed for:

* 📌 Interview preparation
* 📌 GitHub portfolio
* 📌 Quick revision before exams

---

