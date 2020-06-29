import numpy as np

import torchvision.transforms as transforms

from albumentations.pytorch.transforms import ToTensor
from albumentations.augmentations.transforms import (
    PadIfNeeded,
    HorizontalFlip,
    VerticalFlip,    
    CenterCrop,    
    Crop,
    Transpose,
    RandomRotate90,
    ElasticTransform,
    GridDistortion, 
    OpticalDistortion,
    RandomSizedCrop,
    CLAHE,
    RandomBrightnessContrast,    
    RandomGamma,
    Normalize,
    Rotate,
    CoarseDropout,
    PadIfNeeded,
    RandomCrop,
    Cutout,
    RGBShift
)

from albumentations import (
    Compose,
    HueSaturationValue
)

def TransformationFactory(t_type ="pytorch"): 
  
    """Factory Method"""
    transformations = { 
        "albumentations": AlbumentationTransformation, 
        "pytorch": PytorchTransformation,
    } 
  
    return transformations[t_type]()

class AlbumentationTransformation(object):
  def __init__(self):
    super(AlbumentationTransformation, self).__init__()

  def load(self, is_train=False):
    # Mean and standard deviation of train dataset
    mean = np.array([0.4914, 0.4822, 0.4465])
    std = np.array([0.2023, 0.1994, 0.2010])
    transforms_list = []

    # Use data aug only for train data
    if is_train:
      transforms_list.extend([
        PadIfNeeded(min_height=80, min_width=80, value=mean*255.0),
        RandomCrop(height=64, width=64, p=1.0),
        HorizontalFlip(p=0.5),
        RGBShift(r_shift_limit=50, g_shift_limit=50, b_shift_limit=50, p=0.5),
        Cutout(num_holes=1, max_h_size=24, max_w_size=24, fill_value=mean*255.0, p=0.5),
        ])
    transforms_list.extend([
      Normalize(
        mean=mean,
        std=std,
        max_pixel_value=255.0,
        p=1.0
      ),
      ToTensor()
    ])
    transforms = Compose(transforms_list, p=1.0)
    return lambda img:transforms(image=np.array(img))["image"]

class PytorchTransformation(object):
  def __init__(self):
    super(PytorchTransformation, self).__init__()

  def load(self, is_train=False):
    # Mean and standard deviation of train dataset
    mean = (0.4914, 0.4822, 0.4465)
    std = (0.2023, 0.1994, 0.2010)
    transforms_list = []

    # Use data aug only for train data
    if is_train:
      transforms_list.extend([
        transforms.RandomHorizontalFlip()
        ])

    transforms_list.extend([
      transforms.ToTensor(),
      transforms.Normalize(mean, std)
    ])

    return transforms.Compose(transforms_list)
