"""
Suppose your production model suddenly deteriorates. How would you debug it?

- Verify whether problem is real?
    - Compare with historical metrics
    - Verify that the evaluation pipeline is correct
    - Check RMSE/MAE/R-square

- Check for data drift
    - Has the input distribution changed ?
        - New customer segment
        - Different geography
        - Seasonality

- Check for concept drift:
    - Are the features computed differently on production
    - Example:
        - Training: Annual salary
        - Production: Monthly salary
- Check data quality:
    - Missing values
    - Nulls
    - New categories
    - Pipeline bugs

- Check Model itself:
    - Overfitting
    - Wrong training
    - Hyperparameters changes


"""