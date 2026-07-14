"""
Why PR-AUC instead of ROC -AUC ?

- PR- AUC: Precision - Recall Area under curve
    - In highly imbalanced datasets ROC can artificially look good because it is dominated by the majority class.
    - Receiver Operating Characteristics is the ratio between
        TPR and FPR.
        TPR = TP/TP+FN =  Precision
        FPR = FP/FP+TN

    - The ROC curve may still look decent because FPR is normalized by the huge number of negatives.
    - PR-AUC focuses on precision and recall for the minority class, making it a better metric.


"""