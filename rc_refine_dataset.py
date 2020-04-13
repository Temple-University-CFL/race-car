#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200305 (Dr. Bai): baseline software
#  20200309 (Animesh): formating and commenting
#
# usage: python rc_prediction_test
#
# This script takes labeled image data and tests the accuracy of prediction 
# from modeled neural network
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import cv2

# import local modules
#
from av_data_visualization import DataTest

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
QUIT_KEY = ord('q')
SAVE_KEY = ord('s')
IMG_FILE = 'data/list/check.csv'
REFINED_FILE = 'data/list/train_01.csv'

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

    # creates CarDataFile type object
    cardata = DataTest(ifile=IMG_FILE)
    key = 32

    # loops over images to test prediction accuracy
    for index in range(cardata.len):

        # displays image with prediction
        cardata.display(index=index, key=key)

        # sets waitkey for cv2.imshow()
        # waits for key press to show next image
        key = cv2.waitKey(0) & 0xFF
        
        # stops the program and saves data when list ends
        if index == cardata.len-1:
            cardata.display(nfile=REFINED_FILE, index=index, key=SAVE_KEY)
            cv2.destroyAllWindows()
            break

        # stops the program when 'q' is pressed
        # saves data when 's' is pressed
        if (key == QUIT_KEY):
            cv2.destroyAllWindows()
            break
        elif (key == SAVE_KEY):
            cardata.display(nfile=REFINED_FILE, index=index, key=key)
            cv2.destroyAllWindows()
            break

#------------------------------------------------------------------------------
# Driver Program
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#                                                                              
# end of file