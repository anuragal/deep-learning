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
# Loading data and transforming it
img_data = ImageData()

# Choose from "albumentations" or "pytorch". Default is "pytorch"
img_data.load("albumentations")
```

### datamodel.py
### gradcam.py
### transformation.py
### models