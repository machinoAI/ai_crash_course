"""
Assumptions of Linear Regression:
    - Linearity -  Most important
        y=wX+b+ϵ

    - Independence : Observations should be independent of each other.
    - Homoscedasticity : Residuals should have constant variance:
        Var(ϵ)=σ2

    - No multi-collinearity: Features should not be highly correlated.

    - Normality of residuals:
        ϵ∼N(0,σ2)

"""


"""
     - Why  multi-collinearity is harmful?
     
        - Coefficients become unstable.
        - Small changes in data can drastically change coefficients.
        - Hard to interpret feature importance.
        - Model predictions may still be good, but explanations become unreliable.
        
    - How to check for multi-collinearity ?
        - ∣Corr(Xi,Xj∣>0.8  # there may be multicollinearity
        - df.corr(numeric_only= true)
        
        - VIF (Variance Inflation Factor)
            VIFi=1/ (1- Ri^2)

        - from statsmodels.stats.outliers_influence import variance_inflation_factor

        where:
            VIF<5: OK
            5<VIF<10: Moderate
            VIF>10: High multicollinearity

"""


"""
    What is heteroscedasticity?

    - Heteroscedasticity means that the variance of the residuals is not constant.
    - Linear Regression assumes that residuals should have constant variance.
    
    - What problems does it create?
        - Unreliable standard errors.
        - Incorrect p-values.
        - Confidence intervals become misleading.
        - Hypothesis testing becomes unreliable.



"""