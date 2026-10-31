import numpy as np

from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

# define a simple network class
class SimpleNet:
    def __init__(self):
        self.W = np.random.randn(2, 3)

    def forward(self, X):
        a = X @ self.W
        y = softmax(a)
        return y

    def loss(self, x, t):
        y = self.forward(x)
        return cross_entropy_error(y, t)

# mian procession
if __name__ == "__main__":
    # 1. create a date
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])

    # 2. define network model
    net = SimpleNet()

    # 3. calculate grad
    f = lambda w: net.loss(x, t)
    gradw = numerical_gradient(f, net.W)

    print(gradw)

