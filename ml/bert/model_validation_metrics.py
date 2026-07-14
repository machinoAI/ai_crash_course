"""
F1 Score: F1 is the harmonic mean of precision and recall:
    = 2PR/P+R
    - F1 score balances precision and recall.

Precision: Out of all transactions predicted as fraud, how many were actually fraud?
Recall: Out of all actual frauds, how many did we catch?

ROC Curve (Receiver Operating Characteristic): ROC plots TPR against FPR and evaluates the ranking ability of a classifier across thresholds.
    - TPR vs FPR

Precision-Recall (PR) Curve: PR curve plots precision against recall and is preferred for highly imbalanced datasets
    because it focuses on minority-class performance.


Why is the harmonic mean used in F1-score instead of the arithmetic mean?
    - Because the harmonic mean penalizes extreme values.

Why does oversampling cause overfitting?
    - Oversampling duplicates minority examples, so the model repeatedly sees the same points and memorizes them instead of learning general patterns.

Why does undersampling lose information?
    - Undersampling removes majority-class examples, potentially discarding important patterns and reducing the model's ability to generalize.




"""