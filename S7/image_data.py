import torch
import torchvision
import torchvision.transforms as transforms

from config import ModelConfig as args
from utils import has_cuda

class ImageData(object):

	self.classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog',
			'frog', 'horse', 'ship', 'truck')

	def __init__(self, args):
		super(ImageData, self).__init__()
		self.load()

	def load(self):
    transform = transforms.Compose(
		    [transforms.RandomHorizontalFlip(),
		     transforms.ToTensor(),
		     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
     
    SEED = 1

    # CUDA?
    cuda = torch.cuda.is_available()
    print("CUDA Available?", cuda)

    # For reproducibility
    torch.manual_seed(SEED)

    if cuda:
        torch.cuda.manual_seed(SEED)

    # dataloader arguments - something you'll fetch these from cmdprmt
    dataloader_args = dict(shuffle=True, batch_size=128, num_workers=4, pin_memory=True) if cuda else dict(shuffle=True, batch_size=64)

    trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                            download=True, transform=transform)

    testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                           download=True, transform=transform)

   	self.trainloader = torch.utils.data.DataLoader(trainset, **dataloader_args)
		self.testloader = torch.utils.data.DataLoader(testset, **dataloader_args)
