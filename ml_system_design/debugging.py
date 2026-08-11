"""
1. What are your experiences in debugging when the model is not training?
    - I debug it layer by layer instead of changing the multiple things at once.
        - Verify data pipelines:
            - Missing values
            - Incorrect labels
            - Feature scaling
            - train validation split

        - Check class imbalance and label distribution
        - Ensure the loss is decreasing and gradients are not vanishing or exploding

        - Verify the learning rate
            - Too High -> Divergence
            - Too Low -> No learning

        - Check for overfitting vs underfitting using training and validation curves

        - Validate the model architecture
            - Input shape
            - Output layer
            - activation function
            - Loss function
            - Compatibility

        - Monitor Gradient norms and weights parameters are actually changing

        - Review a feature importance or input distribution to identify non-informative- features
        - Compare against a simple baseline model like random forest to determine whether the issues is with the
            data or deep learning model.

        - Start by overfitting a very small dataset. If the model can't memorize the few of the samples there
            is likely a bug in data or model



"""