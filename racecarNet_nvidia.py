#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200315 (Dr. Bai): baseline train-test software
#  20200315 (Animesh): formatting, commenting, modified to make compatioble
#                      with any shape of image input
#
# usage: from racecarNet import ServoNet, MotorNet
#
# This script contains required deep learnling models
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import numpy as np

# import torch modules
#
import torch
from torch.nn import Module
from torch.nn import Conv2d, Linear, Dropout
from torch.nn.functional import elu, relu

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
SHAPE = [100,100] # [shape_y,shape_x]

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------

# class: ServoNet
#
# This class contains deep learning model for servo data prediction
#
class ServoNet(Module):
    
    #--------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  shape: input image shape
    #
    # return: none
    #
    def __init__(self, shape):
        super(ServoNet, self).__init__()     
        self.flatsize = int(10*(np.ceil((np.ceil((np.ceil((shape[0]-2)/2)-2)/2)-2)/2)-4)* \
                            (np.ceil((np.ceil((np.ceil((shape[0]-2)/2)-2)/2)-2)/2)-4))
        
        self.conv1 = Conv2d(3, 24, 3, stride=(2, 2))
        self.conv2 = Conv2d(24, 36, 3, stride=(2, 2))
        self.conv3 = Conv2d(36, 48, 3, stride=(2, 2))
        self.conv4 = Conv2d(48, 64, 3)
        self.conv5 = Conv2d(64, 10, 3)
        self.drop = Dropout(p=0.25)
        self.fc1 = Linear(self.flatsize, 100)
        self.fc2 = Linear(100, 50)
        self.fc3 = Linear(50, 10)
        self.fc4 = Linear(10, 1)
        
        return None
    #
    # end of method

    #--------------------------------------------------------------------------
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
        x = elu(self.conv1(x))
        x = elu(self.conv2(x))
        x = elu(self.conv3(x))
        x = elu(self.conv4(x))
        x = self.conv5(x)
        x = self.drop(x)
        x = x.view(-1, self.flatsize)
        x = elu(self.fc1(x))
        x = elu(self.fc2(x))
        x = self.fc3(x)
        x = self.fc4(x)
        
        return x
    #
    # end of method

#------------------------------------------------------------------------------
# class: MotorNet
#
# This class contains deep learning model for motor data prediction
#
class MotorNet(Module):
    
    #--------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  shape: input image shape
    #
    # return: none
    #
    def __init__(self, shape):
        super(MotorNet, self).__init__()     
        self.flatsize = int(10*(np.ceil((np.ceil((shape[0]-2)/2)-2)/2)-6)* \
                            (np.ceil((np.ceil((shape[1]-2)/2)-2)/2)-6))
        
        self.conv1 = Conv2d(3, 24, 3, stride=(2, 2))
        self.conv2 = Conv2d(24, 36, 3, stride=(2, 2))
        self.conv3 = Conv2d(36, 48, 3)
        self.conv4 = Conv2d(48, 64, 3)
        self.conv5 = Conv2d(64, 10, 3)
        self.fc1 = Linear(self.flatsize, 10)
        self.fc2 = Linear(10, 1)
        
        return None
    #
    # end of method

    #--------------------------------------------------------------------------
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
        x = elu(self.conv1(x))
        x = elu(self.conv2(x))
        x = elu(self.conv3(x))
        x = elu(self.conv4(x))
        x = elu(self.conv5(x))
        x = x.view(-1, self.flatsize)
        x = elu(self.fc1(x))
        x = elu(self.fc2(x))
        
        return x
    #
    # end of method