# Vibe Kaggling

A repository for Kaggle competition entries using Cursor's AI agent features. This repository contains various projects tackling different Kaggle competitions with a focus on leveraging AI assistance for competitive data science.

## Getting Started

### Creating a New Project

To create a new project for a Kaggle competition, use the `create_project.py` script:

```bash
# Basic usage
python create_project.py <project_name>

# With competition URL
python create_project.py <project_name> --competition <competition_url>

# Example
python create_project.py titanic --competition https://www.kaggle.com/competitions/titanic
```

This will create a new directory with the necessary folder structure and starter files.

### Project Structure

Each project follows this basic structure:

```
project_name/
├── data/                 # Data files (not tracked by git)
│   ├── raw/              # Original, immutable data
│   ├── processed/        # Cleaned, transformed data
│   └── submissions/      # Submission files
├── notebooks/            # Jupyter notebooks for exploration and analysis
├── src/                  # Source code for feature engineering and modeling
└── README.md             # Project documentation
```

## Approach to Kaggle Competitions

### 1. Problem Understanding

- Define the problem statement (e.g., predicting passenger transport to another dimension)
- Understand the evaluation metric (accuracy, RMSE, etc.)
- Review competition guidelines and submission format

### 2. Exploratory Data Analysis (EDA)

- Load and examine the data structure
- Check basic statistics (mean, median, missing values, etc.)
- Visualize distributions of features
- Analyze correlations between features
- Identify patterns in the target variable

### 3. Data Cleaning

- Handle missing values
- Address outliers
- Fix inconsistent data
- Create a data preprocessing pipeline

### 4. Feature Engineering

- Extract information from complex features
- Create interaction features
- Transform skewed numerical features
- Encode categorical variables
- Scale numerical features

### 5. Baseline Modeling

- Split data into training and validation sets
- Train simple models (logistic regression, decision tree)
- Evaluate baseline performance
- Identify improvement areas

### 6. Advanced Modeling

- Try ensemble methods (Random Forest, XGBoost, etc.)
- Experiment with neural networks if appropriate
- Implement cross-validation
- Tune hyperparameters systematically

### 7. Model Evaluation

- Compare model performances
- Analyze feature importance
- Check for overfitting
- Review error patterns

### 8. Prediction and Submission

- Make final predictions on test data
- Format submission according to requirements
- Submit and track results
- Iterate based on feedback

### 9. Documentation

- Document approach
- Note key insights from EDA
- Explain feature engineering decisions
- Summarize model performance

## Projects

Each subdirectory in this repository represents a different Kaggle competition:

*Projects will be added as they are created*

## License

[MIT](LICENSE) 