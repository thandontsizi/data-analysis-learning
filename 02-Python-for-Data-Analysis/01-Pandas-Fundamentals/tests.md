# Python for Data Analysis: Thinking Checks.
This file contains reasoning checks to reinforce analytical thinking during data cleaning and exploration.

---

# Part 1: Concept Checks.
1. Why should a dataset be inspected before cleaning it?
2. What is the difference between dropping missing values and filling missing values?
3. Why might duplicate rows exist legitimately in a dataset?
4. Why should data cleaning steps be reproducible instead of done manually in Excel?
5. What risks exist when converting a column from text to numeric?
6. Why is it important tot confirm data types before performing analysis?
7. What problems can inconsistent text formatting cause in categorical data?
8. Why should suspicious values (such as negative prices) be investigated instead of immediately deleted?

---

# Part 2: Scenario-Based Questions.
1. You load a dataset and notice that the 'order_date' column contains multiple formats:
- '2026-02-01'
- '02/01/2026'
- '2026/02/01'

What problem does this create for analysis and how would you address it?

---

2. You discover duplicate rows in a sales dataset. Before removing them, what questions should you ask to determine whether they represent real transactions or data errors?

---

3. A column named 'price' contains the values:
- 12000
- 3500
- -600
- 250

What might a negative price indicate and how should it be investigated before deciding what to do with it?

---

4. A dataset contains customer names such as:
- Brian K.
- brian k.
- BRIAN K.

What issue does this create for analysis and how would you standardise these values?

---

5. You notice that the 'quantity' column contains missing values for several orders. 
What possible explanations could there be for these missing values, and what factors would influence how you handle them?

---

6. After cleaning a dataset, what validation checks should you perform before beginning analysis?

