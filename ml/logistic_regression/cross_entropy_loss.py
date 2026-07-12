"""
Why do we use cross entropy loss not MSE in Logistic Regression?

 L = −(y logp + (1−y)log(1−p))

 where p = σ(wx+b)

  -  MSE works but with sigmoid it causes very small gradients when predictions are highly wrong making learning slow.
  - Cross-entropy avoids this issue and provides stronger gradients.


  - We use cross-entropy because it is derived from maximum likelihood estimation for Bernoulli-distributed targets
  and produces larger, more stable gradients than MSE when combined with sigmoid.
  MSE can suffer from slow convergence due to vanishing gradients.


  Cross-entropy is convex because its second derivative is always non-negative.
  Therefore, logistic regression has a single global minimum, making optimization easier.
"""