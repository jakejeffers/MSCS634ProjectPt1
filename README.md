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
