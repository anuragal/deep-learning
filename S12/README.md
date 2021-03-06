##   Object Localization - YOLO

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

### Assignment B
### Best K clusters for 50 Dog dataset
1. Downloaded [50 images of dogs](https://github.com/anuragal/deep-learning/tree/master/S12/Assignment_B/dog_images)
2. Annotate bounding boxes around the dogs using [VGG annotator](http://www.robots.ox.ac.uk/~vgg/software/via/)
3. Describe the contents of this Annotated JSON file in FULL details 
4. Find out the best total numbers of clusters

#### Results
1. JSON File contents explained

```json
{
    "dog1.jfif3560": {
        "filename": "dog1.jfif",      # FIle Name
        "size": 3560,                 # File Size
        "regions": [{                 # Annotated Region
            "shape_attributes": {     
                "name": "rect",       # Shape Type
                "x": 67,              # Starting X-axis for region
                "y": 6,               # Starting y-axis for region
                "width": 98,          # Width of the region
                "height": 197         # Height of the region
            },
            "region_attributes": {    # Custom Attributes Defined for image
                "Class": "Dog"        # Class
            }
        }],
        "file_attributes": {}
}
```

2. Sample Annotated images

![](https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/annotated_5dog_image.png)

3. Scatter chart

<a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/scatter_log.png" height="40%" width="40%" ></a>


4. Find out Best count of Cluster using Elbow method

<a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/Elbow.png" height="40%" width="40%" ></a>

Looking at the figure above 6 clusters are ideal

5. Plot K means Clusters

| S.No.  | Number of Clusters | Plot | Recommendation |
| ------------- | ------------- | ------------- | ------------- |
| 1  | 2 | <a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/2-clusters.png" height="60%" width="60%" ></a> | |
| 1  | 3 | <a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/3-clusters.png" height="60%" width="60%" ></a> | |
| 1  | 4 | <a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/4-clusters.png" height="60%" width="60%" ></a> | |
| 1  | 6 | <a href="url"><img src="https://github.com/anuragal/deep-learning/blob/master/S12/Assignment_B/files/6-clusters.png" height="60%" width="60%" ></a> | Yes, the distance between various point is minimal |
