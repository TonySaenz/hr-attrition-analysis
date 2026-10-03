# HR Workforce Attrition Analysis

An interactive Tableau dashboard and Python analysis of employee attrition, built to identify which workforce factors are most associated with employees leaving and where HR could focus retention efforts.

**Live dashboard:** [HR Workforce Attrition Analysis on Tableau Public](https://public.tableau.com/app/profile/tony.saenz5756/viz/HRWorkforceAttritionAnalysis_17907012299330/HRWorkforceAttritionAnalysis)

## Business Question

Which employee groups have the highest attrition, and what factors (overtime, tenure, pay, stock options, satisfaction) are most associated with turnover?

## Data

- **Source:** IBM HR Analytics Employee Attrition & Performance dataset (Kaggle)
- **Size:** 1,470 employees, 35 columns
- **Note:** This is a fictional dataset created by IBM data scientists for analysis practice. It is a single snapshot with no time dimension.

## Tools

- **Python (pandas):** data validation, cleaning, feature creation, and attrition analysis
- **Tableau Public:** interactive dashboard with KPIs, charts, and filters

## Process

1. **Exploration (`01_explore.py`):** Checked shape, data types, missing values, and duplicates. Found no missing values or duplicates, three constant columns, and an overall attrition rate of 16.1%.
2. **Cleaning (`02_clean.py`):** Dropped constant and unused columns, created a 1/0 attrition flag, converted coded ratings (1 to 4) into readable labels, and created age, tenure, and income bands. Output: `hr_attrition_clean.csv`.
3. **Analysis (`03_analysis.py`):** Calculated attrition rate and employee count for each group across 13 variables, plus a job satisfaction by environment satisfaction cross-tab.
4. **Dashboard:** Built 9 worksheets in Tableau and combined them into one dashboard with filters for Department, Age Band, Gender, and Overtime. All dashboard values were checked against the Python output.

## Key Findings

| Factor | Highest Attrition Group | Comparison |
|---|---|---|
| Overtime | Works overtime: 30.5% | No overtime: 10.4% |
| Job role | Sales Representative: 39.8% | Research Director: 2.5% |
| Tenure | 0 to 2 years: 29.8% | 11+ years: 8.1% |
| Income | Lowest quartile: 29.3% | Highest quartile: 10.3% |
| Stock options | Level 0 (none): 24.4% | Levels 1 and 2: 9.4% and 7.6% |
| Satisfaction | Low job and low environment satisfaction: 37.7% | Very high on both: 8.5% |

1. **Overtime is the strongest single factor.** Employees working overtime leave at about three times the rate of those who don't, across a large group (416 employees).
2. **Early career employees leave the most.** Ages 18 to 25, job level 1, tenure under 3 years, and the lowest income quartile all show elevated attrition. These groups overlap heavily, so they likely describe the same population.
3. **Two roles stand out.** Sales Representatives have the highest rate, while Laboratory Technicians (23.9%) matter more in absolute terms because the role is much larger (259 employees).
4. **No stock options is associated with higher attrition.** Employees with no stock grant leave at more than twice the rate of those at levels 1 and 2.
5. **Low satisfaction compounds.** Employees with low job satisfaction and low environment satisfaction leave at 37.7%, more than four times the rate of the most satisfied group.

## Recommendations

- Review overtime practices, especially in roles where overtime and attrition overlap.
- Strengthen onboarding and early career support during the first two years.
- Investigate pay, workload, and career paths for Sales Representatives and Laboratory Technicians.
- Evaluate extending stock option eligibility to employees currently at level 0.
- Use satisfaction survey results to flag at-risk teams early.

## Limitations

- The data is fictional and represents a single point in time, so it cannot show trends.
- Findings are associations, not proof of cause. Many factors overlap (for example, early career employees also tend to have lower pay and no stock options).
- Some groups are small (for example, stock option level 3 has 85 employees), so their rates are less stable. Filtered views on the dashboard can become small, and tooltips show the employee count for each group.

## Repository Files

| File | Description |
|---|---|
| `01_explore.py` | Initial data checks |
| `02_clean.py` | Cleaning and feature creation |
| `03_analysis.py` | Attrition rates by group and satisfaction cross-tab |
| `hr_attrition_clean.csv` | Cleaned dataset used in Tableau |

## How to Run

1. Download the dataset from Kaggle (search "IBM HR Analytics Employee Attrition & Performance").
2. Install pandas: `pip install pandas`
3. Update the file paths in the scripts to match where the CSV is saved, then run the scripts in order.
