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


Why weighted loss instead of oversampling?

- Oversampling duplicates minority examples, which can cause overfitting.
    Weighted cross-entropy keeps the original data distribution and penalizes mistakes on the minority class more heavily.

When would you still prefer oversampling?

- When the minority class is extremely-small (for example, 0.1%) and the model rarely sees positive examples.
 In NLP, data augmentation (paraphrasing, back translation) is often preferred over simple duplication.

 Why use focal loss?
 - Focal loss focuses training on hard examples by down-weighting easy examples:
    FL(pt)= −(1−pt)^γ *log (pt)

- It is useful when the dataset is highly imbalanced (99:1, 999:1).


How do you pick the prediction threshold?

- Do not always use 0.5. Choose the threshold based on business needs:
    - Fraud detection → prioritize recall.
    - Spam detection → balance precision and recall.
    - Medical diagnosis → minimize false negatives.

    Typically, choose the threshold using the validation set and PR/F1 curves.



"""