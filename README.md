# Used Car Price Prediction

## Project Overview

This project predicts the selling price of a used car using Machine Learning.

The model uses details such as:
- Car manufacturing year
- Kilometres driven
- Fuel type
- Seller type
- Transmission
- Owner type

## Machine Learning Model

Three regression models were tested:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

Gradient Boosting gave the best results among the tested models.

### Model Performance

- Mean Absolute Error (MAE): ₹179,430.44
- R² Score: 0.4676

## Project Structure

```text
Used-Car-Price-Prediction/
│
├── dataset/
│   ├── used_cars.csv
│   ├── cleaned_cars.csv
│   └── prepared_cars.csv
│
├── check_data.py
├── analyze_data.py
├── clean_data.py
├── visualize_data.py
├── prepare_data.py
├── check_prepared.py
├── train_model.py
├── predict_price.py
├── model.pkl
├── requirements.txt
└── README.md