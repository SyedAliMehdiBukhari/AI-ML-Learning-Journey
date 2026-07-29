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
* **Project 2: Heart Disease Prediction EDA & Preprocessing**
  * **Exploration:** Checked data distribution, duplicates, and missing values. Visualized numeric distributions using histograms, analyzed categorical distributions using countplots, and analyzed linear relationships with a correlation heatmap.
  * **Data Cleaning & Imputation:** Identified invalid `0` values in `Cholesterol` and `RestingBP` columns, replaced them with `NaN`, and imputed them with the respective column means.
  * **Data Preprocessing & Scaling:** Performed one-hot encoding for categorical variables using dummy encoding, and standardized numeric columns (`Age`, `RestingBP`, `Cholesterol`, `MaxHR`, `Oldpeak`) using `StandardScaler`.

### 4. 🤖 Machine Learning (`04_Machine_Learning/`)
* **Project 1: Medical Insurance Charges Prediction**
  * **Dataset:** Trained on the dataset preprocessed and cleaned by myself during the EDA phase (from the Medical Insurance Charges EDA & Feature Selection project).
  * **Implementation:** Developed and trained a **Linear Regression** model using `scikit-learn` to predict medical insurance costs.
  * **Performance & Results:**
    * **$R^2$ Score:** **90.41%**
    * **Adjusted $R^2$ Score:** **90.19%**

---

## 📂 Repository Structure

```text
AI-ML-Learning-Journey/
├── 01_Python/              # Python Basics, OOP, Practice & Projects
│   └── Projects/           # Python mini-projects & practice scripts
├── 02_Numpy/               # Numerical Computing & Array Slicing
├── 03_EDA/                 # Exploratory Data Analysis Projects
│   ├── Project_1/          # Medical Insurance Charges Project
│   └── Project_2/          # Heart Disease Prediction Project
├── 04_Machine_Learning/    # Machine Learning Projects & Modeling
│   └── Project_Insurance_Charges_Prediction/ # Insurance Charges Prediction Project
├── requirements.txt        # Essential Python packages & dependencies
└── README.md               # Repository Documentation
```

---

## 👤 Author

**Syed Ali Mehdi Bukhari**

---

## 📝 License
This repository is open-source and available under the [MIT License](LICENSE).
