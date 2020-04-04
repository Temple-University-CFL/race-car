#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200305 (Dr. Bai): baseline software
#  20200306 (Animesh): formating and commenting
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
SETTINGS = 'data/set_visual.json'
IMAGE_LIST = 'data/list/list_0000_00.csv'
QUIT_KEY = ord('q')


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
    cardata = DataTest(IMAGE_LIST, SETTINGS)

    # loops over images to test prediction accuracy
    for index in range(cardata.len):

        # displays image with prediction
        cardata.display_pred(index=index)

        # sets waitkey for cv2.imshow()
        # waits for key press to show next image
        key = cv2.waitKey(0) & 0xFF

        # stops the program when 'q' is pressed
        if (key == QUIT_KEY):
            cv2.destroyAllWindows()
            break

#------------------------------------------------------------------------------
# Driver Program
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#                                                                              
# end of file