"""
Assignment 6 Part 1: Student Performance Prediction
Name: _______________
Date: _______________

This assignment predicts student test scores based on hours studied.
Complete all the functions below following the in-class ice cream example.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def load_and_explore_data(filename):
    """
    Load the student scores data and explore it
    
    Args:
        filename: name of the CSV file to load
    
    Returns:
        pandas DataFrame containing the data
    """
    # TODO: Load the CSV file using pandas
    data = pd.read_csv(filename)
    # TODO: Print the first 5 rows
    print("=== Student Scores Data ===")
    print(f"\nFirst 5 Rows:")
    print(data.head())
    # TODO: Print the shape of the dataset (number of rows and columns)
    print(f"\nDataset Shape: {data.shape[0]} rows, {data.shape[1]} columns")
    # TODO: Print basic statistics (mean, min, max, etc.)
    print(f"\nBasic Statistics:")
    print(data.describe())
    # TODO: Return the dataframe
    return data


def create_scatter_plot(data):
    """
    Create a scatter plot to visualize the relationship between hours studied and scores
    
    Args:
        data: pandas DataFrame with Hours and Scores columns
    """
    # TODO: Create a figure with size (10, 6)
    plt.figure(figsize=(10,6))
    # TODO: Create a scatter plot with Hours on x-axis and Scores on y-axis
    #       Use color='purple' and alpha=0.6
    plt.scatter(data['Hours'], data['Scores'], color='purple', alpha=0.6)
    # TODO: Add x-axis label: 'Hours Studied'
    plt.xlabel('Hours Studied', fontsize=12)
    # TODO: Add y-axis label: 'Test Score'
    plt.ylabel('Test Score', fontsize=12)
    # TODO: Add title: 'Student Test Scores vs Hours Studied'
    plt.title('Student Test Scores vs Hours Studied', fontsize=14, fontweight='bold')
    # TODO: Add a grid with alpha=0.3
    plt.grid(True, alpha=0.3)
    # TODO: Save the figure as 'scatter_plot.png' with dpi=300
    plt.savefig('scatter_plot.png', dpi=300, bbox_inches='tight')
    print("\nScatterplot saved as 'scatter_plot.png'")
    # TODO: Show the plot
    plt.show()


def split_data(data):
    """
    Split data into features (X) and target (y), then into training and testing sets
    
    Args:
        data: pandas DataFrame with Hours and Scores columns
    
    Returns:
        X_train, X_test, y_train, y_test
    """
    # TODO: Create X with the 'Hours' column (use double brackets to keep as DataFrame)
    X = data[['Hours']]
    # TODO: Create y with the 'Scores' column
    y = data['Scores']
    # TODO: Split the data using train_test_split with test_size=0.2 and random_state=42
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # TODO: Print how many samples are in training and testing sets
    print(f"\n=== Data Split ===")
    print(f"Training Set: {len(X_train)} samples")
    print(f"Testing set: {len(X_test)} samples")
    # TODO: Return X_train, X_test, y_train, y_test
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """
    Create and train a linear regression model
    
    Args:
        X_train: training features
        y_train: training target values
    
    Returns:
        trained LinearRegression model
    """
    # TODO: Create a LinearRegression model
    model = LinearRegression()
    # TODO: Train the model using .fit()
    model.fit(X_train, y_train)
    # TODO: Print the coefficient (slope) and intercept
    print(f"\n=== Model Training Complete ===")
    print(f"Slope (coefficient): {model.coef_[0]:.2f}")
    print(f"Intercept: {model.intercept_:.2f}")
    print(f"\nEquation: Sales = {model.coef_[0]:.2f} × Hours + {model.intercept_:.2f}")
    # TODO: Return the trained model
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model's performance on test data
    
    Args:
        model: trained LinearRegression model
        X_test: testing features
        y_test: testing target values
    
    Returns:
        predictions array
    """
    # TODO: Make predictions using the model
    predictions = model.predict(X_test)
    # TODO: Calculate R² score using r2_score()
    r2 = r2_score(y_test, predictions)
    # TODO: Calculate Mean Squared Error using mean_squared_error()
    mse = mean_squared_error(y_test, predictions)
    # TODO: Calculate Root Mean Squared Error (square root of MSE)
    rmse = np.sqrt(mse)
    # TODO: Print all three metrics with clear labels
    print(f"\n=== Model Performance ===")
    print(f"R² Score: {r2:.4f}")
    print(f"  → Interpretation: The model explains {r2*100:.2f}% of the variance in sales")
    
    print(f"\nMean Squared Error: ${mse:.2f}")
    print(f"Root Mean Squared Error: ${rmse:.2f}")
    print(f"  → Interpretation: On average, predictions are off by ${rmse:.2f}")
    # TODO: Return the predictions
    return predictions


def visualize_results(X_train, y_train, X_test, y_test, predictions, model):
    """
    Visualize the model's predictions against actual values
    
    Args:
        X_train: training features
        y_train: training target values
        X_test: testing features
        y_test: testing target values
        predictions: model predictions on test set
        model: trained model (to plot line of best fit)
    """
    # TODO: Create a figure with size (12, 6)
    plt.figure(figsize=(12,6))
    # TODO: Plot training data as blue scatter points with label 'Training Data'
    plt.scatter(X_train, y_train, color='blue', alpha=0.5, label='Training Data')
    # TODO: Plot test data (actual) as green scatter points with label 'Test Data (Actual)'
    plt.scatter(X_test, y_test, color='green', alpha=0.7, label='Test Data (Actual)')
    # TODO: Plot predictions as red X markers with label 'Predictions'
    plt.scatter(X_test, predictions, color='red', alpha=0.7, label='Predictions', marker='x', s=100)
    # TODO: Create and plot the line of best fit
    #       Hint: Create a range of X values, predict Y values, then plot as a black line
    X_range = np.linspace(X_train.min(), X_train.max(), 100).reshape(-1, 1)
    y_range = model.predict(X_range)
    plt.plot(X_range, y_range, color='black', linewidth=2, label='Line of Best Fit')
    # TODO: Add x-axis label, y-axis label, and title
    plt.xlabel('Hours Studied', fontsize=12)
    plt.ylabel('Test Score', fontsize=12)
    plt.title('Linear Regression: Student Scores Prediction', fontsize=14, fontweight='bold')
    # TODO: Add legend
    plt.legend()
    # TODO: Add grid with alpha=0.3
    plt.grid(True, alpha=0.3)
    # TODO: Save the figure as 'predictions_plot.png' with dpi=300
    plt.savefig('predictions_plot.png', dpi=300, bbox_inches='tight')
    print("\n✓ Predictions plot saved as 'predictions_plot.png'")
    # TODO: Show the plot
    plt.show()


def make_prediction(model, hours):
    """
    Make a prediction for a specific number of hours studied
    
    Args:
        model: trained LinearRegression model
        hours: number of hours to predict score for
    
    Returns:
        predicted test score
    """
    # TODO: Reshape hours into the format the model expects: np.array([[hours]])
    hours_array=np.array([[hours]])
    # TODO: Make a prediction
    predicted_scores = model.predict(hours_array)[0]
    # TODO: Print the prediction with a clear message
    print(f"\n=== New Prediction ===")
    print(f"If hours studied is {hours} hours, predicted scores: ${predicted_scores:.2f}")
    # TODO: Return the predicted score
    return predicted_scores


if __name__ == "__main__":
    print("=" * 70)
    print("STUDENT PERFORMANCE PREDICTION - YOUR ASSIGNMENT")
    print("=" * 70)
    
    # Step 1: Load and explore the data
    # TODO: Call load_and_explore_data() with 'student_scores.csv'
    data = load_and_explore_data('student_scores.csv')
    # Step 2: Visualize the relationship
    # TODO: Call create_scatter_plot() with the data
    create_scatter_plot(data)
    # Step 3: Split the data
    # TODO: Call split_data() and store the returned values
    X_train, X_test, y_train, y_test = split_data(data)
    # Step 4: Train the model
    # TODO: Call train_model() with training data
    model = train_model(X_train, y_train)
    # Step 5: Evaluate the model
    # TODO: Call evaluate_model() with the model and test data
    predictions = evaluate_model(model, X_test, y_test)
    # Step 6: Visualize results
    # TODO: Call visualize_results() with all the necessary arguments
    visualize_results(X_train, y_train, X_test, y_test, predictions, model)
    # Step 7: Make a new prediction
    # TODO: Call make_prediction() for a student who studied 7 hours
    make_prediction(model, 7)
    print("\n" + "=" * 70)
    print("✓ Assignment complete! Check your saved plots.")
    print("Don't forget to complete a6_part1_writeup.md!")
    print("=" * 70) 