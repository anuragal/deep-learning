from os import path

import torch
import torchvision

from deep_learning.S12.transformation import TransformationFactory

class ImageData(object):

    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog',
		    'frog', 'horse', 'ship', 'truck')

    def __init__(self):
        super(ImageData, self).__init__()
        self.trainloader = None
        self.testloader = None
        self.cuda = None

    def load(self, transformation_type="pytorch"):
        # Choose from "albumentations" or "pytorch". Default is "pytorch"
        t = TransformationFactory(transformation_type)
        train_transform = t.load(is_train=True)
        test_transform = t.load(is_train=False)

        SEED = 1

        # CUDA?
        self.cuda = False # torch.cuda.is_available()
        print("CUDA Available?", self.cuda)

        # For reproducibility
        torch.manual_seed(SEED)

        if self.cuda:
            torch.cuda.manual_seed(SEED)

        return train_transform, test_transform

    def load_CIFAR(self, transformation_type="pytorch"):
        train_transform, test_transform = self.load(transformation_type)

        # dataloader arguments - something you'll fetch these from cmdprmt
        dataloader_args = dict(shuffle=True, batch_size=128, num_workers=4, pin_memory=True) if self.cuda else dict(shuffle=True, batch_size=64)

        trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=train_transform)

        testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                            download=True, transform=test_transform)

        self.trainloader = torch.utils.data.DataLoader(trainset, batch_size=512, shuffle=True, num_workers=4)
        self.testloader = torch.utils.data.DataLoader(testset, batch_size=512, shuffle=False, num_workers=4)

    def load_TINY_IMAGENET(self, image_path, transformation_type="pytorch"):
        train_transform, test_transform = self.load(transformation_type)

        training_images = path.join(image_path, "train/")
        test_images = path.join(image_path, "val/")

        trainset = torchvision.datasets.ImageFolder(
                              root = training_images,
                              transform = train_transform
                       )

        testset = torchvision.datasets.ImageFolder(
                              root = test_images,
                              transform = test_transform
                       )

        #print(self.get_class_distribution(trainset))
        #print(self.get_class_distribution(testset))

        self.trainloader = torch.utils.data.DataLoader(trainset, batch_size=512, shuffle=True, num_workers=4)
        self.testloader = torch.utils.data.DataLoader(testset, batch_size=512, shuffle=False, num_workers=4)

    def get_class_distribution(self, dataset_obj):
        idx2class = {v: k for k, v in dataset_obj.class_to_idx.items()}
        count_dict = {k:0 for k,v in dataset_obj.class_to_idx.items()}

        for element in dataset_obj:
            y_lbl = element[1]
            y_lbl = idx2class[y_lbl]
            count_dict[y_lbl] += 1

        return count_dict