#!/usr/bin/env python
#
#==============================================================================
# Initialization
#==============================================================================
# revision history
#  20200510 (Animesh): baseline software
#
# usage: python av_train_test
#
# This script runs training and testing sessions
#
#==============================================================================
# Import Modules
#==============================================================================
#
# import local modules
#
from rc_nn_tools import NNTools

#==============================================================================
# Global Variables
#==============================================================================
TRAIN_DATA = 'data/train.csv'
DEV_DATA = 'data/dev.csv'
TEST_DATA = 'data/test.csv'

SETTINGS = 'settings.json'

#==============================================================================
# Main Method
#==============================================================================
# method: main
#
# arguments: none
#
# return: none
#
# This method is the main function
#
def main():

    # servo training session
    servoTrain = NNTools(settings=SETTINGS, types=['servo','train'])
    servoTrain.load_model('models/servo_model.pth')
    servoTrain.train(TRAIN_DATA, DEV_DATA)

    # servo testing session
    servoTest = NNTools(settings=SETTINGS, types=['servo','test'])
    servoTest.test(TEST_DATA, display=True)

    # motor training session
    motorTrain = NNTools(settings=SETTINGS, types=['motor','train'])
    # servoTrain.load_model('models/servo_model.pth')
    motorTrain.train(TRAIN_DATA, DEV_DATA)

    # motor testing session
    motorTest = NNTools(settings=SETTINGS, types=['motor','test'])
    motorTest.test(TEST_DATA, display=True)

#==============================================================================
# Driver Program
#==============================================================================
if __name__ == "__main__":
    main()

#                                                                            
# end of file
# ANI717