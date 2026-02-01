1️⃣ Character Count in a String
❓ Problem
Count the occurrence of each character in a string.

🏢 Asked In
Amazon, TCS, Infosys, Accenture

✅ Solution
s = "programming"
count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

print(count)
⏱ Complexity
Time: O(n)
Space: O(n)
2️⃣ Check if Two Strings Are Anagrams (Optimized)
❓ Problem
Check whether two strings are anagrams.

🏢 Asked In
Google, Microsoft, Flipkart, Wipro

✅ Solution
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True

print(is_anagram("listen", "silent"))
⏱ Complexity
Time: O(n)
Space: O(n)
3️⃣ Check Anagram Using Sorting
🏢 Asked In
Capgemini, Cognizant

✅ Solution
s1 = "race"
s2 = "care"

print(sorted(s1) == sorted(s2))
⏱ Complexity
Time: O(n log n)
Space: O(n)
4️⃣ First Non-Repeating Character
❓ Problem
Find the first character that appears only once.

🏢 Asked In
Amazon, Paytm

✅ Solution
s = "aabbcde"
count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in s:
    if count[ch] == 1:
        print(ch)
        break
5️⃣ Check if String Has All Unique Characters
🏢 Asked In
Adobe, Zoho

✅ Solution
s = "python"
print(len(set(s)) == len(s))
6️⃣ Group Anagrams Together
❓ Problem
Group strings that are anagrams.

🏢 Asked In
Amazon, Google, Microsoft

✅ Solution
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

print(list(groups.values()))
7️⃣ Anagram Check (Case Insensitive)
🏢 Asked In
Accenture, Infosys

✅ Solution
def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True

print(is_anagram("Listen", "Silent"))
8️⃣ Anagram Ignoring Spaces
🏢 Asked In
TCS, Wipro

✅ Solution
def is_anagram(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    count = {}

    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True

print(is_anagram("conversation", "voices rant on"))
9️⃣ Most Frequent Character in a String
🏢 Asked In
Amazon, Flipkart

✅ Solution
s = "programming"
count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

max_char = max(count, key=count.get)
print(max_char, count[max_char])
🔟 Count Vowels Using Character Count Logic
🏢 Asked In
Cognizant, Capgemini

✅ Solution
s = "interview"
vowels = "aeiou"
count = 0

for ch in s.lower():
    if ch in vowels:
        count += 1

print(count)
1️⃣1️⃣ Check if Any Anagram of Pattern Exists
🏢 Asked In
Google, Adobe

✅ Solution
from collections import Counter

s = "cbaebabacd"
p = "abc"

p_count = Counter(p)
window = Counter(s[:len(p)])

if window == p_count:
    print(True)

for i in range(len(p), len(s)):
    window[s[i]] += 1
    window[s[i - len(p)]] -= 1

    if window[s[i - len(p)]] == 0:
        del window[s[i - len(p)]]

    if window == p_count:
        print(True)
        break
