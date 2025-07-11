# MSCS 634 – Deliverable 1: Data Collection, Cleaning, and Exploration  
## Exploring Powerlifting Data with Python  
Author: Jacob Jeffers

## Project Overview

For this first deliverable in my data mining course, I wanted to work with a dataset that genuinely interested me. As a fan of powerlifting, I chose the OpenPowerlifting dataset because it gave me the chance to analyze performance data from athletes around the world. The goal of this stage was to load, clean, and explore the dataset to prepare it for deeper analysis in future phases.

## About the Dataset

The OpenPowerlifting dataset contains results from competitive powerlifting meets worldwide. It includes detailed information such as lifter name, sex, age, bodyweight, equipment type, individual lift attempts, and scoring metrics like Wilks, Dots, and Glossbrenner.

- Total rows: 2,490,480  
- Total columns: 41  
- Data types: Numerical and categorical  
- Source: https://www.openpowerlifting.org

Due to GitHub’s file size limit, the dataset is not included directly in this repository. You can download it from:

**https://cumber-my.sharepoint.com/:x:/g/personal/jake_jeffers_ucumberlands_edu/EUOW6cDh4H5HhGnOB0nxkqMB7S5fa-XKwafkmZADM0-WfQ?e=iNyyi2**

## Data Cleaning Process

The dataset required substantial cleanup before it could be analyzed effectively. Here are the main steps I took:

- Removed columns with excessive missing values, including `Squat4Kg`, `Bench4Kg`, `Deadlift4Kg`, `Tested`, `MeetState`, and `MeetCountry`
- Dropped rows that were missing values in the `TotalKg` column
- Replaced missing `BodyweightKg` values with the column mean
- Removed duplicate records
- Retained some incomplete columns for potential use in later phases

## Exploratory Data Analysis (EDA)

After cleaning the data, I performed several visual and statistical analyses to better understand key trends and relationships.

**Total Weight Lifted**  
Most lifters had total lift values between 300 and 600 kilograms. A few extremely low or high values appear to be outliers or data entry issues.

**Sex Distribution**  
The dataset contains more male lifters than female lifters, though both are well represented.

**Performance by Sex**  
Boxplot analysis shows that men tend to lift more on average, but women display a wide and competitive range of performances.

**Correlation Analysis**  
There are strong positive correlations between `TotalKg` and each of the lifters' best squat, bench, and deadlift numbers. Performance scores such as Wilks and Dots also track closely with total lifted weight.

## Key Takeaways

- Summary lift values (`Best3SquatKg`, `Best3BenchKg`, `Best3DeadliftKg`) are more reliable than individual attempt data
- The dataset has high potential for regression and classification models
- Outliers and negative values will need to be cleaned further before modeling
- The data aligns well with known trends in powerlifting

## Challenges

- The dataset is nearly 800 MB, which made loading and processing slow at times
- Several columns had large amounts of missing data
- Negative or extreme values appear in some lift fields, indicating the need for validation in later phases

## Next Steps

- Engineer new features such as lift-to-bodyweight ratios
- Remove or correct invalid or extreme entries
- Develop regression models to predict `TotalKg`
- Explore classification models to predict lifter placement or medal status

## Files in This Repository

- `JupyterDataset.ipynb`: Jupyter Notebook containing code, visualizations, and insights
- `README.md`: This summary file

The raw dataset is not included due to size limits but can be downloaded using the link above.

## Personal Note

Powerlifting is something I follow closely, so working with this dataset was especially meaningful to me. It allowed me to combine personal interest with technical learning, and helped make the data mining process more engaging. I'm looking forward to building predictive models from this data in future deliverables.

# MSCS 634 – Deliverable 2: Regression Modeling and Evaluation  
## Predicting Powerlifting Totals Using Linear Models  
Author: Jacob Jeffers

## Project Overview

This phase of the project focused on using regression models to predict a lifter's `TotalKg` performance based on features in the OpenPowerlifting dataset. Since I enjoy powerlifting, I was curious to see how strongly a lifter's squat, bench, deadlift, and bodyweight could be used to estimate their meet total.

My goal was to build and evaluate several regression models and determine which one gave the most accurate results.

## Features Used

I selected four features that directly contribute to a lifter’s total:

- `Best3SquatKg`
- `Best3BenchKg`
- `Best3DeadliftKg`
- `BodyweightKg`

In addition, I created a new feature called `LiftRatio`, which is calculated by dividing `TotalKg` by `BodyweightKg`. This helped me explore the idea of relative strength.

Before training, I cleaned the data by dropping rows with missing values in these columns. I also scaled the features for regularization models.

## Models Trained

I trained the following models:

- Linear Regression
- Ridge Regression
- Lasso Regression

Each model was trained on 80 percent of the data and tested on the remaining 20 percent. For Ridge and Lasso, I applied feature scaling using `StandardScaler`.

## Evaluation Metrics

To compare the models, I used the following metrics:

- R² (coefficient of determination)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- 5-fold cross-validation

These metrics helped me evaluate both accuracy and generalization.

## Results Summary

All three models performed well, with R² values above 0.98. This makes sense considering how closely each lift contributes to the total. Ridge Regression gave the best balance of low error and high R². Lasso came in slightly behind due to more aggressive regularization.

| Model            | R² Score | MSE      | RMSE     |
|------------------|----------|----------|----------|
| Linear Regression| 0.982    | 2650.41  | 51.48    |
| Ridge Regression | 0.983    | 2603.28  | 51.02    |
| Lasso Regression | 0.979    | 2801.77  | 52.93    |

These numbers reflect a strong fit and reliable performance.

## Insights and Observations

- The three lifts are very strong predictors of a lifter’s total.
- Ridge Regression handled multicollinearity between the lifts slightly better than Linear or Lasso.
- Bodyweight helped improve predictions slightly but was less important than the actual lifts.
- The LiftRatio feature could be useful for classification or clustering, but it was not used as a predictor here.

## Challenges

One of the challenges I faced was scaling features for Lasso and Ridge while keeping the workflow simple. I also had to be careful not to include rows with missing or invalid values, since even one null can throw off a model.

Another challenge was balancing simplicity with model accuracy. It was tempting to include more features, but I decided to keep it focused and clean for this deliverable.

## Next Steps

In future work, I would like to:

- Include categorical variables like `Sex`, `Equipment`, and `Federation`
- Try non-linear models like decision trees or gradient boosting
- Use GridSearchCV to tune hyperparameters

## Files Included

- `deliverable2.ipynb`: Notebook containing the full workflow, code, and visualizations
- `README.md`: This project summary

The dataset is not included in this repository due to file size restrictions. You can download the same version I used from:

**https://cumber-my.sharepoint.com/:x:/g/personal/jake_jeffers_ucumberlands_edu/EUOW6cDh4H5HhGnOB0nxkqMB7S5fa-XKwafkmZADM0-WfQ?e=iNyyi2**
