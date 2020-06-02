#!/usr/bin/env python
#
#==============================================================================
# Initialization
#==============================================================================
# revision history
#  20200510 (Animesh): baseline software
#
# usage: from rc_nn_tools import NNTools
#
# This script contains required deep learnling tools
#
#==============================================================================
# Import Modules
#==============================================================================
#
# import global modules
#
import os
import json
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import torch modules
#
import torch
from torch import nn, optim
from torch.utils.data import DataLoader

# import local modules
#
from rc_nn_utility import Datagen, ParseData
from racecarNet import ServoNet, MotorNet

#==============================================================================
# Global Variables
#==============================================================================
TYPE = ["servo","test"]
SETTINGS = 'settings.json'
ODIR = "output/"
SEED = 717

#==============================================================================
# Classes
#==============================================================================

# class: NNTools
#
# This class contains required deep learning tools
#
class NNTools:

    #==========================================================================
    # method: constructor
    #
    # arguments:
    #  settings: setting file for class parameters
    #  types: [servo/motor,train/test] type
    #
    # return: none
    #
    def __init__(self, settings=SETTINGS, types=TYPE):

        self.type = types[0]

        # extract JSON file contents
        with open(settings) as fp:
            content = json.load(fp)[types[0]][types[1]]

            self.shape = content["shape"]            
            self.batch_size = content["batch"]
            self.cuda = content["cuda"]

            if types[1] == "train":
                self.epochs = content["epoch"]
            elif types[1] == "test":
                self.model_file = content["model"]

        # set neural net by type
        torch.manual_seed(SEED)
        if self.type == "servo":
            self.model = ServoNet(self.shape)
        elif self.type == "motor":
            self.model = MotorNet(self.shape)

        if types[1] == "train":
            self.log = self.set_output()
        else:
            self.load_model(self.model_file)

        # set output folders and required classes
        self.parsedata = ParseData()
        self.datagen = Datagen(shape=self.shape)

        return None
    #
    # end of method

    #==========================================================================
    # method: set_output
    #
    # arguments: none
    #
    # return: 
    #  log: log file path
    #
    # This method creates files and folders for producing output
    #
    def set_output(self):

        if not os.path.exists(ODIR):
            os.mkdir(ODIR)        
        if not os.path.exists(os.path.join(ODIR,"curves")):
            os.mkdir(os.path.join(ODIR,"curves"))        
        if not os.path.exists(os.path.join(ODIR,"models")):
            os.mkdir(os.path.join(ODIR,"models"))

        log = os.path.join(ODIR,"result.txt")
        if os.path.exists(log):
            os.remove(log)
            open(log, 'a').close()
        else:
            open(log, 'a').close()

        return log
    #
    # end of method

    #==========================================================================
    # method: train
    #
    # arguments:
    #  trainset: train dataset
    #  devset: dev dataset
    #
    # return: none
    #
    # This method runs training session
    #
    def train(self, trainset, devset):

        #----------------------------------------------------------------------
        trainset = pd.read_csv(trainset)["image"].values.tolist()

        # set neural network model and loss function
        if (self.cuda):
            model = self.model.cuda()
            criterion = nn.MSELoss().cuda()
        else:
            model = self.model
            criterion = nn.MSELoss()
        
        # set optimizer
        optimizer = optim.Adam(self.model.parameters(), lr=0.0001)

        # set dataloader
        dataloader = DataLoader(dataset=Datagen(trainset, self.shape), \
                                    batch_size=self.batch_size, shuffle=True)

        #----------------------------------------------------------------------
        total_loss = []
        dev_accuracy = []
        epoch_loss = 0.0
        accuracy = 0.0

        # loop over the dataset multiple times
        for epoch in range(1, self.epochs+1):

            # initialize train loss and running loss
            batch = 0
            running_loss = 0.0
            start = timeit.default_timer()

            for image, servo, motor in dataloader:

                batch += self.batch_size

                # set input and target
                input, target = self.set_io(image, servo, motor)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward + backward + optimize
                output = model(input)
                loss = criterion(target.unsqueeze(1), output)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

                # print status for every 100 mini-batches
                if batch % 100 == 0:                    
                    stop = timeit.default_timer()
                    print('[%3d, %5d] loss: %2.7f time: %2.3f dev: %2.0f' %
                        (epoch, batch, running_loss/100, \
                                 stop-start, accuracy))

                    epoch_loss = running_loss/100
                    running_loss = 0.0
                    start = timeit.default_timer()

            #------------------------------------------------------------------
            # accuracy count on dev set
            accuracy = self.test(devset)
            dev_accuracy.append(accuracy)

            # total loss count
            total_loss.append(epoch_loss)
            model_path = 'models/servo_model_epoch_%d.pth' % epoch
            self.save_model(mfile=os.path.join(ODIR,model_path))
            
            # plotting loss vs epoch curve, produces log file
            self.plot_result(epoch, total_loss, dev_accuracy)
        
        #show finish message
        if self.type == "servo":
            print("Servo model training finished!")
        if self.type == "motor":
            print("Motor model training finished!")

        return None
    #
    # end of method

    #==========================================================================
    # method: test
    #
    # arguments:
    #  testset: test dataset
    #
    # return: none
    #
    # This method runs testing session
    #
    def test(self, testset, display=False):

        #----------------------------------------------------------------------
        testset = pd.read_csv(testset)["image"].values.tolist()
        
        # set neural network model
        if (self.cuda):
            model = self.model.cuda()
        else:
            model = self.model

        # set dataloader
        dataloader = DataLoader(dataset=Datagen(testset, self.shape), \
                                    batch_size=self.batch_size, shuffle=False) 

        #----------------------------------------------------------------------

        # initialize train loss and running loss
        total_accuracy = 0.0
        count = 0

        for image, servo, motor in dataloader:

            count += self.batch_size

            # set input and target
            input, target = self.set_io(image, servo, motor)

            # accuracy calculation
            output = model(input).round()
            accuracy = abs(target.unsqueeze(1) - output) <= 1

            total_accuracy += sum(accuracy).item()

            if display and count%100 == 0:
                print("[%5d] accuracy: %2.2f" % \
                      (count, total_accuracy*100/count))

        if display:
            print("total accuracy = %2.2f" % (total_accuracy*100/len(testset)))

        return total_accuracy*100/len(testset)
    #
    # end of method

    #==========================================================================
    # method: set_io
    #
    # arguments:
    #  image: image tensor
    #  servo: servo tensor
    #  motor: motor tensor
    #
    # return: 
    #  input: input tensor
    #  target: target tensor
    #
    # This method sets input and target with/without GPU support
    #
    def set_io(self, image, servo, motor):

        if (self.cuda):
            input = image.cuda(non_blocking=True)
            if self.type == "servo":
                target = servo.cuda(non_blocking=True)
            elif self.type == "motor":
                target = motor.cuda(non_blocking=True)
        else:
            input = image
            if self.type == "servo":
                target = servo
            elif self.type == "motor":
                target = motor

        return input, target
    #
    # end of method

    #==========================================================================
    # method: plot_result
    #
    # arguments:
    #  image: image tensor
    #  servo: servo tensor
    #  motor: motor tensor
    #
    # return: 
    #  input: input tensor
    #  target: target tensor
    #
    # This method sets input and target with/without GPU support
    #
    def plot_result(self, epoch, total_loss, dev_accuracy):

        # plotting loss vs epoch curve
        plt.figure()
        plt.plot(range(1,epoch+1), total_loss, linewidth = 4)
        if self.type == "servo":
            plt.title("Servo Data Training")
            fig_path = ODIR + "/curves/Servo Loss Curve.png"
        elif self.type == "motor":
            plt.title("Motor Data Training")
            fig_path = ODIR + "/curves/Motor Loss Curve.png"

        plt.ylabel("Loss")
        plt.xlabel("Epoch")
        plt.savefig(fig_path)
        plt.close()

        #----------------------------------------------------------------------
        # dev accuracy vs epoch curve
        plt.figure()
        plt.plot(range(1,epoch+1), dev_accuracy, linewidth = 4)
        
        if self.type == "servo":
            plt.title("Servo Data Training")
            fig_path = ODIR + "/curves/Servo Accuracy Curve.png"
        elif self.type == "motor":
            plt.title("Motor Data Training")
            fig_path = ODIR + "/curves/Motor Accuracy Curve.png"

        plt.xlabel("Epoch")
        plt.ylabel("Dev Accuracy")
        plt.savefig(fig_path)
        plt.close()
        
        #----------------------------------------------------------------------
        # save accuracy values and show finish message
        if self.type == "servo":
            content = "Servo Model: epoch %d - accuracy: %2.2f - best %d\n" \
                    % (epoch, dev_accuracy[epoch-1], np.argmax(dev_accuracy)+1)
        if self.type == "motor":
            content = "Motor Model: epoch %d - accuracy: %2.2f - best %d\n" \
                    % (epoch, dev_accuracy[epoch-1], np.argmax(dev_accuracy)+1)

        # write in log
        with open(self.log, 'a') as fp:
            fp.write(content)

        return None
    #
    # end of method

    #==========================================================================
    # method: predict
    #
    # arguments:
    #  image: input image
    #
    # return: prediction for single image
    #
    # This method takes an image and predicts servo/motor value from ginen type
    #
    def predict(self, iname):
             
        image = self.datagen.get_image(iname)
        
        # implement GPU support if required
        if (self.cuda):
            model = self.model.cuda()
        else:
            model = self.model

        # return prediction
        if (self.cuda):
            return model(image.cuda(non_blocking=True)).round().int().item()
        else:
            return model(image).round().int().item()
    #
    # end of method

    #==========================================================================
    # method: save_model
    #
    # arguments:
    #  mfile: input model file
    #
    # return: none
    #
    # This method saves a model
    #
    def save_model(self, mfile='models/servo_model.pth'):
        
        if self.type == "servo":
            print('Saving servo Model ')
            torch.save(self.model.state_dict(), mfile)      
        elif self.type == "motor":
            print('Saving motor Model ')
            torch.save(self.model.state_dict(), mfile)
    
        return None
    #
    # end of method

    #==========================================================================
    # method: load_model
    #
    # arguments:
    #  mfile: input model file
    #
    # return: none
    #
    # This method loads a model
    #
    def load_model(self, model_file):

        # Load model from given file
        self.model.load_state_dict(torch.load(model_file, \
                                             map_location=torch.device('cpu')))

        return None
    #
    # end of method

#==============================================================================







#==============================================================================
# Debugging Block ANI717
#==============================================================================
#a = NNTools("data/set_servo_train.json")
#a.train('data/list/list_0.csv')
#a.save_model('models/servo_model.pth')

#aa = NNTools("data/set_servo_test.json")
#aa.load_model('models/servo_model.pth')
#aa.test('data/list/list_2.csv')
#print(aa.predict("data/images/output_0002/i0000000_s15_m15.jpg"))
    
#b = NNTools("data/set_motor_train.json")
#b.train('data/list/list_0.csv')
#b.save_model('models/motor_model.pth')

#bb = NNTools("data/set_motor_test.json")
#bb.load_model('models/motor_model.pth')
#bb.test('data/list/list_2.csv')
#print(bb.predict("data/images/output_0002/i0000000_s15_m15.jpg"))