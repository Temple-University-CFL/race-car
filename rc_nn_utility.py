#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Utility Class.

This script contains data generator and data parsing tools. 

Revision History:
        2020-05-15 (Animesh): Baseline Software.
        2020-07-30 (Animesh): Updated Docstring.

Example:
        from rc_nn_utility import Datagen, ParseData

"""


#___Import Modules:
import cv2

import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms


#___Global Variables:
SHAPE = [100,100]


#__Classes:
class Datagen(Dataset):
    """Neural Network Data Generator.
    
    This class contains all methods to handle data generation for deep learning
    session.
    
    """

    def __init__(self, ilist=None, shape=SHAPE):
        """Constructor.
        
        Args:
            ilist (list): A list of input images.
            ishape (list): A list containing image shape [width, height].

        """
        
        self.transform = transforms.Compose([transforms.ToTensor()])
        
        self.ilist = ilist
        self.shape = shape
        
        self.parsedata = ParseData()

        return None
    

    def get_image(self, ifile):
        """Image to Tensor converter.
        
        This method takes an image and returns as deep learning compatible 
        image tensor with proper transformation.
        
        Args:
            ifile (image file): Image file as input.
        
        Returns:
            image (image tensor): Transformed image tensor.

        """
        
        image = self.parsedata.parse_image(ifile)
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        image = self.transform(image)
        return image.unsqueeze(0)


    def __getitem__(self, index):
        """Getitem Method.
        
        This method takes image, servo and motor data and returns them as 
        deep learning compatible tensor with proper transformation.
        
        Args:
            index (int): An integer indicating required data index from 
            provided list.
        
        Returns:
            image (image tensor): Transformed image tensor.
            servo (tensor): Servo data in tensor form.
            motor (tensor): Motor data in tensor form.

        """
        
        # parse image, servo and motor data
        image,servo,motor = self.parsedata.parse_data(self.ilist[index])
        
        # convert image, servo and motor data to tensor
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        image = self.transform(image)
        servo = torch.tensor(float(servo))
        motor = torch.tensor(float(motor))
        
        return image, servo, motor


    def __len__(self):
        """Len Method.
        
        This method returns the length of provided list.

        """
        
        return len(self.ilist)


class ParseData:
    """Data Parser Class
    
    This class contains all tools to parse servo, motor and image data from a 
    given list item.
    
    """

    def __init__(self):
        """Constructor.

        """

        return None


    def parse_data(self, fname):
        """Data Parser.
        
        This method parses data from a given file name.
        
        Args:
            fname (string): File name containing image directory along with 
                servo and motor value.

        Returns:
            (image file): Image file in opencv format.
            (int): Servo value.
            (int): Motor value.
        
        """
        
        return self.parse_image(fname), \
                    self.parse_servo(fname), self.parse_motor(fname)

    
    def parse_image(self, fname):
        """Image Parser.
        
        This method parses image from a given file name.
        
        Args:
            fname (string): File name containing image directory.

        Returns:
            (image file): Image file in opencv format.
        
        """

        return cv2.imread(fname)
    

    def parse_servo(self, fname):
        """Servo Data Parser.
        
        This method parses servo data from a given file name.
        
        Args:
            fname (string): File name containing image directory along with 
                servo and motor value.

        Returns:
            (int): Servo value.
        
        """
        
        return int(fname.split('/')[-1].split('.')[0].split('_')[-2][1:3])
    
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
        """Motor Data Parser.
        
        This method parses motor data from a given file name.
        
        Args:
            fname (string): File name containing image directory along with 
                servo and motor value.

        Returns:
            (int): Motore value.
        
        """
        
        return int(fname.split('/')[-1].split('.')[0].split('_')[-1][1:3])


#                                                                              
# end of file
"""ANI717"""