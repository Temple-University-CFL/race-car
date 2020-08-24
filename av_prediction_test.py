#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Prediction Testing Tool.

This script takes labeled image data and tests the accuracy of prediction from 
modeled neural network.

Revision History:
        2020-03-05 (Dr. Bai): Baseline Software.
        2020-03-06 (Animesh): Formating and Commenting.
        2020-07-25 (Animesh): Updated Docstring.

Example:
        $ python rc_prediction_test.py

"""


#___Import Modules:
import cv2
from rc_visualization import DataTest


#___Global Variables:
SETTINGS = 'settings.json'
QUIT_KEY = ord('q')

"""User has to provide here the path of image list for prediction"""
IMAGE_LIST = 'data/lists/Error/error.csv'


#___Main Method:
def main():
    """This is the Main Method.

    This method contains visualised session to evaluate prediction.

    """
    
    # creates CarDataFile type object
    cardata = DataTest(IMAGE_LIST, SETTINGS, True)

    # loops over images to test prediction accuracy
    for index in range(cardata.len):

        # displays image with prediction
        cardata.display_pred(index=index)

        # sets waitkey for cv2.imshow()
        # waits for key press to show next image
        key = cv2.waitKey(0) & 0xFF

        # stops the program when 'q' is pressed
        if (key == QUIT_KEY):

            # close wondow
            cv2.destroyAllWindows()
            break

        # close wondow
        cv2.destroyAllWindows()
    
    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""