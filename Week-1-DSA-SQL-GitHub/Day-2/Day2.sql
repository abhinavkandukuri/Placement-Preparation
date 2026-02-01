SQL Interview Questions
(ORDER BY, LIMIT, AND, OR, LIKE)
🔸 Basic Level (Must-Know)
1️⃣ Use of ORDER BY
Used to sort the result set.

SELECT * FROM students
ORDER BY marks;
2️⃣ Default sorting order
✅ Ascending (ASC)

ORDER BY marks;
⭐ ORDER BY vs WHERE
WHERE	ORDER BY
Filters rows	Sorts rows
Applied first	Applied later
⭐ LIMIT with ORDER BY
SELECT * FROM students
ORDER BY marks DESC
LIMIT 5;
3️⃣ ASC vs DESC
ASC	DESC
Small → Large	Large → Small
4️⃣ ORDER BY multiple columns
ORDER BY marks DESC, age ASC;
5️⃣ Purpose of LIMIT
Restricts number of rows returned.

6️⃣ LIMIT vs WHERE
LIMIT	WHERE
Limits output	Filters data
7️⃣ LIMIT without ORDER BY
✅ Allowed, but order not guaranteed.

8️⃣ Execution order
FROM → WHERE → SELECT → ORDER BY → LIMIT
9️⃣ AND operator
All conditions must be true.

🔟 OR operator
Any one condition must be true.

🔸 Intermediate Level ⭐
Operator precedence
()
AND
OR
LIKE operator
Used for pattern matching.

Pattern	Meaning
%	Any number of characters
_	Exactly one character
Examples
LIKE 'A%'      -- starts with A
LIKE '%a%'     -- contains a
LIKE '_____'   -- exactly 5 characters
Top queries
-- Top 5 salaries
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;

-- Second highest salary
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
🔸 Scenario-Based Queries 💡
-- Top 3 students
ORDER BY marks DESC LIMIT 3;

-- Name ends with n
WHERE name LIKE '%n';

-- Hyderabad or Bangalore
WHERE city = 'Hyderabad' OR city = 'Bangalore';
WHERE vs HAVING
WHERE	HAVING
Filters rows	Filters groups
Before GROUP BY	After GROUP BY
AND / OR best practice
Always use parentheses to avoid logical errors.

WHERE age > 18 AND (city = 'Hyd' OR city = 'Blr');
