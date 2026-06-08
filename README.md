# 📈 Sales Forecasting and Demand Prediction Dashboard

## 📌 Project Overview

This project focuses on forecasting future sales using historical retail transaction data. The objective is to help businesses estimate future demand, identify sales patterns, and support data-driven decision-making.

The project includes:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Time-based Feature Engineering
- Sales Forecasting using Machine Learning
- Model Evaluation and Error Analysis
- Interactive Streamlit Dashboard

## 🎯 Project Objectives

- Analyze historical sales data.
- Perform data cleaning and preprocessing.
- Create time-based features for forecasting.
- Build machine learning models for sales prediction.
- Evaluate model performance using standard regression metrics.
- Forecast future sales.
- Visualize results through an interactive dashboard.
- Generate business-friendly insights and recommendations.

## 📊 Dataset Information

The dataset contains retail transaction records including:

- Invoice Number
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Unit Price
- Customer ID
- Country

The dataset was aggregated into daily sales to create a time-series forecasting problem.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Seaborn
- Streamlit
- Jupyter Notebook

## 🔄 Project Workflow

### 1. Data Collection

- Imported retail sales dataset.
- Loaded data into Pandas DataFrame.

### 2. Data Cleaning

- Removed missing values.
- Removed duplicate records.
- Handled invalid transactions.
- Converted date column into datetime format.

### 3. Feature Engineering

Created time-based features:

- Month
- Day
- Day of Week
- Quarter

Created lag features:

- Lag1
- Lag7
- Lag14
- Lag30

Created rolling statistics:

- Rolling Mean 7 Days
- Rolling Mean 14 Days
- Rolling Mean 30 Days

### 4. Exploratory Data Analysis (EDA)

Performed:

- Daily Sales Trend Analysis
- Monthly Sales Trend Analysis
- Sales by Weekday Analysis
- Correlation Heatmap
- Feature Importance Analysis

### 5. Data Preparation

- Train-Test Split using Time-Based Splitting
- Feature Scaling for Linear Regression

### 6. Model Building

Implemented:

#### Linear Regression

Used as a baseline forecasting model.

#### Random Forest Regressor

Used to capture non-linear relationships in sales patterns.

### 7. Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### 8. Future Forecasting

Generated future sales forecasts using the best-performing model.

### 9. Dashboard Development

Developed an interactive Streamlit dashboard to display:

- Historical Sales Trends
- Forecasted Sales
- Business KPIs
- Forecast Table

## 📈 Features Created

|    Feature      |      Description     |
|-----------------|----------------------|
|    Month        | Month of transaction |
|     Day         |     Day of month     |
|   DayOfWeek     |     Day of week      |
|    Quarter      |   Quarter of year    |
|     Lag1        |  Previous day sales  |
|     Lag7        |  Previous week sales |
|     Lag14       |  Sales 14 days ago   |
|     Lag30       |  Sales 30 days ago   |
| Rolling_Mean_7  | 7-day average sales  |
| Rolling_Mean_14 | 14-day average sales |
| Rolling_Mean_30 | 30-day average sales |

## 📊 Model Performance

|            Model        |    MAE   |    RMSE  | R² Score |
|-------------------------|---------:|---------:|---------:|
| Linear Regression       | 12639.62 | 19719.63 | 0.482298 |
| Random Forest Regressor | 15299.59 | 25334.64 | 0.145501 |

Linear Regression achieved a higher R² score and lower prediction errors on unseen data, so it was selected as the final model. Predictive performance was prioritized rather than model complexity.

## 📉 Forecast Output

The model predicts future daily sales based on historical sales patterns and engineered time-series features.

|    Date    | Forecasted Sales |
|---------   |-----------------:|
| 2011-12-10 |	 43538.302568   |
| 2011-12-11 |	 68872.792581   |
| 2011-12-12 |	 63773.513923   |
| 2011-12-13 |	 69886.432643   |
| 2011-12-14 |	 71820.494137   |
| 2011-12-15 |	 67250.973933   |
| 2011-12-16 |	 57175.682342   |
| 2011-12-17 |	 85721.244047   |
| 2011-12-18 |	 74106.131794   |
| 2011-12-19 |	 75364.690249   |
| 2011-12-20 |	 71158.349558   |
| 2011-12-21 |	 64749.752748   |
| 2011-12-22 |	 56112.283842   |
| 2011-12-23 |	 74301.382864   |
| 2011-12-24 |	 61026.963125   |
| 2011-12-25 |	 61219.201870   |
| 2011-12-26 |	 55076.331582   |
| 2011-12-27 |	 52121.038935   |
| 2011-12-28 |	 41110.491268   |
| 2011-12-29 |	 61173.091705   |
| 2011-12-30 |	 60989.562850   |
| 2011-12-31 |	 57671.701517   |
| 2012-01-01 |	 55538.037699   |
| 2012-01-02 |	 54519.979098   |
| 2012-01-03 |	 44322.486812   |
| 2012-01-04 |	 73224.766332   |
| 2012-01-05 |	 67277.356556   |
| 2012-01-06 |	 66710.880959   |
| 2012-01-07 |	 67504.686421   |
| 2012-01-08 |	 93035.116480   |

## 📊 Dashboard Features

The Streamlit dashboard includes:

### Historical Sales Analysis

- Daily Sales Trend
- Monthly Sales Trend
- Average Sales by Day of Week

### Forecasting

- Future Sales Forecast
- Forecast Visualization

### Business KPIs

- Average Sales
- Maximum Sales
- Forecast Average Sales

### Data Tables

- Forecast Results

## 💡 Key Business Insights

- Past sales patterns play a significant role in forecasting future demand.
- Customer purchasing behavior follows a weekly cycle.
- Lag-based features are strong predictors of future demand.
- Monthly sales trends showed fluctuations throughout the year, indicating seasonality in customer demand.
- Forecasting can support inventory planning and resource allocation.


## Live App

https://futureml01-pmyeloebhacfjkmgqbaqxs.streamlit.app/

## 👩‍💻 Author

Sweta Agarwal

MSc. Statistics Student | Data Analytics & Machine Learning Enthusiast

