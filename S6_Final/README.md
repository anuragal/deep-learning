# Session 6 - Regularization

## Objective

1. Use Session 5 code and run the model for 20 epochs for each

- without L1/L2 with BN
- without L1/L2 with GBN
- with L1 with BN
- with L1 with GBN
- with L2 with BN
- with L2 with GBN
- with L1 and L2 with BN
- with L1 and L2 with GBN

2. Plot the validation loss and accuracy changes for all the models.

3. Plot 25 misclassified images for "without L1/L2 with BN" AND "without L1/L2 with GBN" model

##  Results

### Loss change graph for all 8 jobs

![](https://github.com/anuragal/deep-learning/blob/master/S6_Final/images/loss.png)

### Validation Accuracy change graph for all 8 jobs

![](https://github.com/anuragal/deep-learning/blob/master/S6_Final/images/accuracy.png)

### 25 misclassified images for "without L1/L2 with BN"

![](https://github.com/anuragal/deep-learning/blob/master/S6_Final/images/BN.png)

### 25 misclassified images for "without L1/L2 with GBN"

![](https://github.com/anuragal/deep-learning/blob/master/S6_Final/images/GBN.png)

### L1 and L2's performance in the regularization
In my opinion L1 is giving more accurate results then L2. As seen in Loss Change graph with L2 the loss is more compared to when L2 is not used. Similarly using only L1 gives more accuracy compared to using L2 with L1 or alone.

With L2 the fluctuations in accuracy can also be seen
