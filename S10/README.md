## Learning Rates

1. Add CutOut from transformations (albumentations)
2. Implement LR Finder (for SGD, not for ADAM) from https://github.com/davidtvs/pytorch-lr-finder
3. Implement ReduceLROnPlatea - https://pytorch.org/docs/stable/optim.html#torch.optim.lr_scheduler.ReduceLROnPlateau
4. Find best LR to train your model
5. Use SDG with Momentum
6. Train for 50 Epochs. 
7. Show Training and Test Accuracy curves
8. Target 88% Accuracy.
9. Run GradCAM on the any 25 misclassified images. Make sure to mention what is the prediction and what was the ground truth label.

## How to run?

Upload files on colab.research.google.com as per below structure
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/directory.png)

## Results
1. Transfomration
    Added `albumentations.augmentations.transforms.CoarseDropout` in place of `CutOut`
2. LR Finder
    Implemented `https://github.com/anuragal/deep-learning/blob/master/lrfinder.py` class
3. ReduceLROnPlatea
    Used ReduceLROnPlatea for as LR schedular with factor=0.1
4. Best LR - 
5. Best Accuracy
   Train
   Test

### Training & Test Accuracy Curve
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/loss.png)

### GradCAM on for 25 misclassified images
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam2.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam3.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam4.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam5.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam2.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam3.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam4.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam5.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam2.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam3.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam4.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam5.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam2.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam3.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam4.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam5.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam2.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam3.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam4.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam5.png)
