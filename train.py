#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Deep Learning Tool.

This script runs training session on Race-car dataset to predict servo and 
motor control values from a provided image. 

Revision History:
        2020-12-25 (Animesh): Baseline Software.

Example:
        $ python train.py

"""


#___Import Modules:
from _train_test import NNTools


#___Global Variables:
LIST = ['data/lists/Random/', 
        'data/lists/5 Fold Cross-Val/fold1/',
        'data/lists/5 Fold Cross-Val/fold2/',
        'data/lists/5 Fold Cross-Val/fold3/',
        'data/lists/5 Fold Cross-Val/fold4/',
        'data/lists/5 Fold Cross-Val/fold5/',
        'data/lists/Debug/',
        'data/']

BASE = LIST[7]

TRAIN_DATA = BASE + 'train.csv'
DEV_DATA = BASE + 'dev.csv'
SETTINGS = 'settings.json'

TYPE = 1 # 0: Motor Control Value, 1: Servo Control Value
PRETRAINED = 0 # 0: Train from Scratch, 1: Load Pretrained Weight


#___Main Method:
def main():
    """This is the Main Method.

    This method contains training session to predict speed and steering value.

    """
    
    if TYPE:
        
        # training session for servo control value prediction:
        servoTrain = NNTools(settings=SETTINGS, types=['servo','train'])
        
        # load pretrained weights if required
        if PRETRAINED:
            servoTrain.load_weights('models/servo.pth')
                
        servoTrain.train(TRAIN_DATA, DEV_DATA)
    
    else:
        
        # training session for motor control value prediction:
        motorTrain = NNTools(settings=SETTINGS, types=['motor','train'])
        
        # load pretrained weights if required
        if PRETRAINED:
            motorTrain.load_weights('models/servo.pth')
                
        motorTrain.train(TRAIN_DATA, DEV_DATA)

    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""