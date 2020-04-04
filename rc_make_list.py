#!/usr/bin/env python
#
#------------------------------------------------------------------------------
# Initialization
#------------------------------------------------------------------------------
# revision history
#  20200313 (Animesh): baseline software
#
# usage: python rc_make_list
#
# This script makes a list of images from given folders with start-end point
#
#------------------------------------------------------------------------------
# Import Modules
#------------------------------------------------------------------------------
#
# import global modules
#
import os
import pandas as pd

#------------------------------------------------------------------------------
# Global Variables
#------------------------------------------------------------------------------
CSV_LIST_FILE = 'data/list/all_image_list.csv'
FOLDER_LIST_FILE = 'data/set_train_test.csv'
DEF_END_COUNT = None

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

    # extract CSV file contents
    data = pd.read_csv(FOLDER_LIST_FILE)

    # define content holder
    content = []
    
    # define counter
    counter = 0
    
    for index in range(len(data)):

        # extract folder name
        folder = data['folder'][index]

        # extract all file names in a folder
        temp_content = os.listdir(folder)

        # initialize extract start and end point
        # extract them from csv folder file if provided
        start = 0
        end = len(temp_content)
        if isinstance(data['start'][index], str):
            start = temp_content.index(data['start'][index])
        if isinstance(data['end'][index], str):
            end = temp_content.index(data['end'][index])
        
        # truncate primary content list from given start to end point
        temp_content = temp_content[start:end]

        # append image data in content holder
        subcounter = 0
        for i in range(len(temp_content)):

            if DEF_END_COUNT:
                if counter == DEF_END_COUNT:
                    subcounter += 1
                    counter += 1
                    break
            
            name = folder + '/' + temp_content[i]
            content.append(name)
            subcounter += 1
            counter += 1
        
        # show status
        print('{}/ [Start:{:7d}] [End:{:7d}] [Length:{:7d}]'.format(folder, \
                                    start + 1, subcounter, subcounter - start))

    # convert to pandas dataframe and save it in a CSV file
    content = pd.DataFrame(content, columns=["image"])
    content.to_csv(CSV_LIST_FILE, index=False)

#------------------------------------------------------------------------------
# Driver Program
#------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#                                                                            
# end of file
# ANI717