#!/usr/bin/env python
#
#==============================================================================
# Initialization
#==============================================================================
# revision history
#  20200315 (Animesh): baseline software
#
# usage: from rc_nn_utility import Datagen, ParseData etc
#
# This script contains utility classes.
#  Datagen: line 38
#  ParseData: line 128
#
#==============================================================================
# Import Modules
#==============================================================================
#
# import global modules
#
import cv2

# import torch modules
#
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms

#==============================================================================
# Global Variables
#==============================================================================
SHAPE = [100,100]

#==============================================================================
# Classes
#==============================================================================

# class: Datagen
#
# This class generates data for neural network training session
#
class Datagen(Dataset):

    #==========================================================================
    # method: constructor
    #
    # arguments:
    #  ilist: image file name list
    #  isgape: image shape [width, height]
    #
    # return: none
    #
    def __init__(self, ilist=None, shape=SHAPE):
        
        self.transform = transforms.Compose([transforms.ToTensor()])
        
        self.ilist = ilist
        self.shape = shape
        
        self.parsedata = ParseData()

        return None
    #
    # end of method
    
    #==========================================================================
    # method: get_image
    #
    # arguments:
    #  ifile: input image file
    #
    # return:
    #  image: image tensor
    #
    # This method returns image tensor
    #
    def get_image(self, ifile):
        
        image = self.parsedata.parse_image(ifile)
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        image = self.transform(image)
        return image.unsqueeze(0)
    #
    # end of method

    #==========================================================================
    # method: getitem
    #
    # arguments: 
    #  index: index for list of images
    #
    # return: image, servo, motor
    #
    # This method returns data
    #
    def __getitem__(self, index):
        
        # parse image, servo and motor data
        image,servo,motor = self.parsedata.parse_data(self.ilist[index])
        
        # convert image, servo and motor data to tensor
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        image = self.transform(image)
        servo = torch.tensor(float(servo))
        motor = torch.tensor(float(motor))
        
        return image, servo, motor
    #
    # end of method

    #==========================================================================
    # method: length
    #
    # arguments: none
    #
    # return: none
    #
    # This method returns length of data
    #
    def __len__(self):
        
        return len(self.ilist)
    #
    # end of method


#==============================================================================
# class: ParseData
#
# This class parses datas
#
class ParseData:

    #==========================================================================
    # method: constructor
    #
    # arguments: none
    #
    # return: none
    #
    def __init__(self):

        return None
    #
    # end of method

    #==========================================================================
    # method: parse_data
    #
    # arguments:
    #  fname: file name
    #
    # return: image data, servo data, motor data
    #
    # This method parses image, servo and motor data from given image file
    #
    def parse_data(self, fname):
        
        return self.parse_image(fname), \
                    self.parse_servo(fname), self.parse_motor(fname)
    #
    # end of method
    
    #==========================================================================
    # method: parse_image
    #
    # arguments:
    #  fname: file name
    #
    # return: image data
    #
    # This method parses image data from given image file
    #
    def parse_image(self, fname):

        return cv2.imread(fname)
    #
    # end of method
    
    #==========================================================================
    # method: parse_servo
    #
    # arguments:
    #  fname: file name
    #
    # return: servo data
    #
    # This method parses servo data from given image file
    #
    def parse_servo(self, fname):
        
        return int(fname.split('/')[-1].split('.')[0].split('_')[-2][1:3])
    #
    # end of method
    
    #==========================================================================
    # method: parse_motor
    #
    # arguments:
    #  fname: file name
    #
    # return: motor data
    #
    # This method parses motor data from given image file
    #
    def parse_motor(self, fname):
        
        return int(fname.split('/')[-1].split('.')[0].split('_')[-1][1:3])
    #
    # end of method

#==============================================================================







#==============================================================================
# Debugging Block ANI717
#==============================================================================
#from torch.utils.data import DataLoader
#
#file = 'data/list/list_1.csv'
#
#dataloader = DataLoader(dataset=Datagen(file,shape=[10,8]), batch_size=1000, \
#                        shuffle=True)
#for image, servo, motor in dataloader:
#    print(image.shape)
#    print(servo, motor)

#==============================================================================
#a = CarUtility()
#img,servo,motor = a.parse_data('data/images/output_0002/i0000009_s15_m16.jpg')