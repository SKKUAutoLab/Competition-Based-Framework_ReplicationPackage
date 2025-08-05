# Analysis Notes

This document outlines the procedures and formulas used in the analysis of the anonymized survey data collected from autonomous driving competitions and capstone courses.

Survey responses were collected anonymously during competitions and the 2024-2 capstone design course.
In the 2025-1 capstone design course, survey responses were collected with names.
Therefore, data from competitions and the 2024-2 capstone design course were analyzed using independent sample analysis, while data from the 2025-1 capstone design course were analyzed using paired sample analysis.

---

## 1. Descriptive Statistics

For each survey item, the following were calculated using Excel built-in functions:

- **Mean**: `=AVERAGE(range)`
- **Standard Deviation**: `=STDEV.S(range)`
- **Sample Size (N)**: `=COUNT(range)`

---
  
## 2. t-test

### 2.1 Paired t-test

- **Excel formula**:  
  `=T.TEST(pre_range, post_range, 2, 1)`

### 2.2 Independent t-test

- **Excel formula**:  
  `=T.TEST(pre_range, post_range, 2, 2)`  

---

## 3. Effect Size (Cohen's d)

### 3.1 Paired

- **Formula**
`Cohen's d = Mean_Diff / SD_Diff`

- **Where**:  
`Mean_Diff = AVERAGE(post_range - pre_range)`
`SD_Diff = STDEV.S(post_range - pre_range)`

### 3.2 Independent

- **Formula**:
`Cohen's d = (Mean_post - Mean_pre) / SD_pooled`

- **Where**:  
`SD_pooled = SQRT( ((SD_pre^2 * (n_pre - 1)) + (SD_post^2 * (n_post - 1))) / (n_pre + n_post - 2) )`

---

## 4. 95% Confidence Interval

### 4.1 Paired

- **Formula**:
`CI = Mean_Diff ± t * SE_Diff`

- **Where**:
`SE_Diff = SD_Diff / SQRT(n)`
`t = T.INV.2T(0.05, n - 1)`

### 4.2 Independent

- **Formula**:  
  `CI = (Mean_post - Mean_pre) ± t * SE_diff`

- **Where**:  
  `SE_diff = SQRT( (SD_pre^2 / n_pre) + (SD_post^2 / n_post) )`  
  `t = T.INV.2T(0.05, df)`  

- `df` is calculated using the **Welch-Satterthwaite approximation**:
  `df = ((SD_pre^2/n_pre + SD_post^2/n_post)^2) / ((SD_pre^2/n_pre)^2)/(n_pre-1) + ((SD_post^2/n_post)^2)/(n_post-1) )`


## 5. Correlation

- **Excel Formula**:
`=CORREL(array1 , array2)`

- **p-value for Correlation Formula**:
`=T.DIST.2T(ABS (t) , n - 2)`

- **Where**:
  `t = (r * SQRT(n - 2)) / SQRT(1 - r^2)`
