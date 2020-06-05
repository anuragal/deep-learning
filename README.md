# Deep Learning

## Learning resource
https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC

## Code Walkthrough

### dataloader.py
1. Download data
2. Perform transformations on data
	importing `transformation.py`
3. Loads inside pytorch dataloader
	Creates `self.trainloader` & `self.testloader`

#### Usage
```
from dataloader import ImageData

# Loading data and transforming it
img_data = ImageData()

# Choose from "albumentations" or "pytorch". Default is "pytorch"
img_data.load("albumentations")
```

### datamodel.py
1. Model Train and Test
2. Plot graphs
	a. Accuracy
	b. Loss
	c. Misclassified images
	d. GRADCam

#### Usage
```
from datamodel import DataModel

# training the dataset and then running test
dm = DataModel(img_data, num_of_epochs = 10, cal_misclassified = True)
dm.run_model(QuizDNN(), device)

# Plotting Validation Accuracy
dm.plot_accuracy_graph()

# Plotting Loss Graph
dm.plot_loss_graph()

# Plotting Misclassified Images
dm.plot_misclassified()

# Plotting GRADCam for Misclassified Images
dm.plot_GRADcam(["x3_block","x5_block","x7_block","x11_block"])
```

### gradcam.py
### transformation.py
### models