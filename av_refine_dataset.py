#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Race-car Dataset Refining Tool.

This script takes labeled image data and deletes them when they are 
unrealistic and faulty.

Revision History:
        2020-03-05 (Dr. Bai): Baseline Software
        2020-03-09 (Animesh): Formating and Commenting
        2020-07-25 (Animesh): Updated Docstring

Example:
        $ python rc_refine_dataset.py

"""


#___Import Modules:
import cv2
from rc_visualization import DataTest


#___Global Variables:
IMAGE_LIST = 'data/lists/error.csv'
REFINED_LIST = 'data/lists/check_01.csv'

SETTINGS = 'settings.json'
QUIT_KEY = ord('q')
SAVE_KEY = ord('s')


#___Main Method:
def main():
    """This is the Main Method.

    This method contains visualised session to refine racecar dataset.

    Returns:
        None

    """

    # creates CarDataFile type object
    cardata = DataTest(IMAGE_LIST, SETTINGS)
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
            cardata.display(nfile=REFINED_LIST, index=index, key=SAVE_KEY)
            cv2.destroyAllWindows()
            break

        # stops the program when 'q' is pressed
        # saves data when 's' is pressed
        if (key == QUIT_KEY):
            cv2.destroyAllWindows()
            break
        elif (key == SAVE_KEY):
            cardata.display(nfile=REFINED_LIST, index=index, key=key)
            cv2.destroyAllWindows()
            break
        
    return None


#___Driver Program:
if __name__ == "__main__":
    main()


#                                                                              
# end of file
"""ANI717"""