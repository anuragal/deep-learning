from resnetbase import BasicBlock

def ResNet18():
    return ResNet(BasicBlock, [2, 2, 2, 2])
