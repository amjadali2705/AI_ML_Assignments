# Anomaly Detection with MLflow Experiment Tracking

## Project Overview

This project implements an end-to-end anomaly detection workflow using MLflow for experiment tracking, model registry management, and production model deployment.

The objective is to detect fraudulent transactions from a highly imbalanced dataset and compare multiple machine learning models while tracking all experiments in MLflow.

---

## Dataset

Dataset Source:

https://www.kaggle.com/datasets/kartik2112/fraud-detection

Files Used:

- fraudTrain.csv
- fraudTest.csv

**Note:** Dataset files are not included in this repository because of GitHub file size limitations. Download the dataset from Kaggle and place the files in the project root before running the notebook.

---

## Technologies Used

- Python 3.11
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Imbalanced-Learn (SMOTE)
- MLflow

---

## Project Workflow

### 1. Data Preprocessing

- Loaded fraud detection dataset
- Analyzed class distribution
- Sampled 200,000 records for efficient experimentation
- Removed unnecessary columns
- Encoded categorical variables using LabelEncoder
- Performed 70:30 stratified train-test split

### 2. Handling Class Imbalance

SMOTE (Synthetic Minority Oversampling Technique) was applied only on the training dataset.

Class distribution was recorded before and after resampling.

### 3. Models Evaluated

#### Logistic Regression

Parameters:

- C = 1
- solver = liblinear

#### Random Forest

Parameters:

- n_estimators = 30
- max_depth = 3

#### XGBoost

Parameters:

- eval_metric = logloss

#### XGBoost With SMOTE

Parameters:

- eval_metric = logloss
- SMOTE applied on training data

---

## MLflow Experiment Tracking

**Experiment Name:** Anomaly Detection MLflow

The following information was logged for every run:

### Parameters

- C
- solver
- n_estimators
- max_depth
- eval_metric
- sampling strategy

### Metrics

- accuracy
- recall_class_0
- recall_class_1
- f1_score_macro

### Artifacts

- Trained model artifact

---

## Results

| Model | Accuracy | Recall Class 1 | F1 Macro |
|---------|---------|---------|---------|
| Logistic Regression | 0.99405 | 0.00000 | 0.49851 |
| Random Forest | 0.99405 | 0.00000 | 0.49851 |
| XGBoost | 0.99630 | 0.59384 | 0.82724 |
| XGBoost With SMOTE | 0.99110 | 0.75070 | 0.74822 |

---

## Best Model

### Selected Model

**XGBoost With SMOTE**

### Reason

Although standard XGBoost achieved the highest accuracy, XGBoost with SMOTE achieved significantly higher recall for the fraud class. Since anomaly detection prioritizes identifying fraudulent transactions, recall for class 1 was considered the most important metric.

---

## Model Registry

### Registered Model

`anomaly-detector-xgb-smote`

### Alias

`@challenger`

### Production Model

`anomaly-detection-prod`

### Alias

`@champion`

---

## Production Inference

The production model was successfully loaded from the MLflow Model Registry and inference was executed on unseen test samples.

Example Output:

```python
[0 0 0 0 0 0 0 0 0 0]
```

---

## Screenshots

The screenshots folder contains all the relevant screenshots:

---

## How to Run

### Step 1: Install Dependencies

```bash
pip install pandas numpy scikit-learn xgboost imbalanced-learn mlflow
```

### Step 2: Start MLflow UI

```bash
mlflow ui --port 5000
```

Open:

```text
http://127.0.0.1:5000
```

### Step 3: Run Notebook

Open and execute:

```text
anomaly_detection_mlflow.ipynb
```

from start to finish.

---

## Repository Structure

```text
anomaly-detection-mlflow/
│
├── anomaly_detection_mlflow.ipynb
│
├── screenshots/
│   ├── 01_experiments_list.png
│   ├── 02_runs_comparison.png
│   ├── 03_best_run_details.png
│   ├── 04_model_registry.png
│   └── 05_production_model.png
│
├── report/
│   └── experiment_report.pdf
│
├── README.md
│
└── .gitignore
```

---

## Author

Md Amjad Ali

Capstone Project: Anomaly Detection with MLflow Experiment Tracking