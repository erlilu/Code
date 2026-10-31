import numpy as np
import matplotlib.pyplot as plt

from common.gradient import numerical_gradient

# define gradient descent function
def gradient_descent(f, init_x, lr = 0.01, num_iter = 100):
    x = init_x
    x_history = []
    for i in range(num_iter):
        x_history.append(x.copy())
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, np.array(x_history)


# define a function
def f(x):
    return x[0] ** 2 + x[1] ** 2

if __name__ == '__main__':
    init_x = np.array([-3.0, 4.0])
    lr = 0.1
    num_iter = 20
    x, x_history = gradient_descent(f, init_x, lr, num_iter)
    print('the minest point is :', x)

    plt.plot([-3.0, 1.0], [0, 0], '--r')
    plt.plot([0, 0], [-1.0, 4.0], '--r')
    plt.scatter(x_history[:, 0], x_history[:, 1])
    plt.xlim([-3.0, 1.0])
    plt.ylim([-1.0, 4.0])
    plt.show()
