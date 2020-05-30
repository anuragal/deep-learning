## Albumentations & GradCam + Quiz

1. Apply tranformations using library Albumentations. Apply ToTensor, HorizontalFlip, Normalize (at min) + More (for additional points)
2. Please make sure that your test_transforms are simple and only using ToTensor and Normalize
3. Implement GradCam function as a module. 
4. Your final code (notebook file) must use imported functions to implement transformations and GradCam functionality
5. Target Accuracy is 87%

## Transformations Used

### Train
1. HorizontalFlip
2. Rotate
3. CoarseDropout

### Train + Test
4. Normalize
5. ToTensor

## Results

1. Accuracy is 88.19% at Epoch 30
2. Number of Epochs 30

## How to run?

Upload files on colab.research.google.com as per below structure

![](https://github.com/anuragal/deep-learning/blob/master/S9/images/directory.png)

### Model

1. Model looks good
2. Training Accuracy 89.98%
3. Test Accuracy 88.19%

### Loss change graph

![](https://github.com/anuragal/deep-learning/blob/master/S9/images/loss.png)

### Validation Accuracy change graph

![](https://github.com/anuragal/deep-learning/blob/master/S9/images/accuracy.png)

### 25 misclassified images

![](https://github.com/anuragal/deep-learning/blob/master/S9/images/misclassified.png)

## GRADCam 

![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam2.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam3.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam4.png)
![](https://github.com/anuragal/deep-learning/blob/master/S9/images/gradcam5.png)


## Quiz Results

1. Model looks good
2. Training Accuracy 79.58%
3. Test Accuracy 81.65%%
4. Number of Epochs - 10
5. Notebook file link - https://github.com/anuragal/deep-learning/blob/master/S9/QuizDNN.ipynb
