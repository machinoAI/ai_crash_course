"""
How do you design BERT training for imbalance datasets?
-   Lets say class ration is 99:1
- Data level: We can use oversampling , undersampling, or data augmentation to increase the minor class or decrease the major class.
- Loss : Focal loss or weighted cross entropy
- Evaluation metrics:
    - Precision
    - Recall
    - PR- curve
    - F1 -score
- ROC-AUC curve is not effective in imbalance dataset.

- Threshold tuning: Don't blindly use the default threshold of 0.5. Choose the threshold based on business requirements (e.g., high recall for fraud detection).

"""