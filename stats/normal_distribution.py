"""
Normal distribution aka Gaussian Distribution:
 It is a probability distribution in which most observations cluster around the mean and
 frequency decreases symmetrically once you move away from the mean.

 It has the familiar bell-shaped curve.

 Mean: The center of the distribution.
 standard deviation(σ): Measures how spread out the data are.
    - A small σ means the data are tightly clustered around the mean.
    - A large σ means the data are more spread out.

 ** The 68–95–99.7 Rule (Very Important)
    - 68% within 1 standard deviation
    - 95% within 2nd standard deviation
    - 99.7% within 3rd standard deviation

Normal distribution: X∼N(μ,σ^2)
where:
    μ = Mean
    σ = Standard Deviation

    standardization(Z) = (X- mean)/ Standard Deviation #
    Example: A z-score tells us how many standard deviations a data point is away from the mean.
            Mean = 170 cm
            SD = 5 cm

            Height = 180 cm

            Z = (180-170)/5 = 2

Central Limit Theorem (CLT):
    Regardless of the population's distribution, the distribution of the sample mean approaches a
    normal distribution as the sample size becomes sufficiently large,
    provided the samples are independent and identically distributed with finite variance.

Example:
    - Suppose all house prices in a city are highly skewed.
    -   ₹30L
        ₹35L
        ₹40L
        ₹45L
        ₹10 Cr
        ₹25 Cr
        ₹80 Cr

    - This distribution is clearly not normal because a few very expensive houses create a long right tail.
    - Randomly select 100 houses.
    - Compute their average price.
    - Repeat this 10,000 times.

- You now have 10,000 sample means.
- Those sample means will be approximately normally distributed, even though the
    original house prices are not. This is called CLT.


    Standard Error of the Mean: Mean/ Sqrt(n)

    where:
    σ = Population standard deviation
    n = Sample size


 - How do you check whether your data are normally distributed?
 Ans: I would use a statistical test such as the Shapiro–Wilk test and also inspect a histogram and a Q-Q plot.
  The statistical test provides evidence against normality, while the plots help identify skewness,
  heavy tails, or outliers that may not be obvious from the p-value alone.

"""
# Normal distribution:
from scipy.stats import norm

# P(X <= 180)
prob = norm.cdf(180, loc=170, scale=5)

print("Normal distribution:",prob)

# Z- Score:
x = 180
mean = 170
std = 5

z = (x - mean) / std

print("Z- Score:",z)

# Standard Error:
import numpy as np

sigma = 15
n = 100

se = sigma / np.sqrt(n)

print("Standard Error:", se)

# Check whether data is normally distributed:

from scipy.stats import shapiro

data = [50, 60, 75, 90, 100, 110, 125, 140]

stat, p = shapiro(data)

print("Stats:", stat)
print("p-value:", p)

"""
he hypotheses for the Shapiro–Wilk test are:

H₀ (Null Hypothesis): The data are normally distributed.
H₁ (Alternative Hypothesis): The data are not normally distributed.

Decision rule:

p-value > 0.05 → Fail to reject H₀.
p-value ≤ 0.05 → Reject H₀.
"""

