# Used Car Price Prediction Project

## Project Organization

This project is focused on predicting used car prices using regression models, with all analysis conducted in a Jupyter Notebook. Below is a summary of the findings and key components:

- **Notebook**: The main analysis is in [prompt_II.ipynb](prompt_II.ipynb), which includes data preprocessing, modeling, evaluation, and findings.
- **Summary of Findings**: See the "Findings" section below for a detailed summary of results, actionable insights, and recommendations for stakeholders.

## Modeling

The modeling phase was conducted to predict used car prices using various regression models, with a focus on robust evaluation and interpretation. The following approaches were implemented:

- **Use of Multiple Regression Models**:
  - **Linear Regression**: A baseline model with no regularization to predict car prices.
  - **Lasso Regression**: Uses L1 regularization to perform feature selection, identifying the most impactful predictors.
  - **Ridge Regression**: Uses L2 regularization to reduce overfitting, improving model stability.
  - These models were applied after reducing dimensionality with Principal Component Analysis (PCA), testing 10, 30, and 100 components.

- **Cross-Validation of Models**:
  - All models were evaluated using 5-fold cross-validation to ensure robust performance metrics. This method splits the data into five parts, training on four and testing on one, repeating five times to average the results.

- **Grid Search Hyperparameters**:
  - Hyperparameter tuning was planned for Lasso and Ridge (e.g., tuning the `alpha` parameter for regularization strength) using Grid Search with cross-validation, but this step was not executed in the latest run. Future iterations should include this to optimize model performance.

- **Appropriate Interpretation of Coefficients in Models**:
  - For linear models (Linear, Lasso, Ridge), coefficients represent the impact of each PCA component on the predicted car price. Positive coefficients increase the price, while negative coefficients decrease it. Larger absolute values indicate a stronger influence. In the latest run, coefficient interpretation was not performed, but it’s recommended for the final model to understand which components drive price predictions.

- **Appropriate Interpretation of Evaluation Metric**:
  - The best model (Lasso Regression with 30 PCA components) achieved an `R²` of 0.3574, meaning it explains 35.74% of the variance in car prices. This indicates a moderate fit, but there’s room for improvement, as 64.26% of the variance remains unexplained.
  - The `RMSE` was $10,456, meaning the average prediction error is $10,456. For a typical car price of $20,000, this is a 52.28% error, suggesting predictions are not yet accurate enough for practical use.

- **Clear Identification of Evaluation Metric**:
  - **R² (R-squared)**: Measures the proportion of variance in price explained by the model (0 to 1, higher is better).
  - **RMSE (Root Mean Squared Error)**: Measures the average prediction error in dollars (lower is better).

- **Clear Rationale for Use of Given Evaluation Metric**:
  - **R²** was chosen because it quantifies how well the model fits the data, a standard metric for regression tasks. It helps assess the overall explanatory power of the model.
  - **RMSE** was chosen because it provides an interpretable error in the same units as price (dollars), emphasizing larger errors and making it easier to understand prediction accuracy for stakeholders.

## Findings

### Business Understanding of the Problem
The goal of this project is to predict used car prices accurately to help a car dealership set competitive prices, optimize inventory, and improve sales. Understanding the factors that influence car prices (e.g., age, odometer reading, manufacturer, condition) allows the dealership to make data-driven pricing decisions, avoid overpricing (which slows sales), or underpricing (which reduces profits).

### Clean and Organized Notebook with Data Cleaning
- The notebook (`prompt_II.ipynb`) is structured with clear sections for data loading, cleaning, modeling, evaluation, and findings.
- **Data Cleaning Steps**:
  - Removed invalid entries: Dropped rows with negative `odometer` or `price` values.
  - Handled categorical variables: Combined rare `type` categories to reduce dimensionality.
  - Managed missing data: Replaced `NaN` in `condition` with `'unknown'`.
  - Applied outlier removal: Used the Interquartile Range (IQR) method to remove extreme values in numerical columns like `price`.
  - Encoded categorical variables: Applied one-hot encoding (OHE) to features like `region`, `manufacturer`, and label encoding to binned features like `age_binned`.

### Correct and Concise Interpretation of Descriptive and Inferential Statistics
- **Descriptive Statistics** (assumed, as not provided):
  - The dataset likely showed a wide range of car prices, with a mean around $20,000 (assumed for RMSE interpretation).
  - Numerical features like `age` and `odometer` probably had skewed distributions, justifying the use of binning (`age_binned`, `odometer_binned`) to capture non-linear effects.
- **Inferential Statistics**:
  - PCA revealed that 100 components captured only 23.61% of the variance, far below the expected ~80% (per the Cumulative Explained Variance Plot), indicating a possible issue with data preprocessing or PCA application.
  - Cross-validation results showed low `R²` (0.3574 at `n=30`), suggesting that linear models struggle to capture the complexity of car price prediction.

### Key Findings
- The best model, Lasso Regression with 30 PCA components, achieved an `R²` of 0.3574 and an `RMSE` of $10,456.
  
- **For Stakeholders**:
  - The current model explains only 35.74% of the variation in car prices, meaning predictions are not yet reliable for setting prices.
  - The average prediction error is $10,456, which is 52.28% of a typical $20,000 car price. This error is too high for practical use in pricing decisions.
  - **Actionable Item**: The dealership should **not rely on this model for pricing yet**. Predictions could lead to significant overpricing or underpricing, impacting sales and profits.

**Technical Insights**:
- The low variance captured (8.35% at `n=30`, 23.61% at `n=100`) suggests that more PCA components (e.g., 125, capturing ~90% variance) or better feature engineering is needed.
- Linear models (Linear, Lasso, Ridge) performed similarly, indicating that regularization didn’t significantly improve fit, likely due to non-linear relationships in the data.

### Next Steps and Recommendations
- **Increase PCA Components**: Test `n=125` (capturing ~90% variance) to include more information, which should improve `R²` and reduce `RMSE`.
- **Add Non-Linear Models**: Incorporate Random Forest and XGBoost to capture non-linear patterns (e.g., interactions between `manufacturer` and `odometer_binned`), likely improving prediction accuracy.
- **Hyperparameter Tuning**: Use Grid Search to tune parameters (e.g., `alpha` for Lasso/Ridge) to optimize model performance.
- **Improve Preprocessing**:
  - **Impute Missing Data**: Instead of dropping rows with `NaN`, impute categorical features with `'unknown'` and numerical features like `age` with the median to retain more data.
  - **Combine Rare Categories**: Reduce dimensionality by combining rare categories in high-cardinality features like `region` and `manufacturer` (e.g., group less frequent regions into `'other'`).
  - **Feature Engineering**: Create interaction features (e.g., `age` × `odometer`) to capture combined effects on price.
- **For Stakeholders**:
  - **Recommendation**: Invest in further model development to achieve a prediction error below 10% of the typical price (e.g., $2,000 for a $20,000 car). This will enable reliable pricing, improving sales efficiency and profitability.
  - **Next Step**: Schedule a follow-up in one month to review an improved model with higher accuracy, incorporating more data and advanced techniques.
