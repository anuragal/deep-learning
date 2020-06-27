from deep_learning.models.resnetbase import BasicBlock, ResNet

def ResNet101():
    return ResNet(Bottleneck, [3, 4, 23, 3])
