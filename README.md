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

* **Project 2: Car Price Prediction**
  * **Dataset:** Ford Car Price Prediction dataset (`ford.csv`).
  * **EDA & Visualization:** Analyzed dimensions, handled duplicates, plotted histograms for numeric column distributions, and countplots for categorical distributions. Explored features and their relationship with target (`price`) using correlation heatmaps and boxplots.
  * **Data Preprocessing & Scaling:** Encoded categorical features (`model`, `transmission`, `fuelType`) using `OneHotEncoder` and standardized numerical features (`year`, `mileage`, `tax`, `mpg`, `engineSize`) using `StandardScaler` through `ColumnTransformer`.
  * **Implementation & Models:** Split the data (80% train, 20% test) and trained three models: **Linear Regression**, **Decision Tree Regressor**, and **Random Forest Regressor**.
  * **Performance & Results:**
    * **Linear Regression:**
      * **$R^2$ Score:** **81.89%**
      * **Adjusted $R^2$ Score:** **81.70%**
      * **MAE:** **1360.54**
    * **Decision Tree Regressor:**
      * **$R^2$ Score:** **88.05%**
      * **Adjusted $R^2$ Score:** **87.93%**
      * **MAE:** **1090.39**
    * **Random Forest Regressor (Best Model):**
      * **$R^2$ Score:** **92.40%**
      * **Adjusted $R^2$ Score:** **92.32%**
      * **MAE:** **891.68**

* **Project 3: Titanic Survival Prediction**
  * **Dataset:** Titanic Survival dataset loaded from Seaborn (`sns.load_dataset("titanic")`).
  * **EDA & Visualization:** Checked dataset dimensions, dropped duplicate rows, handled missing values, and analyzed feature distribution (skewness, outliers).
  * **Feature Selection & Engineering (Iterative Optimization):**
    * Conducted iterative trial-and-error to optimize feature selection and model accuracy:
      * Initially included `sex` and `age` columns, yielding an accuracy of **77%**.
      * Removing the `age` column bumped the accuracy to **78%**.
      * Replacing `sex` with `adult_male` (removing both `age` and `sex` completely) significantly improved the model's accuracy to the final **82.17%**.
    * Dropped other redundant/high-cardinality/redundant features (`deck`, `who`, `embarked`, `class`, `sex`, `alive`, `age`) and cast `alone` and `adult_male` to integer types.
  * **Data Preprocessing & Scaling:** Scaled and imputed numeric features (`pclass`, `parch`, `sibsp`, `fare`) using `SimpleImputer` (median) and `StandardScaler`. Imputed and encoded `embark_town` using `SimpleImputer` (most frequent) and `OneHotEncoder` (dropping the first category). Passed through `alone` and `adult_male` as-is. Preprocessing steps were bundled using `ColumnTransformer` and `Pipeline` with pandas DataFrame output configured.
  * **Implementation & Model:** Split the data (80% train, 20% test) and trained a **Logistic Regression** model using `scikit-learn`.
  * **Performance & Results:**
    * **Accuracy:** **82.17%**
    * **Confusion Matrix:** 78 True Negatives, 10 False Positives, 18 False Negatives, 51 True Positives
    * **Classification Report:**
      * **Not Survived (Class 0):** Precision: **81%** | Recall: **89%** | F1-Score: **85%**
      * **Survived (Class 1):** Precision: **84%** | Recall: **74%** | F1-Score: **78%**

---

## 📂 Repository Structure

```text
AI-ML-Learning-Journey/
├── 01_Python/                                  # Python Basics, OOP, Practice & Projects
│   └── Projects/                               # Python mini-projects & practice scripts
├── 02_Numpy/                                   # Numerical Computing & Array Slicing
├── 03_EDA/                                     # Exploratory Data Analysis Projects
│   ├── Project_1/                              # Insurance Charges EDA Project
│   └── Project_2/                              # Heart Disease EDA Project
├── 04_Machine_Learning/                        # Machine Learning Projects & Modeling
│   ├── Project_1_Insurance_Charges_Prediction/ # Insurance Charges Prediction Project
│   ├── Project_2_Car_Price_Prediction/         # Car Price Prediction Project
│   └── Project_3_Titanic_Survival_Prediction/  # Titanic Survival Prediction Project
├── requirements.txt                            # Essential Python packages & dependencies
└── README.md                                   # Repository Documentation
```


---

## 👤 Author

**Syed Ali Mehdi Bukhari**

---

## 📝 License
This repository is open-source and available under the [MIT License](LICENSE).
