### Assignment A
### ResNet-Tiny-ImageNet
1. Use TINY IMAGENET dataset. 
2. Train ResNet18 on this dataset (70/30 split) for 50 Epochs.
3. Target 50%+ Validation Accuracy.

#### Parameters and Hyperparameters
1. Loss Function: Cross Entropy
2. Optimizer: SGD
3. Scheduler: OneCycleLR
4. Batch Size: 256
5. Epochs: 50

#### Image Transformation
1. Pad: h=72, w=72
2. RandomCrop: h=64, w=64, p=1.0
3. Horizontal Flip: p=0.25
4. RGBShift: (20, 20, 20), p=0.25
5. Cutout: holes=1, h=8, w=8, p=0.75

#### Results
Acheived Validation Accuracy: 41%

#### Test & Train Accuracy
<a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_A/images/accuracy.png" height="40%" width="40%" ></a>

#### Validation Loss & Accuracy
<a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_A/images/loss_accuracy.png" height="40%" width="40%" ></a>
