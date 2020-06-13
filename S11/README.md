## SuperConvergence

1. Write a code that draws zigzag curve

2. Write a code which uses this new ResNet Architecture for Cifar10:
  a. PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
  b. Layer1 -
    - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]
    - R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 
    - Add(X, R1)
  c. Layer 2 -
    - Conv 3x3 [256k]
    - MaxPooling2D
    - BN
    - ReLU
  d. Layer 3 -
    - X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
    - R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
    - Add(X, R2)
  e. MaxPooling with Kernel Size 4
  f. FC Layer 
  g. SoftMax
  
3. Uses One Cycle Policy such that:-
  - Total Epochs = 24
  - Max at Epoch = 5
  - LRMIN = FIND
  - LRMAX = FIND
  - NO Annihilation
  
4. Uses this transform -
  RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)

5. Batch size = 512

6. Target Accuracy: 90%. 

## How to run?

Upload files on colab.research.google.com as per below structure

![](https://github.com/anuragal/deep-learning/blob/master/S10/images/directory.png)

## Results
1. Cyclic Curve

![](https://github.com/anuragal/deep-learning/blob/master/S11/images/cyclic_curve.png)

2. LR Max - 0.015
3. Best Accuracy
   Train - 95.79%
   Test - 90.63%

### Training & Test Accuracy Curve
![](https://github.com/anuragal/deep-learning/blob/master/S11/images/val_traintestaccuracy_change.png)

### GradCAM on for first 5 misclassified images

![](https://github.com/anuragal/deep-learning/blob/master/S11/images/gradcam1.png)

![](https://github.com/anuragal/deep-learning/blob/master/S11/images/gradcam2.png)

![](https://github.com/anuragal/deep-learning/blob/master/S11/images/gradcam3.png)

![](https://github.com/anuragal/deep-learning/blob/master/S11/images/gradcam4.png)

![](https://github.com/anuragal/deep-learning/blob/master/S11/images/gradcam5.png)

