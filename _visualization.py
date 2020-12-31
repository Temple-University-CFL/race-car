#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Visualization Utility Class.

This script contains required tools to refine dataset and explore prediction
visually. 

Revision History:
        2020-03-09 (Animesh): Baseline Software.
        2020-08-15 (Animesh): Updated Docstring, compatible with dynamic 
                              resolution, improved Interface.

Example:
        from _visualization import DataTest

"""


#___Import Modules:
import cv2
import json
import math
import pandas as pd

from _train_test import NNTools
from _parser import ParseData


#___Global Variables:
IMAGE_LIST = 'data/list/list_0.csv'
NEW_LIST = 'data/list/list_0_1.csv'
SETTINGS = 'settings.json'

SPACE_KEY = ord(' ')
DEL_KEY = ord('d')
SAVE_KEY = ord('s')


#__Classes:
class DataTest:
    """Data Test Class.
    
    This class contains all methods to refine dataset and test prediction on
    visually.
    
    """

    def __init__(self, ifile=IMAGE_LIST, sfile=SETTINGS, predict=None):
        """Constructor.
        
        Args:
            ifile (csv file): This file contains list of images.
            sfile (json file): This file contains all user setting.
            predict (boolian): This flag determines the session is for 
                prediction or not.

        """

        self.data = pd.read_csv(ifile)
        self.len = len(self.data)
        self.badindex=[]

        with open(sfile) as fp:
            content = json.load(fp)['display']       
            self.position = content['position']
            self.shape = content['shape']
            self.motor_flag = content['motor_flag']
            self.watermark = content['watermark']
            self.angle = math.pi*content['angle']/90

        if predict:
            self.servo_pred = NNTools(sfile, ['servo','test'])
            self.motor_pred = NNTools(sfile, ['motor','test'])

        self.parsedata = ParseData()


    def display_pred(self, index=0):
        """Method for Prediction Test.
        
        This method takes images and display them with target and prediction
        values.
        
        Args:
            index (int): Index value pointing image list.

        """
        
        # parse image, servo and motor data
        image,servo,motor = self.parsedata.parse_data(self.data["image"][index])
        
        # make prediction
        pred =  self.servo_pred.predict(image) 
        
        # reshape image for displey
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)

        # set base point
        origin = [self.shape[0]//2, self.shape[1]-20]

        # line display for showing steering angle
        cv2.line(image, (origin[0], origin[1]-40), \
            (origin[0]-2*int(math.sin(self.angle*(5-servo)/10)*origin[1]/3), \
             origin[1]-40-2*int(math.cos(self.angle*(5-servo)/10)*origin[1]/3)), \
                     (127,255,0), 5)
        cv2.line(image, (origin[0], origin[1]-40), \
            (origin[0]-2*int(math.sin(self.angle*(5-pred)/10)*origin[1]/3), \
             origin[1]-40-2*int(math.cos(self.angle*(5-pred)/10)*origin[1]/3)), \
                     (255,127,0), 5)
        
        # display target and prediction with texts
        image = cv2.putText(image, ":", \
                                (origin[0]-5, origin[1]), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,255,255), 2, cv2.LINE_AA)
        image = cv2.putText(image, "(Target)" + str(servo), \
                                (origin[0]-215, origin[1]), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (127,255,0), 2, cv2.LINE_AA)
        image = cv2.putText(image, str(pred) + "(Predict)", \
                                (origin[0]+12, origin[1]), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,127,0), 2, cv2.LINE_AA)
        
        # display motor value
        if self.motor_flag:
            pred = self.motor_pred.predict(self.data["image"][index])
            image = cv2.putText(image, ":", \
                                (origin[0]-5, 40), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,255,255), 2, cv2.LINE_AA)
            image = cv2.putText(image, "(Target)" + str(motor), \
                                (origin[0]-215, 40), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (127,255,0), 2, cv2.LINE_AA)
            image = cv2.putText(image, str(pred) + "(Predict)", \
                                (origin[0]+12, 40), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,127,0), 2, cv2.LINE_AA)

        # display watermark
        if self.watermark:
            image = cv2.putText(image, "ANI717", \
                                (20, 40), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,255,255), 2, cv2.LINE_AA)

        # show image
        cv2.imshow('picture {}'.format(index), cv2.cvtColor(image, \
                                   cv2.COLOR_RGB2BGR))
        cv2.moveWindow('picture {}'.format(index), *self.position)

        return None


    def display(self, nfile=NEW_LIST, index=0, key=SPACE_KEY):
        """Method for Refine Dataset.
        
        This method displays images, also lets user to refine image set by 
        deleting unwanted images.
        
        Args:
            index (int): Index value pointing image list.
            key (key press): Provided key press.
            nfile (csv file): New csv file to store refined images

        """
        
        # when 'd' is pressed, (index-1) value is appended in badindex array
        # when 's' is pressed, all image data except deleted indices is saved
        # to new CSV image data file
        if (key == DEL_KEY):
            self.badindex.append(index-1)
            cv2.destroyWindow('picture {}'.format(index-1))
        elif (key == SAVE_KEY):
            ref_data = self.data[0:index].drop(self.badindex)
            ref_data.to_csv(nfile, index=False)
        else:
            cv2.destroyWindow('picture {}'.format(index-1))

        # parse image, servo and motor data
        image,servo,motor = self.parsedata.parse_data(self.data["image"][index])
        
        # reshape image for displey
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)

        # set base point
        origin = [self.shape[0]//2, self.shape[1]-20]
        
        # line display for showing steering angle
        cv2.line(image, (origin[0], origin[1]-40), \
            (origin[0]-2*int(math.sin(self.angle*(5-servo)/10)*origin[1]/3), \
             origin[1]-40-2*int(math.cos(self.angle*(5-servo)/10)*origin[1]/3)), \
                         (0,255,0), 7)
        
        # display target and prediction with texts
        image = cv2.putText(image, str(servo), \
                                (origin[0]-30, origin[1]), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,255,255), 2, cv2.LINE_AA)
        
        # display motor value
        if self.motor_flag:
            image = cv2.putText(image, str(motor), \
                                (origin[0]-30, 40), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,255,255), 2, cv2.LINE_AA)
        
        # display watermark
        if self.watermark:
            image = cv2.putText(image, "ANI717", \
                                (20, 40), \
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, \
                                    (255,255,255), 2, cv2.LINE_AA)

        # show image
        cv2.imshow('picture {}'.format(index), cv2.cvtColor(image, \
                                   cv2.COLOR_RGB2BGR))
        cv2.moveWindow('picture {}'.format(index), *self.position)

        return None


#                                                                              
# end of file
"""ANI717"""