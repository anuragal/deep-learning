from deep_learning.models.resnetbase import BasicBlock, ResNet

def ResNet50():
    return ResNet(Bottleneck, [3, 4, 6, 3])
