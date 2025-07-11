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
