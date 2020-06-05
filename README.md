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
```python
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
```python
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

### models
1. Resnet18
2. Resnet34
3. Resnet50
4. Resnet101
5. Resnet152

#### Usage
```python
    from models.resnet18 import ResNet18

	use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    model = ResNet18().to(device)
```

### gradcam.py
Gradient-weighted Class Activation Mapping (Grad-CAM)

#### Usage
```python
    from gradcam import VisualizeCam

    viz_cam = VisualizeCam(self.model, self.img_data.classes, target_layers)
```
### transformation.py
Defining data transformations. For e.g. how data can be augmented to correct represent images which it might not see otherwise

#### Usage
```python
    from transformation import TransformationFactory

    # Choose from "albumentations" or "pytorch". Default is "pytorch"
    t = TransformationFactory(transformation_type)
```
