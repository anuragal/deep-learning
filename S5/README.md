
# Code Run

###	Objective
-	99.4% validation accuracy
- Less than 15 Epochs
-	Less than 10000 Parameters
- Do this in minumum 5 steps

### Run 1 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anuragal/deep-learning/blob/master/S5/run1.ipynb)

#### Targets:
- Get the basic skeleton right. We will try and avoid changing this skeleton as much as possible. 
- No fancy stuff
#### Results:
- Parameters: 195k
- Best Train Accuracy: 99.35
- Best Test Accuracy: 99.02
#### Analysis:
- The model is still large, but working. 
- We see some over-fitting

### Run 2 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anuragal/deep-learning/blob/master/S5/run2.ipynb)

#### Targets:
- Make the model lighter by changing the number of channels
- Add GAP
#### Results:
- Parameters: 9,664
- Best Train Accuracy: 98.91%
- Best Test Accuracy: 98.81%
#### Analysis:
- Model is slightly over-fitting
- Performance reduction is expected as model capacity is reduced significantly 

### Run 3 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anuragal/deep-learning/blob/master/S5/run3.ipynb)

#### Targets:
- Added Batch-Noramlization to increase model efficiency
#### Results:
- Parameters: 9,816
- Best Train Accuracy: 99.60%
- Best Test Accuracy: 99.21%
#### Analysis:
- Model is still over-fitting
- Not a good model as slight push to Train accuracy might not push Test Accuracy to 99.40%

### Run 4 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anuragal/deep-learning/blob/master/S5/run4.ipynb)

#### Targets:
- Add Regularization, Dropout
#### Results:
- Parameters: 9,816
- Best Train Accuracy: 99.09%
- Best Test Accuracy: 99.34%
#### Analysis:
- After regularization, no overfitting
- Can be pushed further
- Good Model

### Run 5 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/anuragal/deep-learning/blob/master/S5/run5.ipynb)

#### Targets:
- Add LR Scheduler
#### Results:
- Parameters: 9,816
- Best Train Accuracy: 99.05%
- Best Test Accuracy: 99.41% (15th Epoch)
#### Analysis:
- Reducing LR by 10 at 6th epoch increases the accuracy
- Model is good and can be pushed firther
- Reached target accuracy
- No fluctuations in accuracy 
