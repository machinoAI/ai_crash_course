"""
Mean Squared Error:
    - A function is differential at a point if you can draw exactly one tangent line there.
    -  The derivative tell us:
        - If you move a little bit how much does the function change ?
    - For a single point:
        L = (y-y^)^2 lets say e = (y-y^)
        L = e^2
        dL/de = 2e

        for every e value you have derivative even e = 0 derivative is exactly 0.

        - HENCE,  MSE is differentiable.

Mean Absolute Error:
    For a single point MAE:
        L = (y-y^)     say e = (y-y^)
        L = |e|

        for positive errors:
            dL/de = 1     right derivative

        for negative errors: dL/de = -1  left derivative

        dL/de = { 1 when e>0 or -1  when e<0

    - The left and right derivatives are different
    - Hence MAE is not differentiable at e = 0


Why does differentiable feature matter ?
    - Gradient descent updates weight using:
        W new = W old - eta*dL/dW
    - To update the weights, the algorithm needs dL/dW
    - For MSE gradient exist everywhere
    - For MAE gradient is undefined at e = 0
    -

    - MSE optimization is easier
    - MAE optimization is trickier
    - MSE is even have closed-forum solution (normal distribution)

- Now the question is,
    - If MAE is not differentiable, then how do people train model with MAE ?
    - Answer is sub-gradients
    - at e = 0 it accepts any value between [-1,1]








"""