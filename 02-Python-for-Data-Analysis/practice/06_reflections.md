# Reflections:

## Common Data Quality Issues:
Datasets often contain problems that must be addressed before analysis can begin.

Typical issues include:
- missing values.
- incorrect numeric values.
- invalid date formats.
- inconsistent text entries.
- incomplete records.

---

## Principles for Cleaning Data:
Cleaning decisions should be guided by evidence within the dataset rather than arbitrary changes.

Some useful principles include:
- **Preserve valid data whenever possible:** Removing rows should be a last resort because it discards real information.
- **Use contextual evidence to correct errors:** If values in similar rows follow a consistent pattern, those patterns can guide corrections.
- **Mark values as missing when the correct value cannot be confidently inferred.**
- **Document every cleaning decision:** Documenting makes the rerason behind decisions and changes transparent.

These principles help maintain the integrity of the daataset while improving its usability.

---

## Working with Missing Data:
Missing values can occur for many reasons including data entry mistakes or incomplete records.

Possible approaches include:
- replacing missing values with reasonable defaults.
- inferring values using patterns within the dataset.
- leaving the values missing but accounting for them during analysis.
- removing rows only when the missing information makes the record unusable.

Choosing the correct approach depends on the context of the data and the goals of the analysis.

---

## Key Pandas Operations Practiced:
This exercise reinforced several important pandas operations used frequently in data preparation:
- selecting rows using 'loc()'.
- identifying missing values with 'isnull()'.
- replacing missing values.
- updating column values conditionally.
- correcting numeric errors using 'abs()'.
- filtering rows with multiple conditions.

I believe that these operations should form the foundation of many real-world data cleaning workflows.

---

## Key Takeaway:
Effective data analysis begins with understanding the dataset and addressing data quality issues in a systematic way. 

Inspection, documentation, and carefully justified cleaning decisions are essential steps before performing meaningful analysis.
