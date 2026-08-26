import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(sigmoid_output):
    return sigmoid_output * (1 - sigmoid_output)


def tanh_derivative(tanh_output):
    return 1 - tanh_output ** 2


class LSTMCell:

    def __init__(self, input_size, hidden_size):

        self.input_size = input_size
        self.hidden_size = hidden_size

        # ------------------------------------------------
        # One weight matrix for all 4 gates
        #
        # [forget, input, candidate, output]
        # ------------------------------------------------

        self.W = np.random.randn(
            4 * hidden_size,
            input_size + hidden_size
        ) * 0.01

        self.b = np.zeros((4 * hidden_size, 1))

    # ====================================================
    # FORWARD PASS
    # ====================================================

    def forward(self, x_t, h_prev, c_prev):

        # -----------------------------------------------
        # Combine previous hidden state and current input
        # -----------------------------------------------

        combined = np.vstack((h_prev, x_t))

        # -----------------------------------------------
        # Linear transformation
        # -----------------------------------------------

        gates = self.W @ combined + self.b

        # -----------------------------------------------
        # Split into 4 gates
        # -----------------------------------------------

        H = self.hidden_size

        f = sigmoid(gates[0:H])          # Forget gate
        i = sigmoid(gates[H:2*H])        # Input gate
        g = np.tanh(gates[2*H:3*H])      # Candidate
        o = sigmoid(gates[3*H:4*H])      # Output gate

        # -----------------------------------------------
        # Cell state
        # -----------------------------------------------

        c_t = f * c_prev + i * g

        # -----------------------------------------------
        # Hidden state
        # -----------------------------------------------

        h_t = o * np.tanh(c_t)

        # -----------------------------------------------
        # Cache values for backward pass
        # -----------------------------------------------

        cache = (
            x_t,
            h_prev,
            c_prev,
            combined,
            f,
            i,
            g,
            o,
            c_t
        )

        return h_t, c_t, cache

    # ====================================================
    # BACKWARD PASS
    # ====================================================

    def backward(self, dh_next, dc_next, cache):

        (
            x_t,
            h_prev,
            c_prev,
            combined,
            f,
            i,
            g,
            o,
            c_t
        ) = cache

        # -----------------------------------------------
        # Gradient through:
        #
        # h_t = o * tanh(c_t)
        # -----------------------------------------------

        tanh_c = np.tanh(c_t)

        do = dh_next * tanh_c

        dc = (
            dh_next
            * o
            * tanh_derivative(tanh_c)
            + dc_next
        )

        # -----------------------------------------------
        # c_t = f*c_prev + i*g
        # -----------------------------------------------

        df = dc * c_prev
        di = dc * g
        dg = dc * i
        dc_prev = dc * f

        # -----------------------------------------------
        # Backprop through activation functions
        # -----------------------------------------------

        d_f_pre = df * sigmoid_derivative(f)
        d_i_pre = di * sigmoid_derivative(i)
        d_g_pre = dg * tanh_derivative(g)
        d_o_pre = do * sigmoid_derivative(o)

        # -----------------------------------------------
        # Combine gate gradients
        # -----------------------------------------------

        d_gates = np.vstack((
            d_f_pre,
            d_i_pre,
            d_g_pre,
            d_o_pre
        ))

        # -----------------------------------------------
        # W @ combined
        # -----------------------------------------------

        dW = d_gates @ combined.T

        db = d_gates

        # -----------------------------------------------
        # Gradient w.r.t. combined
        # -----------------------------------------------

        dcombined = self.W.T @ d_gates

        # -----------------------------------------------
        # Split combined gradient
        #
        # combined = [h_prev]
        #            [x_t]
        # -----------------------------------------------

        H = self.hidden_size

        dh_prev = dcombined[:H]
        dx_t = dcombined[H:]

        return dx_t, dh_prev, dc_prev, dW, db




# Example dimensions

input_size = 3
hidden_size = 4

lstm = LSTMCell(
    input_size=input_size,
    hidden_size=hidden_size
)

# Current input x_t
x_t = np.random.randn(input_size, 1)

# Previous hidden state
h_prev = np.zeros((hidden_size, 1))

# Previous cell state
c_prev = np.zeros((hidden_size, 1))


# -----------------------------
# Forward
# -----------------------------

h_t, c_t, cache = lstm.forward(
    x_t,
    h_prev,
    c_prev
)

print("h_t shape:", h_t.shape)
print("c_t shape:", c_t.shape)


# -----------------------------
# Backward
# -----------------------------

dh_next = np.random.randn(hidden_size, 1)
dc_next = np.random.randn(hidden_size, 1)

dx, dh_prev, dc_prev, dW, db = lstm.backward(
    dh_next,
    dc_next,
    cache
)

print("dx shape:", dx.shape)
print("dh_prev shape:", dh_prev.shape)
print("dc_prev shape:", dc_prev.shape)
print("dW shape:", dW.shape)
print("db shape:", db.shape)