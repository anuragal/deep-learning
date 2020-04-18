## Using given colab file

1. Achieve 99.4% validation accuracy
2. Use less than 20k Parameters
3. Use less than 20 Epochs
4. Don't use fully connected layer
5. To learn how to add different things we covered in this session, you can refer to this [code](https://www.kaggle.com/enwei26/mnist-digits-pytorch-cnn-99 (Links to an external site.))

## Parameters used


    ------------------------------------------------------------
        Layer (type)               Output Shape         Param #
    ============================================================
            Conv2d-1           [-1, 16, 28, 28]             160
              ReLU-2           [-1, 16, 28, 28]               0
       BatchNorm2d-3           [-1, 16, 28, 28]              32
           Dropout-4           [-1, 16, 28, 28]               0
            Conv2d-5           [-1, 16, 28, 28]           2,320
              ReLU-6           [-1, 16, 28, 28]               0
       BatchNorm2d-7           [-1, 16, 28, 28]              32
           Dropout-8           [-1, 16, 28, 28]               0
            Conv2d-9           [-1, 16, 28, 28]           2,320
             ReLU-10           [-1, 16, 28, 28]               0
      BatchNorm2d-11           [-1, 16, 28, 28]              32
          Dropout-12           [-1, 16, 28, 28]               0
        MaxPool2d-13           [-1, 16, 14, 14]               0
           Conv2d-14           [-1, 16, 14, 14]           2,320
             ReLU-15           [-1, 16, 14, 14]               0
      BatchNorm2d-16           [-1, 16, 14, 14]              32
          Dropout-17           [-1, 16, 14, 14]               0
           Conv2d-18           [-1, 16, 14, 14]           2,320
             ReLU-19           [-1, 16, 14, 14]               0
      BatchNorm2d-20           [-1, 16, 14, 14]              32
          Dropout-21           [-1, 16, 14, 14]               0
        AvgPool2d-22             [-1, 16, 7, 7]               0
           Conv2d-23             [-1, 16, 5, 5]           2,320
             ReLU-24             [-1, 16, 5, 5]               0
          Dropout-25             [-1, 16, 5, 5]               0
           Conv2d-26             [-1, 32, 3, 3]           4,640
             ReLU-27             [-1, 32, 3, 3]               0
          Dropout-28             [-1, 32, 3, 3]               0
           Conv2d-29             [-1, 10, 1, 1]           2,890
             ReLU-30             [-1, 10, 1, 1]               0
    ============================================================

    Total params: 19,450
    Trainable params: 19,450
    Non-trainable params: 0

## Accuracy

    Acheived 99.4% accuracy at last epoch

    loss=0.007401198148727417 batch_id=468: 100%|██████████| 469/469 [00:10<00:00, 43.87it/s]
    Test set: Average loss: 0.0182, Accuracy: 9940/10000 (99.40%)
    
