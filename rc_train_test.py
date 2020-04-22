#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200306 (Animesh): baseline software
#  20200310 (Animesh): modified file path and names for proposed format
#
# usage: python rc_train_test
#
# This scriptruns training and testing sessions
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import local modules
#
from av_nn_tools import NNTools

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
TRAIN_DATA = 'data/list/train.csv'
TEST_DATA = 'data/list/test.csv'

SERVO_TRAIN_SETTING = "data/set_servo_train.json"
SERVO_TEST_SETTING = "data/set_servo_test.json"
SERVO_MODEL = 'models/servo_model.pth'

MOTOR_TRAIN_SETTING = "data/set_motor_train.json"
MOTOR_TEST_SETTING = "data/set_motor_test.json"
MOTOR_MODEL = 'models/motor_model.pth'

IMAGE_FILE = "data/images/03_06_2020_0/output_0002/i0000000_s15_m15.jpg"


#------------------------------------------------------------------------------
# Main Method
#------------------------------------------------------------------------------
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
    servo_train = NNTools(SERVO_TRAIN_SETTING)
    servo_train.train(TRAIN_DATA)
    servo_train.save_model(SERVO_MODEL)
    
    # # servo testing session
    # servo_test = NNTools(SERVO_TEST_SETTING)
    # servo_test.load_model(SERVO_MODEL)
    # servo_test.test(TEST_DATA)
    
    # # test on single file
    # servo_pred = NNTools(SERVO_TEST_SETTING)
    # servo_pred.load_model(SERVO_MODEL)
    # print(servo_pred.predict(IMAGE_FILE))

    # motor training session
    # motor_train = NNTools(MOTOR_TRAIN_SETTING)
    # motor_train.train(TRAIN_DATA)
    # motor_train.save_model(MOTOR_MODEL)
    
    # # motor testing session
    # motor_test = NNTools(MOTOR_TEST_SETTING)
    # motor_test.load_model(MOTOR_MODEL)
    # motor_test.test(TEST_DATA)
    
    # # test on single file
    # motor_pred = NNTools(MOTOR_TEST_SETTING)
    # motor_pred.load_model(MOTOR_MODEL)
    # print(motor_pred.predict(IMAGE_FILE))

#------------------------------------------------------------------------------
# Driver Program
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#                                                                            
# end of file
# ANI717