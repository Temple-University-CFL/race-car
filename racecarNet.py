#!/usr/bin/env python
#
#==============================================================================
# Initialization
#==============================================================================
# revision history
#  20200315 (Dr. Bai): baseline train-test model
#  20200315 (Animesh): formatting, commenting, modified to make compatioble
#                      with any shape of image input
#  20200417 (Animesh): implement drop-out layer
#  20200520 (Dr. Bai): implement simpler flat-size calculator
#  20200520 (Animesh): implement more simpler flat-size calculator
#
# usage: from racecarNet import ServoNet, MotorNet
#
# This script contains required deep learnling models
#
#==============================================================================
# Import Modules
#==============================================================================
#
# import global modules
#
import numpy as np

# import torch modules
#
import torch
from torch import nn

#==============================================================================
# Global Variables
#==============================================================================
SHAPE = [100,100] # [shape_y,shape_x]

#==============================================================================
# Classes
#==============================================================================

# class: ServoNet
#
# This class contains deep learning model for servo data prediction
#
class ServoNet(nn.Module):
    
    #==========================================================================
    #
    # arguments:
    #  shape: input image shape
    #
    # return: none
    #
    def __init__(self, shape):
        super(ServoNet, self).__init__()

        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=(10,10), padding=(2,2)),
            nn.ReLU(inplace=True),
            nn.AdaptiveMaxPool2d(output_size=(10,10)),
            nn.Conv2d(64, 10, 3),
            nn.Dropout(0.25),
        )

        self.flatsize = np.prod(self.features(torch.ones(1, 3, *shape)).size())

        self.classifier = nn.Sequential(
            nn.Linear(self.flatsize, 10),
            nn.Linear(10, 1),
        )

        return None
    #
    # end of method

    #==========================================================================
    # method: forward
    #
    # arguments:
    #  x: image tensor
    #
    # return:
    #  x: output tensor
    #
    # This method passes tensors through neural network model
    #
    def forward(self, x):
        
        x = self.features(x)
        x = x.view(-1, self.flatsize)
        x = self.classifier(x)
        
        return x
    #
    # end of method

#==============================================================================
# class: MotorNet
#
# This class contains deep learning model for motor data prediction
#
class MotorNet(nn.Module):

    #==========================================================================
    # method: constructor
    #
    # arguments:
    #  shape: input image shape
    #
    # return: none
    #
    def __init__(self, shape):
        super(MotorNet, self).__init__()     

        self.features = nn.Sequential(
            nn.Conv2d(3, 24, 3, stride=(2, 2)),
            nn.ELU(),
            nn.Conv2d(24, 36, 3, stride=(2, 2)),
            nn.ELU(),
            nn.Conv2d(36, 48, 3),
            nn.ELU(),
            nn.Conv2d(48, 64, 3),
            nn.ELU(),
            nn.Conv2d(64, 10, 3),
            nn.ELU(),
            nn.Dropout(0.25),
        )

        self.flatsize = np.prod(self.features(torch.ones(1, 3, *shape)).size())

        self.classifier = nn.Sequential(
            nn.Linear(self.flatsize, 10),
            nn.ELU(),
            nn.Linear(10, 1),
            nn.ELU(),
        )

        return None
    #
    # end of method

    #==========================================================================
    # method: forward
    #
    # arguments:
    #  x: image tensor
    #
    # return:
    #  x: output tensor
    #
    # This method passes tensors through neural network model
    #
    def forward(self, x):
        
        x = self.features(x)
        x = x.view(-1, self.flatsize)
        x = self.classifier(x)
        
        return x
    #
    # end of method

#==============================================================================