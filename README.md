# 🚀 AI & Machine Learning | Learning Journey

Welcome to my **AI & Machine Learning | Learning Journey** repository! This repository serves as a structured, hands-on record of my learning path in Python, Data Science, and Machine Learning.

---

## 💻 Tech Stack & Libraries

- **Language:** `Python`
- **Environment:** `Jupyter Notebook` / `IPython Kernel`
- **Data Manipulation:** `numpy`, `pandas`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Data Analysis & Statistics:** `statsmodels`
- **Machine Learning & Web Apps:** `scikit-learn`, `streamlit`

---

## 📚 Modules

### 1. 🐍 Core Python & OOP (`01_Python/`)
* **Core Concepts:** Variables, Input/Type Casting, Control Flow (Conditional logic, Loops), Functions, Data Structures (Lists, Dicts, Tuples, Sets).
* **Object-Oriented Programming (OOP):** Classes, Objects, and the 4 pillars (Encapsulation, Inheritance, Polymorphism, Abstraction).
* **Advanced Basics:** File Handling, Exception Handling (`try-except`), Random Module, String Manipulation.
* **Practice & Projects:** Hands-on practice notebooks and mini-projects (e.g., automated tools/scripts in the `Projects/` directory).

### 2. 🔢 Numerical Computing with NumPy (`02_Numpy/`)
* High-performance array creation methods (zeros, ones, arange, linspace, random).
* Dimension manipulation, shape checking, indexing, and advanced slicing techniques.

### 3. 📊 Exploratory Data Analysis (`03_EDA/`)
* **Project 1: Medical Insurance Charges EDA & Feature Selection**
  * **Exploration:** Analyzed data distribution (skewness, kurtosis), outliers, and bivariate relationships with heatmaps.
  * **Data Cleaning & Preprocessing:** Binary mapping (`is_smoker`, `is_female`), one-hot encoding for categorical variables (`region`, `bmi_category`), and feature scaling using `StandardScaler`.
  * **Feature Selection:** 
    * Checked and resolved multicollinearity (Dummy Variable Trap) using **Variance Inflation Factor (VIF)**.
    * Used **OLS Regression (via `statsmodels`)** to eliminate statistically insignificant features (p-value > 0.05).
  * **Feature Engineering:** Added a non-linear interaction term (`smoker_obese_interaction` = Smoker × Obese) which boosted the model's $R^2$ score from **75.4% to 85.9%**!
  * **Output:** Exported the final optimized dataset to `insurance_cleaned.csv`.
* **Project 2:** *Upcoming Project...*

---

## 📂 Repository Structure

```text
AI-ML-Learning-Journey/
├── 01_Python/              # Python Basics, OOP, Practice & Projects
│   └── Projects/           # Python mini-projects & practice scripts
├── 02_Numpy/               # Numerical Computing & Array Slicing
├── 03_EDA/                 # Exploratory Data Analysis Projects
│   ├── Project_1/          # Medical Insurance Charges Project
│   │   ├── insurance.csv            # Raw dataset
│   │   ├── insurance_charges.ipynb  # EDA & Statistical Modeling Notebook
│   │   └── insurance_cleaned.csv    # Final processed dataset
│   └── Project_2/          # (Upcoming project)
├── requirements.txt        # Essential Python packages & dependencies
└── README.md               # Repository Documentation
```

---

## 👤 Author

**Syed Ali Mehdi Bukhari**

---

## 📝 License
This repository is open-source and available under the [MIT License](LICENSE).
