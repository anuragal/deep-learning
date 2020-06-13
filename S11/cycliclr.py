import math

import matplotlib.pyplot as plt

def get_cyclic_lr(iterations, stepsize, lr_source, lr_dest):
    lr_values = []
    iterations_values = []

    cycle = math.floor(1 + iterations/(2 * stepsize))
    x = math.fabs(iterations/stepsize - 2 * cycle + 1)

    lrt = lr_source + (lr_dest - lr_source) * (1 - x)

    loop_counter = 0
    for j in range(3):
        lr = lr_source
        while True:
            loop_counter = loop_counter + 1
            lr = lr + lrt
            lr_values.append(lr)
            iterations_values.append(stepsize * loop_counter)
            if lr >= lr_dest:
                break

        lr = lr_dest
        while True:
            loop_counter = loop_counter + 1
            lr = lr - lrt
            lr_values.append(lr)
            iterations_values.append(stepsize * loop_counter)
            if lr <= lr_source:
                break

    return lr_values, iterations_values

def plot_cyclic_curve(iterations, stepsize, lr_source, lr_dest):
    fig = plt.figure(figsize = (40,5))
    lr_list, iteration_list = get_cyclic_lr(iterations, stepsize, lr_source, lr_dest)

    plt.subplot(133)
    plt.plot(iteration_list, lr_list)
