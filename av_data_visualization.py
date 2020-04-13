#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200305 (Dr. Bai): baseline software
#  20200309 (Animesh): modification for accepting image files instead of 
#                      numpy array to reduce complexity and processing time
#
# usage: from av_data_visualization import CarDataFile
#
# This script refines dataset and explores prediction
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import cv2
import json
import pandas as pd

# import local modules
#
from av_nn_tools import NNTools
from av_parse_data import ParseData

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
IMAGE_LIST = 'data/list/list_0.csv'
NEW_LIST = 'data/list/list_0_1.csv'
SETTINGS = 'data/set_visual.json'

SPACE_KEY = ord(' ')
DEL_KEY = ord('d')
SAVE_KEY = ord('s')

#------------------------------------------------------------------------------
# Classes
#------------------------------------------------------------------------------

# class: DataTest
#
# This class refines dataset and explores prefdiction
#
class DataTest:

    #--------------------------------------------------------------------------
    # method: constructor
    #
    # arguments:
    #  dfile: image data holder file
    #  dwidth: width of the images
    #  dheight: height of the images
    #
    # return: none
    #
    def __init__(self, ifile=IMAGE_LIST, sfile=SETTINGS):

        self.data = pd.read_csv(ifile)
        self.len = len(self.data)
        self.parsedata = ParseData()
        self.badindex=[]

        with open(sfile) as fp:
            content = json.load(fp)
            
            self.shape = content['shape']
            self.servo_pred = NNTools(content["servo_setting"])
            self.motor_pred = NNTools(content["motor_setting"])
            self.servo_pred.load_model(content['servo_model'])
            self.motor_pred.load_model(content['motor_model'])

        return None
    #
    # end of method

    #--------------------------------------------------------------------------
    # method: display_pred
    #
    # arguments:
    #  index: index value
    #
    # return: none
    #
    # This method compares prediction with given data
    #
    def display_pred(self, index=0):
        
        # parse image, servo and motor data
        image,servo,motor = self.parsedata.parse_data(self.data["image"][index])
        
        # make prediction
        pred_servo =  self.servo_pred.predict(self.data["image"][index])
        pred_motor =  self.motor_pred.predict(self.data["image"][index])
        
        # process image with servo and motor values for displey
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        cv2.line(image, (240, 280), (240 - 20*(15 - servo), 100), \
                                     (255, 0, 0), 3)
        cv2.line(image, (220, 280), (220 - 20*(15 - pred_servo), 100), \
                                     (255, 255, 0), 3)
        image = cv2.putText(image, str(pred_motor) + ":" + str(motor), \
                                (180, 310), cv2.FONT_HERSHEY_SIMPLEX, 1, \
                                    (255,255,255), 2, cv2.LINE_AA)

        # show image
        cv2.imshow('picture {}'.format(index), cv2.cvtColor(image, \
                                   cv2.COLOR_RGB2BGR))
        cv2.moveWindow('picture {}'.format(index), 500,500)

        return None
    #
    # end of method

    #--------------------------------------------------------------------------
    # method: display
    #
    # arguments:
    #  index: index value
    #  key: provided key press
    #  nfile: new csv file to store refined images
    #
    # return: none
    #
    # This method displays images, also lets user to refine image set by 
    # deleting unwanted images
    #
    def display(self, nfile=NEW_LIST, index=0, key=SPACE_KEY):
        
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
        
        # process image with servo and motor values for displey
        image = cv2.resize(image, (self.shape[0], self.shape[1]), \
                           interpolation=cv2.INTER_CUBIC)
        cv2.line(image, (240, 300), (240 - 20*(15 - servo), 200), \
                             (255, 0, 0), 3)
        image = cv2.putText(image, str(motor), (180, 310),  \
                                  cv2.FONT_HERSHEY_SIMPLEX, \
                                     1, (255,255,255), 2, cv2.LINE_AA)
        
        # show image
        cv2.imshow('picture {}'.format(index), cv2.cvtColor(image, \
                               cv2.COLOR_RGB2BGR))
        cv2.moveWindow('picture {}'.format(index), 500,500)

        return None
    #
    # end of method







#------------------------------------------------------------------------------
# Debugging Block ANI717
#------------------------------------------------------------------------------
#import timeit
#QUIT_KEY = ord('q')
#total_start = timeit.default_timer()
#
#cardata = CarDataFile()
#for i in range(100):
#    cardata.display_pred(index=i)
#
#total_stop = timeit.default_timer()
#print('Total time required: %f' % (total_stop - total_start))