# Employee Data Analysis and Visualization

## 1. Project Overview

This project analyzes employee data using Python, Pandas, and Matplotlib.

The main objective is to understand employee salary patterns, department-wise salary differences, age distribution, and the relationship between age and salary.

## 2. Dataset

The project uses `employees.csv`, which contains 20 employee records and 8 columns:

- Employee ID
- Name
- Age
- Salary
- Department
- City
- Experience Years
- Gender

## 3. Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Jupyter nbconvert

## 4. Project Structure

```text
task3.visuvalization/
│
├── employees.csv
├── task3.ipynb
├── requirements.txt
├── README.md
│
├── report/
│   ├── summary.md
│   └── task3.html
│
└── reports/
    └── figures/
        ├── 01_department_salary.png
        ├── 02_age_histogram.png
        ├── 03_age_salary_scatter.png
        ├── 04_salary_line_chart.png
        └── 05_salary_boxplot.png
```

## 5. Installation

### Step 1: Create a virtual environment

```powershell
python -m venv .venv
```

### Step 2: Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install required libraries

```powershell
python -m pip install -r requirements.txt
```

## 6. Run the Project

Open the project folder in VS Code and run:

```powershell
jupyter notebook
```

Open `task3.ipynb` and execute the notebook cells from top to bottom.

## 7. Export Notebook as HTML

To generate the HTML report, run:

```powershell
python -m jupyter nbconvert --to html task3.ipynb --output-dir report
```

Open the generated report:

```text
report/task3.html
```

## 8. Key Findings

1. Finance has the highest average salary at ₹79,500.
2. Sales has the lowest average salary at ₹42,600.
3. Age and salary have a strong positive correlation of approximately 0.983.

## 9. Recommendations

1. Review salary differences across departments.
2. Consider employee experience, skills, and responsibilities when reviewing compensation.

## 10. Limitations

- The dataset contains only 20 employees.
- The analysis does not prove cause-and-effect relationships.
- Job roles and employee performance ratings are not included.